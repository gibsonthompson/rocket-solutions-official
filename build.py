#!/usr/bin/env python3
# Generates the service pages + contact page for Rocket Solutions.
# All pages share styles.css + app.js and the same nav/footer shell.

ICONS = {
  "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.1-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.4-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>',
  "cal": '<path d="M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/><path d="M9 15l2 2 4-4"/>',
  "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  "trend": '<path d="M3 17l6-6 4 4 8-8M21 7v5M21 7h-5"/>',
  "check": '<path d="M4 12l5 5L20 6"/>',
  "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
  "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/>',
  "bolt": '<path d="M13 2 3 14h7l-1 8 10-12h-7l1-8Z"/>',
  "grid": '<rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/>',
  "gear": '<path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/><circle cx="12" cy="12" r="3.4"/>',
  "transfer": '<path d="M16 3l4 4-4 4M20 7H8M8 21l-4-4 4-4M4 17h12"/>',
  "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="M9 12l2 2 4-4"/>',
  "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/>',
  "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
  "bars": '<path d="M3 3v18h18M7 14v4M12 9v9M17 5v13"/>',
  "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>',
  "cursor": '<path d="M3 3l7.5 18 2.5-7.5L20.5 11 3 3Z"/>',
  "layers": '<path d="M12 2 2 7l10 5 10-5-10-5Z"/><path d="M2 12l10 5 10-5M2 17l10 5 10-5"/>',
  "cycle": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
  "mega": '<path d="M11 5 6 9H2v6h4l5 4V5Z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M19 5a10 10 0 0 1 0 14"/>',
  "sparkle": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3Z"/>',
  "map": '<path d="M9 3 3 5v16l6-2 6 2 6-2V3l-6 2-6-2Z"/><path d="M9 3v16M15 5v16"/>',
  "gauge": '<path d="M12 13l4-4"/><path d="M3 17a9 9 0 1 1 18 0"/>',
  "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5Z"/>',
}

