#!/usr/bin/env python3
# Generates the service pages + contact page for Rocket Solutions.
# Rigid, structured, declarative. Shares styles.css + app.js.

ARROW = '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
ARROW_S = '<svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'

MONOGRAM_DEFS = ''

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#F3F1EB" />
<script>document.documentElement.classList.add('js')</script>
<link rel="icon" type="image/png" href="/rocket-solutions-icon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/styles.css" />
<style>
  .svc-hero {{ padding: clamp(48px,6vw,84px) 0 0; }}
  .svc-hero .label {{ display:block; margin-bottom: clamp(24px,3vw,36px); }}
  .svc-hero h1 {{ max-width: 15em; margin-bottom: clamp(24px,3vw,36px); }}
  .svc-hero .lead {{ max-width: 40em; padding-bottom: clamp(36px,4vw,52px); }}
  .contact-grid {{ display:grid; grid-template-columns: 0.8fr 1.2fr; gap: clamp(32px,5vw,72px); align-items:start; }}
  .cmeta {{ border-top:1px solid var(--line-strong); }}
  .cmeta .row {{ display:flex; flex-direction:column; gap:5px; padding:18px 0; border-bottom:1px solid var(--line); }}
  .cmeta .row .k {{ font-family:var(--display); font-size:12px; font-weight:500; letter-spacing:0.1em; text-transform:uppercase; color:var(--ink-3); }}
  .cmeta .row .v {{ font-size:16px; }}
  .cmeta .row a.v:hover {{ color:var(--red); }}
  form.rs-form {{ border:1px solid var(--line-strong); border-radius:var(--radius); padding: clamp(24px,3vw,40px); background:var(--panel); }}
  @media (max-width: 900px) {{ .contact-grid {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
'''

def nav(active):
    items = [("Voice AI","/voice-ai"),("Websites","/websites"),
             ("Software","/software"),("Automation","/automation"),("Contact","/contact")]
    links = "".join(f'<a class="item{" active" if a==active else ""}" href="{h}">{a}</a>' for a,h in items)
    return f'''<header class="nav" id="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/" aria-label="Rocket Solutions home">
      <img class="brand-logo" src="/rocket-solutions-lockup.png" alt="Rocket Solutions" />
    </a>
    <nav class="nav-menu" id="navMenu">{links}</nav>
    <div class="nav-right">
      <a class="nav-cta" href="/contact">Get In Touch</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Menu" aria-expanded="false">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>
      </button>
    </div>
  </div>
</header>'''

FOOTER = '''<footer class="site">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <a class="brand" href="/"><img class="brand-logo" src="/rocket-solutions-lockup-invert.png" alt="Rocket Solutions" /></a>
        <p>A technology firm building the voice systems, websites, software, and automation that businesses run on.</p>
      </div>
      <div class="foot-col"><div class="h">The Work</div>
        <a href="/voice-ai">Voice AI</a><a href="/websites">Websites</a><a href="/software">Custom Software</a><a href="/automation">AI Automation</a></div>
      <div class="foot-col"><div class="h">Firm</div>
        <a href="/">Home</a><a href="/contact">Contact</a><a href="mailto:hello@gorocketsolutions.com">Email</a></div>
      <div class="foot-col"><div class="h">Office</div>
        <a href="#">Atlanta, GA</a><a href="mailto:hello@gorocketsolutions.com">hello@gorocketsolutions.com</a></div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 Rocket Solutions LLC</span>
      <span>Atlanta, GA</span>
    </div>
  </div>
</footer>'''

CONTACT_BAND = f'''  <section class="section band-dark">
    <div class="wrap">
      <div class="reveal" style="max-width:22em">
        <span class="label"><span class="n" style="color:var(--red)">*</span> Contact</span>
        <h2 class="h2" style="margin:20px 0 20px">Tell Us What You Are Working On.</h2>
        <p class="lead" style="margin-bottom:32px">Send a few details about the business and what needs building. You will hear back within one business day.</p>
        <a class="btn btn-invert" href="/contact">Get In Touch {ARROW}</a>
      </div>
    </div>
  </section>'''

def service_page(s):
    cols = "\n        ".join(
        f'<div class="col reveal"><div class="c-n">{ln}</div><h4>{t}</h4><p>{d}</p></div>'
        for ln,t,d in s["outcomes"])
    spec = "\n        ".join(
        f'<div class="spec-item"><span class="s-n">{i+1:02d}</span><h5>{t}</h5><p>{d}</p></div>'
        for i,(t,d) in enumerate(s["included"]))
    proc = "\n        ".join(
        f'<div class="process-row reveal"><span class="p-n">{i+1:02d}</span><h4>{t}</h4><p>{d}</p></div>'
        for i,(t,d) in enumerate(s["steps"]))
    mast = "\n      ".join(
        f'<div class="m-cell"><b>{k}</b> {v}</div>' for k,v in s["mast"])

    return HEAD.format(title=s["title"], desc=s["desc"]) + MONOGRAM_DEFS + nav(s["active"]) + f'''
<main>
  <section class="svc-hero">
    <div class="wrap">
      <span class="label"><span class="n">{s["num"]}</span> {s["eyebrow"]}</span>
      <h1 class="h1">{s["h1"]}</h1>
      <p class="lead">{s["lead"]}</p>
    </div>
    <div class="wrap"><div class="masthead">
      {mast}
    </div></div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal"><span class="label"><span class="n">A</span> What It Does</span>
        <h2 class="h2">{s["outcomes_head"]}</h2></div>
      <div class="cols">
        {cols}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal"><span class="label"><span class="n">B</span> What Is Included</span>
        <h2 class="h2">Everything In The Build.</h2></div>
      <div class="spec">
        {spec}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal"><span class="label"><span class="n">C</span> Method</span>
        <h2 class="h2">How It Gets Built.</h2></div>
      <div class="process">
        {proc}
      </div>
    </div>
  </section>

{CONTACT_BAND}
</main>
''' + FOOTER + '\n<script src="/app.js"></script>\n</body>\n</html>\n'


SERVICES = [
 {
  "slug":"voice-ai","active":"Voice AI","eyebrow":"Voice AI","num":"01",
  "title":"Voice AI | Rocket Solutions",
  "desc":"AI phone systems that answer, qualify, and book every call in a natural voice, around the clock.",
  "h1":"AI Phone Systems That Answer And Book Every Call.",
  "lead":"We build always on voice agents that pick up every call, answer the questions, book the appointment, and pass the details along. Overflow, after hours, and the calls a team cannot get to are covered.",
  "mast":[("What It Is","Voice Agent"),("Runs","24 / 7"),("Handles","Answer, Book, Route")],
  "outcomes_head":"Every Call Answered. Every Lead Kept.",
  "outcomes":[
    ("A / Coverage","Never A Missed Call","Every call is picked up in seconds, day or night, so no opportunity ends in voicemail."),
    ("B / Booking","A Calendar That Fills","Callers are booked on the spot, with confirmations and reminders handled automatically."),
    ("C / Time","Off The Phones","The team stops chasing the phone and focuses on the work that gets paid."),
  ],
  "included":[
    ("Around The Clock Answering","Every call picked up in seconds, including nights, weekends, and holidays."),
    ("Appointment Booking","Callers booked straight onto the calendar with automatic confirmations."),
    ("Call Routing","The right call reaches the right place based on set rules."),
    ("Live Transfer","Hot leads and urgent calls handed to the team in real time."),
    ("Spam Screening","Robocalls and time wasters filtered out before they reach anyone."),
    ("Caller Recognition","Returning customers greeted by name with their history on hand."),
    ("Text Summaries","Every call arrives as a clean, readable summary."),
    ("Matched Voice","It sounds like the brand and answers the way the business would."),
  ],
  "steps":[
    ("Learn The Business","Hours, services, pricing, and how calls should be handled are mapped."),
    ("Build And Train","A voice agent is shaped to sound right and answer every question cold."),
    ("Go Live","Calls get answered, work gets booked, and details land on the phone."),
  ],
 },
 {
  "slug":"websites","active":"Websites","eyebrow":"Websites","num":"02",
  "title":"Websites | Rocket Solutions",
  "desc":"Websites engineered to be found in search and built to turn visitors into booked work.",
  "h1":"Websites Built To Be Found And To Convert.",
  "lead":"We build fast, search ready websites that rank for what customers actually search, load in an instant, and turn the people who arrive into booked jobs.",
  "mast":[("What It Is","Website"),("Built For","Search & Booking"),("Load","Under 1s")],
  "outcomes_head":"Found In Search. Built To Book.",
  "outcomes":[
    ("A / Reach","Found By The Right People","Built around the searches customers type, so the business shows up when it counts."),
    ("B / Speed","Fast Enough To Keep Them","Pages that load in under a second, because every slow second sends people away."),
    ("C / Conversion","Visitors Become Bookings","Clear paths to call, book, and buy, so traffic turns into work on the calendar."),
  ],
  "included":[
    ("Custom Design","A site designed for the brand, not a template everyone else uses."),
    ("SEO Architecture","Clean structure and content built to rank in local and organic search."),
    ("Service & Location Pages","Dedicated pages that capture searches across every service and area."),
    ("Booking & Lead Flows","Simple, obvious paths that turn a visitor into a booked customer."),
    ("Mobile First","Flawless on the phone, where most customers actually are."),
    ("Analytics","Clear reporting on what brings in leads."),
    ("Structured Data","Schema that helps search engines and AI surface the business."),
    ("Ongoing Updates","Kept fast, current, and converting long after launch."),
  ],
  "steps":[
    ("Learn The Market","The customers, the services, and the competition are studied first."),
    ("Design And Build","A fast, search ready site is built to convert, shared as it comes together."),
    ("Launch And Grow","It goes live, starts ranking, and keeps improving what brings in work."),
  ],
 },
 {
  "slug":"software","active":"Software","eyebrow":"Custom Software","num":"03",
  "title":"Custom Software | Rocket Solutions",
  "desc":"Dashboards, CRMs, and internal tools that run the daily operations of a business in one place.",
  "h1":"Software That Runs The Whole Operation In One Place.",
  "lead":"We build the dashboard, CRM, or internal tool a business actually needs, shaped around how it already works, so spreadsheets and disconnected apps stop costing time and mistakes.",
  "mast":[("What It Is","Internal Tools"),("Replaces","Spreadsheets & Apps"),("Shaped To","Your Workflow")],
  "outcomes_head":"One System. Total Control. No Busywork.",
  "outcomes":[
    ("A / One Place","Everything Together","Leads, jobs, scheduling, and reporting live in one system instead of five tabs."),
    ("B / Time","Admin Gone","The manual copying, chasing, and double entry simply disappears."),
    ("C / Clarity","Numbers You Trust","Clear reporting on what matters, updated in real time."),
  ],
  "included":[
    ("Admin Dashboards","A command center for the business, built around its workflow."),
    ("CRM","Every lead and customer tracked from first contact to repeat work."),
    ("Scheduling","Jobs, staff, and calendars managed in one clean view."),
    ("Reporting","Live numbers on revenue, leads, and performance."),
    ("Role Based Access","The right people see the right things, and nothing they should not."),
    ("Integrations","Connected to the tools already in use."),
    ("Built To Fit","Shaped around the existing process, not forced into someone else's."),
    ("Support & Upkeep","Maintained and evolved as the business grows."),
  ],
  "steps":[
    ("Map The Workflow","How the business runs today, and where it leaks time, is documented."),
    ("Design And Build","A tool is shaped around the process and shared as it takes form."),
    ("Roll Out","It launches, the team is trained, and it keeps improving over time."),
  ],
 },
 {
  "slug":"automation","active":"Automation","eyebrow":"AI Automation","num":"04",
  "title":"AI Automation | Rocket Solutions",
  "desc":"Content and marketing systems that research, write, and publish on their own, on schedule.",
  "h1":"Marketing Systems That Run On Their Own.",
  "lead":"We build automated pipelines that research, write, and publish content and social on a schedule, so the marketing keeps running while the business runs itself.",
  "mast":[("What It Is","Automation"),("Runs","On Schedule"),("Output","Content & Social")],
  "outcomes_head":"Consistent Output. Zero Overhead.",
  "outcomes":[
    ("A / Consistency","Always Publishing","Fresh content and posts go out on schedule, with no hand on the keyboard."),
    ("B / Cost","No New Hires","The work of a content team, handled by a system that runs itself."),
    ("C / Reach","Compounding Visibility","Steady, search ready output that builds presence month after month."),
  ],
  "included":[
    ("Content Pipelines","Systems that research, write, and format articles end to end."),
    ("Automated Publishing","New content goes live on a set schedule, hands free."),
    ("Social Posting","Posts created and scheduled across channels automatically."),
    ("Performance Tracking","The system watches what performs and leans into it."),
    ("Lead Workflows","Follow ups and nurture sequences that run on their own."),
    ("Brand Consistency","Everything sounds like the business, every time."),
    ("Quality Control","Automated checks keep output accurate and on brand before it ships."),
    ("Reporting","Clear visibility into what is going out and how it performs."),
  ],
  "steps":[
    ("Learn The Voice","How the brand sounds and what its customers care about is captured."),
    ("Build The System","The pipelines that research, write, and publish are set up."),
    ("Run It","Content ships on schedule while performance is monitored and tuned."),
  ],
 },
]

def contact_page():
    return HEAD.format(
        title="Contact | Rocket Solutions",
        desc="Tell us what you are working on. We reply within one business day.") + MONOGRAM_DEFS + nav("Contact") + f'''
<main>
  <section class="svc-hero" style="padding-bottom:clamp(56px,7vw,96px)">
    <div class="wrap">
      <span class="label"><span class="n">06</span> Contact</span>
      <h1 class="h1">Tell Us What You Are Working On.</h1>
      <p class="lead" style="padding-bottom:clamp(40px,5vw,60px)">Send a few details about the business and what needs building. You will hear back within one business day. No sales calls.</p>
      <div class="contact-grid">
        <div class="reveal">
          <div class="cmeta">
            <div class="row"><span class="k">Email</span><a class="v" href="mailto:hello@gorocketsolutions.com">hello@gorocketsolutions.com</a></div>
            <div class="row"><span class="k">Office</span><span class="v">Atlanta, GA</span></div>
            <div class="row"><span class="k">Response</span><span class="v">Within One Business Day</span></div>
            <div class="row"><span class="k">Delivery</span><span class="v">Nationwide</span></div>
          </div>
        </div>
        <form class="rs-form reveal" id="contactForm">
          <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true" />
          <div class="field-row">
            <div class="field"><label for="name">Name <span class="req">*</span></label><input id="name" name="name" type="text" placeholder="Your name" required /></div>
            <div class="field"><label for="company">Company</label><input id="company" name="company" type="text" placeholder="Business name" /></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" placeholder="you@company.com" required /></div>
            <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" placeholder="(555) 000-0000" /></div>
          </div>
          <div class="field"><label for="interest">The Work</label>
            <select id="interest" name="interest"><option>Voice AI</option><option>Website</option><option>Custom Software</option><option>AI Automation</option><option>Not Sure Yet</option></select></div>
          <div class="field"><label for="message">What Needs Building <span class="req">*</span></label>
            <textarea id="message" name="message" placeholder="A sentence or two about the business and what you need." required></textarea></div>
          <button type="submit" class="btn" id="submitBtn" style="width:100%;justify-content:center">Send Message {ARROW}</button>
          <div class="form-note">No spam and no sales calls. Just a reply.</div>
          <div class="form-status" id="formStatus" role="status"></div>
        </form>
      </div>
    </div>
  </section>
</main>
''' + FOOTER + '''
<script src="/app.js"></script>
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