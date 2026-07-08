// Vercel serverless function: /api/contact
// Receives the website contact form and texts a lead alert to your phone via Telnyx.
// No database. This is the only server-side piece, and it exists solely to keep the
// Telnyx API key off the client.
//
// Set these in Vercel > Project > Settings > Environment Variables:
//   TELNYX_API_KEY               Telnyx API key (starts with "KEY...")
//   TELNYX_PHONE_NUMBER          number to send FROM, E.164 (e.g. +14045551234)
//   NOTIFICATION_PHONE           number to text (your cell), E.164 (e.g. +14045550000)
//   TELNYX_MESSAGING_PROFILE_ID  (optional) messaging profile the from-number is on

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  const body = typeof req.body === 'object' && req.body ? req.body : {};

  // Honeypot: bots tick this hidden field. Accept quietly and drop.
  if (body.botcheck) return res.status(200).json({ ok: true });

  const name = (body.name || '').toString().trim();
  const email = (body.email || '').toString().trim();
  const message = (body.message || '').toString().trim();
  const company = (body.company || '').toString().trim();
  const phone = (body.phone || '').toString().trim();
  const interest = (body.interest || '').toString().trim();

  if (!name || !email || !message) {
    return res.status(400).json({ ok: false, error: 'Missing required fields' });
  }

  const apiKey = process.env.TELNYX_API_KEY;
  const from = process.env.TELNYX_PHONE_NUMBER;
  const to = process.env.NOTIFICATION_PHONE;
  const profileId = process.env.TELNYX_MESSAGING_PROFILE_ID;

  if (!apiKey || !from || !to) {
    console.error('SMS not configured: need TELNYX_API_KEY, TELNYX_PHONE_NUMBER, NOTIFICATION_PHONE');
    return res.status(500).json({ ok: false, error: 'Notification not configured' });
  }

  const text = [
    'New lead - Rocket Solutions',
    company ? `${name} (${company})` : name,
    phone ? `${email} / ${phone}` : email,
    interest ? `Interest: ${interest}` : null,
    '',
    message.slice(0, 600)
  ].filter(v => v !== null).join('\n');

  try {
    const r = await fetch('https://api.telnyx.com/v2/messages', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from,
        to,
        text,
        ...(profileId ? { messaging_profile_id: profileId } : {})
      })
    });
    const data = await r.json();
    if (!r.ok) {
      console.error('Telnyx error:', JSON.stringify(data));
      return res.status(502).json({ ok: false, error: 'Failed to send notification' });
    }
    return res.status(200).json({ ok: true, id: data && data.data ? data.data.id : null });
  } catch (err) {
    console.error('SMS request failed:', err);
    return res.status(500).json({ ok: false, error: 'Failed to send notification' });
  }
}