def icon(key, size=24, sw=1.9, stroke="currentColor"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg>')

MONOGRAM_DEFS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <linearGradient id="burn" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#F9743B"/><stop offset="55%" stop-color="#F0432A"/><stop offset="100%" stop-color="#C31C36"/></linearGradient>
  <symbol id="rs-monogram" viewBox="0 0 40 40">
    <rect width="40" height="40" rx="11" fill="url(#burn)"/>
    <path d="M20 8.5 C24.5 12.5 26 18 26 22.4 L22.4 25.8 H17.6 L14 22.4 C14 18 15.5 12.5 20 8.5 Z" fill="#fff"/>
    <circle cx="20" cy="18" r="2.5" fill="#F0432A"/>
    <path d="M17.6 25.8 L15.4 31.5 L19.2 28.8 Z M22.4 25.8 L24.6 31.5 L20.8 28.8 Z" fill="#fff" opacity=".92"/>
  </symbol>
</defs></svg>'''

def nav(active):
    items = [("Home","index.html"),("Voice AI","voice-ai.html"),("Websites","websites.html"),
             ("Software","software.html"),("Automation","automation.html"),("Contact","contact.html")]
    links = "".join(
        f'<a class="item{" active" if a==active else ""}" href="{h}">{a}</a>' for a,h in items)
    arrow = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
    return f'''<header class="nav" id="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="index.html" aria-label="Rocket Solutions home">
      <svg class="monogram"><use href="#rs-monogram"/></svg>
      <span class="word">Rocket Solutions</span>
    </a>
    <nav class="nav-menu" id="navMenu">{links}</nav>
    <div class="nav-right">
      <a class="btn btn-primary desk" href="contact.html">Start a project {arrow}</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Menu" aria-expanded="false">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>
      </button>
    </div>
  </div>
</header>'''

FOOTER = '''<footer class="site">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <a class="brand" href="index.html"><svg class="monogram"><use href="#rs-monogram"/></svg><span class="word">Rocket Solutions</span></a>
        <p>A technology firm that builds the systems businesses run on. Georgia based, delivering nationwide.</p>
      </div>
      <div class="foot-col"><div class="h">Capabilities</div>
        <a href="voice-ai.html">Voice AI</a><a href="websites.html">Websites</a><a href="software.html">Custom Software</a><a href="automation.html">AI Automation</a></div>
      <div class="foot-col"><div class="h">Firm</div>
        <a href="index.html">Home</a><a href="contact.html">Contact</a><a href="mailto:hello@gorocketsolutions.com">Email us</a></div>
      <div class="foot-col"><div class="h">Get started</div>
        <a href="contact.html">Start a project</a><a href="contact.html">Book a call</a></div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 Rocket Solutions LLC. All rights reserved.</span>
      <span>Georgia, United States</span>
    </div>
  </div>
</footer>'''

ARROW = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#FBF7F1" />
<script>document.documentElement.classList.add('js')</script>
<link rel="icon" type="image/png" href="/logo.png" />
<link rel="preconnect" href="https://api.fontshare.com" crossorigin />
<link href="https://api.fontshare.com/v2/css?f[]=clash-display@500,600,700&f[]=satoshi@400,500,700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="styles.css" />
<style>
  .svc-hero {{ position: relative; overflow: hidden; padding: clamp(36px,5vw,72px) 0 clamp(56px,7vw,96px); }}
  .svc-hero .orb {{ position: absolute; border-radius: 50%; background: var(--grad-dawn); filter: blur(20px); pointer-events: none; }}
  .svc-hero .orb.a {{ width: 520px; height: 520px; right: -150px; top: -120px; opacity: .5; }}
  .svc-hero .orb.b {{ width: 300px; height: 300px; left: -160px; bottom: -40px; opacity: .32; }}
  .svc-hero .wrap {{ position: relative; z-index: 1; }}
  .svc-grid {{ display: grid; grid-template-columns: 1.1fr 0.9fr; gap: clamp(30px,5vw,68px); align-items: center; }}
  .svc-hero .eyebrow {{ margin-bottom: 26px; }}
  .svc-hero h1 {{ font-family: var(--display); font-weight: 600; font-size: clamp(40px,5.6vw,76px); line-height: 1.0; letter-spacing: -0.03em; margin-bottom: 24px; }}
  .svc-hero .lead {{ max-width: 32em; margin-bottom: 34px; }}
  .svc-actions {{ display: flex; gap: 15px; flex-wrap: wrap; }}
  .stage {{ position: relative; height: clamp(340px,38vw,440px); }}
  .stage-orb {{ position: absolute; inset: 8% 8% 8% 8%; border-radius: 46% 54% 52% 48% / 55% 48% 52% 45%; background: var(--grad-dawn); box-shadow: 0 40px 100px -40px rgba(240,67,42,.5); }}
  .stage-orb.inner {{ inset: 22% 20% 22% 20%; background: var(--grad-burn); opacity: .9; border-radius: 52% 48% 46% 54% / 48% 55% 45% 52%; }}
  .float-card {{ animation: bob 6s ease-in-out infinite; }}
  .float-card:nth-of-type(3) {{ animation-delay: -2s; }} .float-card:nth-of-type(4) {{ animation-delay: -4s; }}
  @keyframes bob {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-12px); }} }}
  .fc-a {{ top: 4%; left: -4%; }} .fc-b {{ top: 44%; right: -6%; }} .fc-c {{ bottom: 4%; left: 12%; }}

  .stakes {{ padding: clamp(20px,3vw,32px) 0; }}
  .stakes-panel {{ position: relative; overflow: hidden; background: var(--grad-soft); border: 1px solid var(--line-2); border-radius: var(--r-lg); padding: clamp(36px,5vw,68px); }}
  .stakes-panel .sp-orb {{ position: absolute; right: -80px; bottom: -100px; width: 300px; height: 300px; border-radius: 50%; background: var(--grad-dawn); opacity: .5; filter: blur(14px); }}
  .stakes-panel .inner {{ position: relative; max-width: 30em; }}
  .stakes-panel .k {{ font-size: 14px; font-weight: 600; color: var(--red); letter-spacing: 0.02em; margin-bottom: 16px; }}
  .stakes-panel p {{ font-family: var(--display); font-weight: 500; font-size: clamp(24px,3.2vw,40px); line-height: 1.14; letter-spacing: -0.02em; }}
  .stakes-panel p .accent {{ color: var(--red); }}

  @media (max-width: 1000px) {{
    .svc-grid {{ grid-template-columns: 1fr; gap: 40px; }}
    .stage {{ max-width: 440px; }}
  }}
  @media (max-width: 760px) {{ .fc-a {{ left: 0; }} .fc-b {{ right: 0; }} }}
</style>
</head>
<body>
'''

def float_card(pos, ic_key, k, v):
    return f'''<div class="float-card fc-{pos}">
      <div class="fc-ic" style="background:var(--blush)">{icon(ic_key, 20, 2, "#C31C36")}</div>
      <div><div class="fc-k">{k}</div><div class="fc-v">{v}</div></div>
    </div>'''

def service_page(s):
    fcards = "\n      ".join(float_card(p, ic, k, v) for p,(ic,k,v) in zip(["a","b","c"], s["cards"]))
    outcomes = "\n        ".join(
        f'''<div class="outcome-card reveal{f" d{i}" if i else ""}">
          <div class="oc-ic">{icon(ic,22,2,"#C31C36")}</div>
          <h4>{t}</h4><p>{d}</p>
        </div>''' for i,(ic,t,d) in enumerate(s["outcomes"]))
    included = "\n        ".join(
        f'''<div class="inc-item"><div class="ic">{icon("check",15,2.4,"#C31C36")}</div>
          <div><h5>{t}</h5><p>{d}</p></div></div>''' for t,d in s["included"])
    steps = "\n        ".join(
        f'''<div class="stepc reveal{f" d{i}" if i else ""}"><div class="sn">{i+1:02d}</div>
          <h4>{t}</h4><p>{d}</p></div>''' for i,(t,d) in enumerate(s["steps"]))

    return HEAD.format(title=s["title"], desc=s["desc"]) + MONOGRAM_DEFS + nav(s["active"]) + f'''
<main>
  <section class="svc-hero">
    <div class="orb a"></div><div class="orb b"></div>
    <div class="wrap">
      <div class="svc-grid">
        <div>
          <span class="eyebrow"><span class="dot"></span> {s["eyebrow"]}</span>
          <h1>{s["h1"]}</h1>
          <p class="lead">{s["lead"]}</p>
          <div class="svc-actions">
            <a class="btn btn-primary" href="contact.html">Start a project {ARROW}</a>
            <a class="btn btn-ghost" href="#how">How it works</a>
          </div>
        </div>
        <div class="stage" aria-hidden="true">
          <div class="stage-orb"></div><div class="stage-orb inner"></div>
          {fcards}
        </div>
      </div>
    </div>
  </section>

  <section class="stakes">
    <div class="wrap">
      <div class="stakes-panel reveal">
        <div class="sp-orb"></div>
        <div class="inner">
          <div class="k">{s["stakes_k"]}</div>
          <p>{s["stakes"]}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal"><span class="eyebrow"><span class="dot"></span> What you get</span>
        <h2 class="h2">{s["outcomes_head"]}</h2></div>
      <div class="outcomes" style="margin-top:clamp(40px,5vw,64px)">
        {outcomes}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head reveal"><span class="eyebrow"><span class="dot"></span> What is included</span>
        <h2 class="h2">Everything, handled for you.</h2></div>
      <div class="included" style="margin-top:clamp(36px,4vw,52px)">
        {included}
      </div>
    </div>
  </section>

  <section class="section" id="how" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head reveal"><span class="eyebrow"><span class="dot"></span> How it works</span>
        <h2 class="h2">Live in weeks, not months.</h2></div>
      <div class="stepline" style="margin-top:clamp(40px,5vw,64px)">
        {steps}
      </div>
    </div>
  </section>

  <section class="section tight">
    <div class="wrap">
      <div class="cta-band reveal">
        <div class="cta-orb orb-a"></div><div class="cta-orb orb-b"></div>
        <h2 class="h2">{s["cta_h"]}</h2>
        <p>{s["cta_p"]}</p>
        <div class="cta-actions">
          <a class="btn btn-white" href="contact.html">Start a project {ARROW}</a>
          <a class="btn" style="background:rgba(255,255,255,.1);color:#fff;border-color:rgba(255,255,255,.2)" href="index.html">Back to home</a>
        </div>
      </div>
    </div>
  </section>
</main>
''' + FOOTER + '\n<script src="app.js"></script>\n</body>\n</html>\n'


SERVICES = [
 {
  "slug":"voice-ai","active":"Voice AI","eyebrow":"Voice AI",
  "title":"Voice AI | Rocket Solutions",
  "desc":"An always on AI receptionist that answers, books, and routes every call so you never lose a customer to a missed call.",
  "h1":"Answer every call.<br>Book every job.<br>Even at 2am.",
  "lead":"Most businesses quietly lose money to calls that ring out. Your AI receptionist picks up every time, answers the questions, books the appointment, and texts you the details, so a missed call never means a missed customer again.",
  "cards":[("phone","Incoming call","Answered live"),("cal","New booking","Tue, 2:00 PM"),("transfer","Hot lead","Transferred to you")],
  "stakes_k":"The cost of a missed call",
  "stakes":'A missed call is a customer who simply dials <span class="accent">the next business on the list.</span> We make sure that never happens to you again.',
  "outcomes_head":"More revenue, a fuller calendar, and time back.",
  "outcomes":[
    ("trend","Never miss revenue","Every call answered, day or night, so the jobs you used to lose now land on your calendar instead of a competitor's."),
    ("cal","A calendar that fills itself","Callers get booked on the spot, with confirmations and reminders handled automatically. No phone tag."),
    ("clock","Hours back in your day","Your team stops chasing the phone and focuses on the work that actually gets paid."),
  ],
  "included":[
    ("24/7 answering","Every call picked up in seconds, around the clock, including nights, weekends, and holidays."),
    ("Appointment booking","Callers are booked straight onto your calendar with automatic confirmations."),
    ("Smart call routing","The right call reaches the right place based on your rules."),
    ("Live transfer","Hot leads and urgent calls get handed to your team in real time."),
    ("Spam screening","Robocalls and time wasters are filtered out before they reach you."),
    ("Caller recognition","Returning customers are greeted by name with their history on hand."),
    ("Instant text summaries","Every call arrives on your phone as a clean, readable summary."),
    ("Your voice and script","It sounds like your brand and answers exactly how you would."),
  ],
  "steps":[
    ("We learn your business","We map your hours, services, pricing, and how you like calls handled."),
    ("We build and train it","We shape a receptionist that sounds like your brand and knows your answers cold."),
    ("It goes live","Calls get answered, jobs get booked, and every detail lands on your phone."),
  ],
  "cta_h":"Stop paying for calls<br>you never answer.",
  "cta_p":"Tell us about your call volume and we will show you exactly how many opportunities you are leaving on the table, and how we would capture them.",
 },
 {
  "slug":"websites","active":"Websites","eyebrow":"Websites",
  "title":"Websites | Rocket Solutions",
  "desc":"Fast, search ready websites engineered to get found and turn visitors into booked work.",
  "h1":"Get found.<br>Get booked.<br>Get paid.",
  "lead":"A website should do more than look good. Yours is engineered to rank in search, load in an instant, and turn the people who find you into booked jobs and paying customers.",
  "cards":[("search","Search ranking","Page 1"),("gauge","Load time","0.9s"),("cal","Booking","Confirmed")],
  "stakes_k":"The cost of a slow, invisible site",
  "stakes":'If customers cannot find you or your site makes them wait, they leave and <span class="accent">book with someone who shows up first.</span>',
  "outcomes_head":"A site that earns its place in your pipeline.",
  "outcomes":[
    ("search","Found by the right people","Built around the searches your customers actually type, so you show up when it counts."),
    ("bolt","Fast enough to keep them","Pages that load in under a second, because every slow second sends people away."),
    ("cal","Visitors become bookings","Clear paths to call, book, and buy, so traffic turns into real work on the calendar."),
  ],
  "included":[
    ("Custom design","A site designed for your brand, not a template everyone else is using."),
    ("SEO architecture","Clean structure and content built to rank in local and organic search."),
    ("Service and location pages","Dedicated pages that capture searches across every service and area you cover."),
    ("Booking and lead flows","Simple, obvious paths that turn a visitor into a booked customer."),
    ("Mobile first","Flawless on the phone, where most of your customers actually are."),
    ("Analytics","Clear reporting on what brings in leads, so you know what is working."),
    ("Structured data","Schema that helps search engines and AI understand and surface your business."),
    ("Ongoing updates","We keep it fast, current, and converting long after launch."),
  ],
  "steps":[
    ("We learn your market","We study your customers, your services, and who you are competing against."),
    ("We design and build","A fast, search ready site built to convert, shared with you as it comes together."),
    ("We launch and grow it","It goes live, starts ranking, and we keep improving what brings in work."),
  ],
  "cta_h":"Turn your website into<br>your best salesperson.",
  "cta_p":"Send us your current site or your idea for one. We will show you what we would build and how it would bring in more booked work.",
 },
 {
  "slug":"software","active":"Software","eyebrow":"Custom Software",
  "title":"Custom Software | Rocket Solutions",
  "desc":"Admin dashboards, CRMs, and internal tools built around how your business actually runs.",
  "h1":"Run your whole<br>operation in<br>one place.",
  "lead":"Spreadsheets and a dozen disconnected apps are quietly costing you hours and mistakes. We build the dashboard, CRM, or tool your business actually needs, shaped around how you already work.",
  "cards":[("grid","Dashboard","All systems"),("user","New lead","Assigned"),("bars","This week","On track")],
  "stakes_k":"The cost of scattered tools",
  "stakes":'Every hour spent copying data between apps and chasing spreadsheets is an hour <span class="accent">stolen from actually running your business.</span>',
  "outcomes_head":"One system. Total control. No busywork.",
  "outcomes":[
    ("layers","Everything in one place","Leads, jobs, scheduling, and reporting live together instead of in five different tabs."),
    ("clock","Hours of admin gone","The manual copying, chasing, and double entry simply disappears."),
    ("bars","Decisions you can trust","Clear reporting on the numbers that matter, updated in real time."),
  ],
  "included":[
    ("Admin dashboards","A command center for your business, built around your workflow."),
    ("CRM","Track every lead and customer from first contact to repeat work."),
    ("Scheduling","Jobs, staff, and calendars managed in one clean view."),
    ("Reporting","Live numbers on revenue, leads, and performance, no spreadsheets required."),
    ("Role based access","The right people see the right things, and nothing they should not."),
    ("Integrations","Connected to the tools you already use so nothing falls through the cracks."),
    ("Built for your process","Shaped around how you work, not forcing you into someone else's system."),
    ("Support and upkeep","We maintain and evolve it as your business grows."),
  ],
  "steps":[
    ("We map your workflow","We learn exactly how your business runs today, and where it leaks time."),
    ("We design and build","A tool shaped around your process, shared with you as it takes form."),
    ("We roll it out","We launch it, train your team, and keep improving it over time."),
  ],
  "cta_h":"Replace the spreadsheets<br>with one system.",
  "cta_p":"Tell us how you run things today. We will show you the tool we would build to make it faster, clearer, and easier to grow.",
 },
 {
  "slug":"automation","active":"Automation","eyebrow":"AI Automation",
  "title":"AI Automation | Rocket Solutions",
  "desc":"Content and marketing that research, write, and publish themselves on a schedule, without a hand on the keyboard.",
  "h1":"Marketing that<br>runs while<br>you work.",
  "lead":"Staying visible online is a full time job you do not have time for. We build automated systems that research, write, and publish your content and social on a schedule, so your marketing keeps running while you run the business.",
  "cards":[("pen","New article","Published"),("mega","Social post","Scheduled"),("cycle","Pipeline","Running")],
  "stakes_k":"The cost of going quiet",
  "stakes":'When your marketing stops, so does your pipeline. Staying consistent by hand is <span class="accent">the thing every busy owner drops first.</span>',
  "outcomes_head":"Consistent output, zero overhead.",
  "outcomes":[
    ("cycle","Always publishing","Fresh content and posts go out on schedule, without you lifting a finger."),
    ("clock","No new hires","The work of a content team, handled by a system that runs itself."),
    ("trend","Compounding reach","Steady, search ready content that builds your visibility month after month."),
  ],
  "included":[
    ("Content pipelines","Systems that research, write, and format articles end to end."),
    ("Automated publishing","New content goes live on your site on a set schedule, hands free."),
    ("Social posting","Posts created and scheduled across your channels automatically."),
    ("Performance tracking","The system watches what performs and leans into what works."),
    ("Lead workflows","Follow ups and nurture sequences that run on their own."),
    ("Brand consistency","Everything sounds like you, every time, with no drift."),
    ("Quality control","Automated checks keep the output accurate and on brand before it ships."),
    ("Reporting","Clear visibility into what is going out and how it is doing."),
  ],
  "steps":[
    ("We learn your voice","We capture how your brand sounds and what your customers care about."),
    ("We build the system","We set up the pipelines that research, write, and publish for you."),
    ("It runs on its own","Content ships on schedule while we monitor and tune what performs."),
  ],
  "cta_h":"Put your marketing<br>on autopilot.",
  "cta_p":"Tell us where you want to show up. We will show you the system we would build to keep you visible without the manual work.",
 },
]

def contact_page():
    return HEAD.format(
        title="Contact | Rocket Solutions",
        desc="Tell us what you are trying to fix. We will get back to you within one business day.") + MONOGRAM_DEFS + nav("Contact") + f'''
<main>
  <section class="svc-hero">
    <div class="orb a"></div><div class="orb b"></div>
    <div class="wrap">
      <div class="svc-grid" style="align-items:start">
        <div>
          <span class="eyebrow"><span class="dot"></span> Contact</span>
          <h1>Tell us what<br>you are trying<br>to fix.</h1>
          <p class="lead">Send a few details about your business and what is slowing you down. We will get back to you within one business day with what we would build.</p>
          <div class="cmeta" style="margin-top:8px">
            <div class="row" style="display:flex;flex-direction:column;gap:4px;padding:18px 0;border-top:1px solid var(--line)">
              <span style="font-size:13px;font-weight:600;color:var(--ink-3);text-transform:uppercase;letter-spacing:.08em">Email</span>
              <a href="mailto:hello@gorocketsolutions.com" style="font-size:17px;font-weight:500">hello@gorocketsolutions.com</a></div>
            <div class="row" style="display:flex;flex-direction:column;gap:4px;padding:18px 0;border-top:1px solid var(--line)">
              <span style="font-size:13px;font-weight:600;color:var(--ink-3);text-transform:uppercase;letter-spacing:.08em">Based in</span>
              <span style="font-size:17px;font-weight:500">Georgia, United States</span></div>
            <div class="row" style="display:flex;flex-direction:column;gap:4px;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
              <span style="font-size:13px;font-weight:600;color:var(--ink-3);text-transform:uppercase;letter-spacing:.08em">Response</span>
              <span style="font-size:17px;font-weight:500">Within one business day</span></div>
          </div>
        </div>

        <form class="card" id="contactForm" style="box-shadow:var(--sh-float)">
          <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true" />
          <div class="field-row">
            <div class="field"><label for="name">Name <span class="req">*</span></label><input id="name" name="name" type="text" placeholder="Your name" required /></div>
            <div class="field"><label for="company">Company</label><input id="company" name="company" type="text" placeholder="Business name" /></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" placeholder="you@company.com" required /></div>
            <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" placeholder="(555) 000-0000" /></div>
          </div>
          <div class="field"><label for="interest">What can we help with?</label>
            <select id="interest" name="interest"><option>Voice AI</option><option>Website</option><option>Custom software</option><option>AI automation</option><option>Not sure yet</option></select></div>
          <div class="field"><label for="message">What are you trying to fix? <span class="req">*</span></label>
            <textarea id="message" name="message" placeholder="A sentence or two about your business and what you need." required></textarea></div>
          <button type="submit" class="btn btn-primary" id="submitBtn" style="width:100%;justify-content:center">Send message {ARROW}</button>
          <div class="form-note">No spam and no sales calls. Just a reply.</div>
          <div class="form-status" id="formStatus" role="status"></div>
        </form>
      </div>
    </div>
  </section>
</main>
''' + FOOTER + '''
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
<script src="config.js"></script>
<script src="app.js"></script>
</body>
</html>
'''


import os
outdir = os.path.dirname(os.path.abspath(__file__))
for s in SERVICES:
    with open(os.path.join(outdir, s["slug"] + ".html"), "w") as f:
        f.write(service_page(s))
    print("wrote", s["slug"] + ".html")
with open(os.path.join(outdir, "contact.html"), "w") as f:
    f.write(contact_page())
print("wrote contact.html")
