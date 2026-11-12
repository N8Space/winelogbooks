from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

app = FastAPI(
    title="Nathan Lester | Practical AI Enablement & Solution Architecture",
    description="Portfolio of Nathan Lester: specializing in practical AI enablement, solution architecture, and operational readiness.",
    version="0.3.0",
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

NOVA_PHONE_E164 = "+18886003783"
NOVA_PHONE_DISPLAY = "+1 (888) 600-3783"
CAL_BOOKING_URL = "https://cal.com/nathan-scott-lester/interview-scheduled"
RESUME_PDF_URL = "/static/Nathan-Lester-Resume-20261112.pdf"

KNOWLEDGE_HUB_ICON_SVG = """<div class="case-study-icon case-study-icon--kb" aria-hidden="true">
  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>"""

NEWSGENIE_ICON_SVG = """<div class="case-study-icon case-study-icon--newsgenie" aria-hidden="true">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="48" height="48" aria-hidden="true">
    <defs>
      <radialGradient id="ngBg" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#1E1B4B" stop-opacity="0.95"/>
        <stop offset="100%" stop-color="#0F172A" stop-opacity="0.98"/>
      </radialGradient>
      <linearGradient id="ngNeon" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#06B6D4"/>
        <stop offset="40%" stop-color="#6366F1"/>
        <stop offset="80%" stop-color="#A855F7"/>
        <stop offset="100%" stop-color="#EC4899"/>
      </linearGradient>
      <linearGradient id="ngLamp" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#818CF8"/>
        <stop offset="50%" stop-color="#4F46E5"/>
        <stop offset="100%" stop-color="#312E81"/>
      </linearGradient>
      <filter id="ngGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="2.5" result="b"/>
        <feComposite in="SourceGraphic" in2="b" operator="over"/>
      </filter>
    </defs>
    <circle cx="60" cy="60" r="54" fill="url(#ngBg)" stroke="url(#ngNeon)" stroke-width="2.5" filter="url(#ngGlow)"/>
    <path d="M 60 22 C 70 20, 80 28, 76 38 C 73 47, 60 48, 66 58 C 71 66, 80 68, 70 77 C 62 83, 48 80, 52 68 C 56 57, 44 51, 46 39 C 48 27, 54 22, 60 22 Z" fill="url(#ngNeon)" filter="url(#ngGlow)" opacity="0.95"/>
    <circle cx="60" cy="36" r="3.5" fill="#FFFFFF"/>
    <path d="M 46 94 L 74 94 L 70 89 L 50 89 Z" fill="#312E81" stroke="#818CF8" stroke-width="1.2"/>
    <path d="M 32 75 C 32 68, 42 63, 60 63 C 78 63, 88 68, 88 75 C 88 83, 76 89, 60 89 C 44 89, 32 83, 32 75 Z" fill="url(#ngLamp)" stroke="#A5B4FC" stroke-width="1.8"/>
    <path d="M 38 70 C 22 64, 18 80, 30 84 C 25 79, 28 69, 38 72 Z" fill="url(#ngNeon)" stroke="#6366F1" stroke-width="0.8"/>
    <path d="M 80 72 C 92 68, 102 58, 104 50 C 101 54, 94 60, 84 64 Z" fill="url(#ngNeon)" stroke="#38BDF8" stroke-width="0.8"/>
    <path d="M 88 28 L 90.5 34.5 L 97 37 L 90.5 39.5 L 88 46 L 85.5 39.5 L 79 37 L 85.5 34.5 Z" fill="#F472B6"/>
    <path d="M 28 42 L 30 46.5 L 35 48.5 L 30 50.5 L 28 55 L 26 50.5 L 21 48.5 L 26 46.5 Z" fill="#38BDF8"/>
  </svg>
</div>"""

VOICE_ASSISTANT_ICON_SVG = """<div class="case-study-icon case-study-icon--voice" aria-hidden="true">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="48" height="48" aria-hidden="true">
    <defs>
      <radialGradient id="vaBg" cx="50%" cy="45%" r="55%">
        <stop offset="0%" stop-color="#064E3B" stop-opacity="0.95"/>
        <stop offset="100%" stop-color="#090D16" stop-opacity="0.98"/>
      </radialGradient>
      <linearGradient id="vaRing" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#10B981"/>
        <stop offset="55%" stop-color="#34D399"/>
        <stop offset="100%" stop-color="#FAE2A6"/>
      </linearGradient>
      <linearGradient id="vaGold" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FAE2A6"/>
        <stop offset="100%" stop-color="#E5B869"/>
      </linearGradient>
    </defs>
    <circle cx="60" cy="60" r="54" fill="url(#vaBg)" stroke="url(#vaRing)" stroke-width="2.5"/>
    <circle cx="60" cy="60" r="44" fill="none" stroke="#10B981" stroke-width="1" stroke-dasharray="4 4" opacity="0.45"/>
    <!-- Handset silhouette -->
    <path d="M40 43 C36 47, 36 57, 43 67 C50 77, 60 83, 68 83 C73 83, 78 79, 80 75 L73 69 C71 68, 68 68, 66 70 L63 73 C57 70, 51 64, 48 58 L51 55 C53 53, 53 50, 52 48 L46 41 C44 40, 42 41, 40 43 Z" fill="url(#vaGold)"/>
    <!-- Acoustic AI voice wave bars -->
    <line x1="65" y1="46" x2="65" y2="56" stroke="#34D399" stroke-width="3.2" stroke-linecap="round"/>
    <line x1="73" y1="39" x2="73" y2="60" stroke="#6EE7B7" stroke-width="3.2" stroke-linecap="round"/>
    <line x1="81" y1="34" x2="81" y2="56" stroke="#FAE2A6" stroke-width="3.2" stroke-linecap="round"/>
    <line x1="89" y1="41" x2="89" y2="51" stroke="#34D399" stroke-width="3.2" stroke-linecap="round"/>
    <!-- AI spark star -->
    <path d="M56 26 L58 31 L63 33 L58 35 L56 40 L54 35 L49 33 L54 31 Z" fill="#FAE2A6"/>
  </svg>
</div>"""

CASE_STUDIES = [
    {
        "slug": "intelligent-knowledge-hub",
        "title": "Knowledge Hub Chatbot",
        "category": "Case Study 01 // Enterprise Search & Retrieval",
        "icon_html": KNOWLEDGE_HUB_ICON_SVG,
        "problem": (
            "I saw support teams spending too much time digging through online reference pages just "
            "to answer everyday customer questions. Even after finding the right article, reps still "
            "had to read, interpret, and write a response from scratch—which led to inconsistent "
            "answers. When I ran early chatbot tests, standard context windows couldn't hold the full "
            "library, larger context windows suffered from \"context rot,\" uploaded files quickly fell "
            "out of sync with live articles, and heavy reasoning models were too slow and expensive "
            "for frontline support."
        ),
        "solution": (
            "I built an example for demonstration that is a hybrid search chatbot hosted on Azure App "
            "Service and powered by Azure AI Search (combining keyword and vector search) with a FastAPI "
            "backend. It pulls grounded answers straight from current support documentation I've synthesized "
            "in under a second, enforces role-based access, and checks answer quality automatically. I also "
            "built in live tracking for token usage, cost, and response latency, along with a user feedback "
            "loop that builds golden evaluation sets to validate future updates before they go live."
        ),
        "try_url": "https://intelligent-knowledge-hub-audyhad0ebbhbzc3.southcentralus-01.azurewebsites.net",
        "try_label": "Try Knowledge Hub Chatbot ↗",
        "github_url": "https://github.com/N8Space/intelligent-knowledge-hub",
        "detail_url": None,
    },
    {
        "slug": "newsgenie",
        "title": "News Chatbot with Tools",
        "category": "Case Study 02 // Tool-Using Conversational Agent",
        "icon_html": NEWSGENIE_ICON_SVG,
        "problem": (
            "I built this because standard AI models are frozen in time at their training cutoff. "
            "When you ask them about breaking news or current events, they either admit they don't "
            "know or confidently make things up. On the flip side, traditional news apps force you "
            "to scroll through endless feeds and clickbait just to get a straight answer on what's "
            "happening."
        ),
        "solution": (
            "I designed this assistant to figure out what a user is actually asking and pick the "
            "right tool for the job. If you ask a general question, it answers directly from its own "
            "knowledge. If you want the latest headlines in technology, business, or sports, it pulls "
            "live stories straight from a news feed. And if you ask about a specific event happening "
            "right now, it searches the live web to give you an accurate, up-to-the-minute summary "
            "with source links you can verify."
        ),
        "try_url": "https://newsgenie-lesterlabs.azurewebsites.net",
        "try_label": "Try News Chatbot ↗",
        "github_url": "https://github.com/N8Space/NewsGenie",
        "detail_url": None,
    },
    {
        "slug": "call-agent",
        "title": "AI Voice Assistant",
        "category": "Case Study 03 // Live Voice & Missed-Call Recovery",
        "icon_html": VOICE_ASSISTANT_ICON_SVG,
        "problem": (
            "I built this because I stay busy and didn't want to miss an important call—especially from "
            "a recruiter or hiring manager. It's the same challenge businesses face every day when they "
            "miss calls from high-intent leads. I needed a system that answers immediately 24/7, locks in "
            "a meeting on the spot, and automatically follows up by text if a caller hangs up or gets "
            "disconnected before booking."
        ),
        "solution": (
            "I designed this as a dependable voice assistant that works right out of the box. I can load "
            "it with business details, pricing, and everyday FAQs so callers get clear, helpful answers "
            "in a natural conversation that builds trust right away. When a caller is ready to take the "
            "next step, it checks my live calendar and books the appointment on the spot. My goal was "
            "simple: stop losing prospects and end the game of phone tag."
        ),
        "try_url": f"tel:{NOVA_PHONE_E164}",
        "try_label": None,
        "github_url": None,
        "detail_url": "/projects/call-agent",
    },
]

# Shared "Call Nova" modal, rendered once per layout page and driven by
# /static/voice-agent.js. Uses a native <dialog> for focus handling and Esc.
VOICE_AGENT_MODAL_HTML = f"""
    <dialog id="voice-agent-modal" class="voice-modal" closedby="any" aria-labelledby="voice-modal-title">
      <form method="dialog" class="voice-modal-close-form">
        <button class="voice-modal-close" aria-label="Close voice modal">×</button>
      </form>
      <div class="voice-modal-header">
        <span class="kicker">Live AI Voice Assistant</span>
        <h2 id="voice-modal-title">Call Nova</h2>
        <p class="voice-subtitle">
          <span>Nathan Lester's AI Assistant</span>
          <span class="voice-subtitle-line">Connected to Live Calendar</span>
        </p>
      </div>
      <div class="voice-visualizer-container">
        <div id="voice-orb" class="voice-orb" aria-hidden="true">
          <div class="voice-orb-pulse"></div>
          <div class="voice-orb-icon">📞</div>
        </div>
        <a href="tel:{NOVA_PHONE_E164}" class="modal-phone-number">{NOVA_PHONE_DISPLAY}</a>
        <div id="voice-status" class="voice-status-text">Dial from your phone to speak with Nova and schedule time on Nathan's live calendar.</div>
        <div class="voice-latency-badge"><span class="chip-dot green"></span> Engine: Retell Neural Voice &bull; &lt; 800ms Latency</div>
      </div>
      <div class="voice-modal-actions">
        <a class="btn btn-primary btn-call-phone" href="tel:{NOVA_PHONE_E164}" autofocus><span>Call</span><span class="btn-phone-number">{NOVA_PHONE_DISPLAY}</span></a>
        <button type="button" class="copy-btn phone-btn" onclick="copyPhone(this)">
          <span>📋</span> Copy Number
          <span class="copy-toast">Copied Phone to Clipboard!</span>
        </button>
      </div>
      <div class="voice-modal-fallback">
        <span class="fallback-note">Hang-ups or missed calls automatically receive a follow-up SMS with Nathan's direct calendar link.</span>
      </div>
    </dialog>"""


def render_page(title: str, current_path: str, main_content: str) -> HTMLResponse:
    nav_items = [
        ("/", "Home"),
        ("/projects/call-agent", "AI Voice Assistant"),
    ]
    links = []
    for path, label in nav_items:
        active = ' class="active"' if path == current_path else ""
        links.append(f'<a href="{path}"{active}>{label}</a>')

    canonical_path = current_path if current_path != "/" else ""
    canonical_url = f"https://www.nathanscottlester.com{canonical_path}"

    return HTMLResponse(
        f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Nathan Lester: Specializing in practical AI enablement, solution architecture, and operational readiness. Real-world experience from McDonald's and Scooter's Coffee to regulated insurance." />
    <title>{title} - Nathan Lester</title>
    <link rel="canonical" href="{canonical_url}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:site_name" content="Nathan Lester" />
    <meta property="og:title" content="{title} - Nathan Lester" />
    <meta property="og:description" content="Specializing in practical AI enablement, solution architecture, and operational readiness." />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/style.css" />
  </head>
  <body>
    <header class="site-header">
      <div class="container navbar">
        <a class="brand" href="/">
          <span class="brand-mark">NL</span>
          <div class="brand-title">
            <span class="brand-name">Nathan Lester</span>
            <span class="brand-subtitle">Applied AI</span>
          </div>
        </a>
        <nav class="nav-links" aria-label="Main navigation">
          {''.join(links)}
        </nav>
      </div>
    </header>
    {main_content}
    <footer class="footer">
      <div class="container footer-inner">
        <div><strong>Nathan Lester</strong> • AI Enablement &amp; Innovation Leader Applying AI</div>
        <div>Targeting roles in Chicago • Milwaukee • Indianapolis • Remote • <a href="tel:+18886003783">+1 (888) 600-3783</a> • <a href="mailto:hello@nathanscottlester.com">hello@nathanscottlester.com</a></div>
      </div>
    </footer>
    {VOICE_AGENT_MODAL_HTML}
    <script src="/static/voice-agent.js" defer></script>
  </body>
</html>"""
    )


def render_case_study_placeholders() -> str:
    cards = []
    for item in CASE_STUDIES:
        if item["slug"] == "call-agent":
            action_buttons = (
                f'<a class="btn btn-primary" href="{item["detail_url"]}">View Full Case Study →</a>'
                f'<a class="btn btn-secondary btn-call-phone" href="tel:{NOVA_PHONE_E164}" onclick="if (window.openVoiceAgentModal && !/Mobi|Android|iPhone/i.test(navigator.userAgent)) {{ event.preventDefault(); openVoiceAgentModal(); }}"><span>Call</span><span class="btn-phone-number">{NOVA_PHONE_DISPLAY}</span></a>'
            )
        else:
            github_btn = (
                f'<a class="btn btn-secondary" href="{item["github_url"]}" target="_blank" rel="noopener noreferrer">GitHub Repo ↗</a>'
                if item.get("github_url")
                else ""
            )
            action_buttons = (
                f'<a class="btn btn-primary" href="{item["try_url"]}" target="_blank" rel="noopener noreferrer">{item["try_label"]}</a>'
                f"{github_btn}"
            )

        cards.append(
            f"""
            <article class="case-study-card placeholder-card">
              <header class="case-study-header">
                <div class="case-study-title-group">
                  <span class="category-badge">{item['category']}</span>
                  <h3>{item['title']}</h3>
                </div>
                {item['icon_html']}
              </header>
              <div class="placeholder-topics">
                <div class="topic-block">
                  <h4>The Problem</h4>
                  <p>{item['problem']}</p>
                </div>
                <div class="topic-block">
                  <h4>The Solution</h4>
                  <p>{item['solution']}</p>
                </div>
              </div>
              <footer class="case-study-footer">
                <div class="case-study-actions">
                  {action_buttons}
                </div>
              </footer>
            </article>
            """
        )
    return "\n".join(cards)


@app.get("/", response_class=HTMLResponse)
async def home():
    case_studies_html = render_case_study_placeholders()
    body = f"""
    <main>
      <section class="hero">
        <div class="container hero-grid">
          <div class="story-intro">
            <span class="kicker">Who I Am</span>
            <h1>Connecting Business Strategy &amp; <span class="gradient-text">Practical AI.</span></h1>
            <p>
              My journey with applied AI started early. At <strong>McDonald's</strong>, I tested voice and generative AI in what we called the Voice-Activated Drive-Thru Order Taker. It was an unforgiving proving ground: roaring diesel engines, ambient outdoor noise, regional accents, sub-second latency requirements, and zero room for order errors. That experience taught me a lasting lesson: <em>happy-path demos in a clean boardroom mean nothing; real AI lives and dies in the unproven edge cases.</em>
            </p>
            <p>
              In December 2022, as Innovation Director for <strong>Scooter's Coffee</strong>, I used generative AI and simulation modeling to build operational test tools and an enterprise Innovation Lab. Later, at a <strong>regulated insurance carrier</strong>, I watched the industry hype cycle explode with point solutions that promised magic in sales pitches but fell apart under real compliance rules and fragmented data silos.
            </p>
            <p>
              I have never viewed AI as a tool to replace people. Rather, it is a practical way to eliminate routine drudgery so cross-functional teams can do their best work with greater creativity, purpose, and empathy. Today, everyone can build with AI. The real question is: <strong>What should you build, and how do you design it so teams adopt it safely and reliably?</strong> The best way to answer that is not through slide decks, but by rolling up your sleeves and building working, dependable tools.
            </p>
            <p>
              My focus on <strong>Chicago, IL, Milwaukee, WI, and Indianapolis, IN</strong> (along with remote roles) is personal. My extended family is aging and lives across the Midwest, and being close to them is a priority for my family.
            </p>
          </div>
          <aside class="hero-aside">
            <div class="profile-card">
              <div class="hud-corner top-left"></div>
              <div class="hud-corner top-right"></div>
              <div class="hud-corner bottom-left"></div>
              <div class="hud-corner bottom-right"></div>
              <div class="avatar-box">
                <iframe
                  src="https://www.youtube-nocookie.com/embed/V-cfCoKe1TQ?autoplay=1&mute=1&controls=0&autohide=1&modestbranding=1&enablejsapi=1&cc_load_policy=1&cc_lang_pref=en&playsinline=1&rel=0&loop=1&playlist=V-cfCoKe1TQ"
                  title="Nathan Lester - AI Enablement Leader Applying AI"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  allowfullscreen
                ></iframe>
              </div>
              <p class="profile-summary">Specializing in practical AI enablement, solution architecture, and operational readiness.</p>
              <div class="profile-links">
                <a class="btn btn-primary" href="{RESUME_PDF_URL}" download="Nathan-Lester-Resume.pdf">Download Resume (PDF)</a>
                <a class="btn btn-secondary btn-call-phone" href="tel:{NOVA_PHONE_E164}" onclick="if (window.openVoiceAgentModal && !/Mobi|Android|iPhone/i.test(navigator.userAgent)) {{ event.preventDefault(); openVoiceAgentModal(); }}"><span>Call My AI Assistant</span><span class="btn-phone-number">{NOVA_PHONE_DISPLAY}</span></a>
                <a class="btn btn-secondary" href="mailto:hello@nathanscottlester.com">Email hello@nathanscottlester.com</a>
              </div>
            </div>
          </aside>
        </div>
      </section>

      <section class="section" id="case-studies">
        <div class="container">
          <div class="section-header">
            <div>
              <h2>Case Studies</h2>
              <p>Hands-on projects built to test how AI holds up in real workflows.</p>
            </div>
          </div>
          {case_studies_html}
        </div>
      </section>
    </main>
    """
    return render_page("Practical AI Enablement & Solution Architecture", "/", body)


def render_call_agent_page() -> HTMLResponse:
    body = f"""
    <main>
      <section class="page-hero">
        <div class="container voice-hero-grid">
          <div class="voice-hero-copy">
            <span class="kicker">Case Study // AI Voice Assistant</span>
            <h1>My AI Voice Assistant</h1>
            <p>
              Nova is built to answer inbound phone calls, book live appointments during the call, text back callers if they hang up before scheduling, and answer questions about me on my behalf.
            </p>
            <div class="hero-actions" style="margin-top: 1.5rem;">
              <a class="btn btn-primary btn-call-phone" href="tel:{NOVA_PHONE_E164}" onclick="if (window.openVoiceAgentModal && !/Mobi|Android|iPhone/i.test(navigator.userAgent)) {{ event.preventDefault(); openVoiceAgentModal(); }}"><span>Call</span><span class="btn-phone-number">{NOVA_PHONE_DISPLAY}</span></a>
              <button type="button" class="copy-btn phone-btn btn-call-phone" onclick="copyPhone(this)">
                <span>📋 Copy</span>
                <span class="btn-phone-number">{NOVA_PHONE_DISPLAY}</span>
                <span class="copy-toast">Copied Phone to Clipboard!</span>
              </button>
            </div>
          </div>
          <aside class="voice-hero-visual">
            <div class="nova-portrait-card">
              <div class="hud-corner top-left"></div>
              <div class="hud-corner top-right"></div>
              <div class="hud-corner bottom-left"></div>
              <div class="hud-corner bottom-right"></div>
              <div class="nova-portrait-stage">
                <img
                  src="/static/img/nova-avatar.png"
                  alt="Nova — Nathan Lester's AI Voice Assistant"
                  width="473"
                  height="652"
                  fetchpriority="high"
                  decoding="async"
                />
              </div>
              <div class="nova-portrait-caption">
                <span class="pulse-dot"></span>
                <span><strong>Nova</strong> • 24/7 AI Voice Assistant</span>
              </div>
            </div>
          </aside>
        </div>
      </section>

      <section class="section">
        <div class="container detail-single">
          <article class="article-panel">
            <h2>Project Overview: The Problem &amp; The Solution</h2>
            <p>
              <strong>The Problem:</strong> Voice is an unforgiving interface. If an AI phone assistant pauses for more than a second or two while waiting on a calendar API or a chain of no-code webhooks, callers think the line dropped and hang up. And once a caller hangs up on a traditional voice bot, that missed connection is gone.
            </p>
            <p>
              <strong>The Solution:</strong> I built Nova as a standalone asynchronous Python microservice with zero reliance on third-party automation glues like n8n or Make. To keep the conversation natural while never losing a caller, the service splits every call into two separate pipelines:
            </p>
            <ul class="prose-list">
              <li><strong>Mid-Call Tools (&lt; 500ms budget, 3.5s timeout fallback):</strong> While the caller is speaking with Nova, Retell AI calls HMAC-SHA256 verified endpoints (<code>/api/v1/retell/tools/check-availability</code>, <code>book-appointment</code>, and <code>urgent-escalation</code>). If a calendar lookup ever takes longer than 3.5 seconds, the service returns a graceful spoken fallback instead of leaving the caller in dead air.</li>
              <li><strong>Post-Call Webhook &amp; Missed-Call Recovery (&lt; 50ms ACK):</strong> As soon as a call ends, <code>/api/v1/retell/webhook</code> verifies the signature, returns an immediate <code>200 OK</code> in under 50ms, and hands the rest of the work to FastAPI <code>BackgroundTasks</code>. If the caller hung up without booking, the service automatically sends a follow-up text message with a direct calendar link and logs the call transcript and summary to the database.</li>
            </ul>

            <div class="system-specs-card" role="region" aria-label="System Specifications">
              <div class="system-specs-header">
                <span class="kicker">Operational Profile</span>
                <h2>System Specs</h2>
              </div>
              <ul class="spec-grid">
                <li><span>Voice Engine</span><strong>Retell AI + ElevenLabs</strong></li>
                <li><span>Telephony / SMS</span><strong>Telnyx SIP &amp; Twilio</strong></li>
                <li><span>Toll-Free Line</span><strong><a href="tel:{NOVA_PHONE_E164}">{NOVA_PHONE_DISPLAY}</a></strong></li>
                <li><span>Voice Turnaround</span><strong>&lt; 800ms</strong></li>
                <li><span>Mid-Call Tools</span><strong>&lt; 500ms (3.5s Guard)</strong></li>
                <li><span>Webhook ACK</span><strong>&lt; 50ms (Async Queue)</strong></li>
                <li><span>Runtime</span><strong>FastAPI • Python 3.12+</strong></li>
                <li><span>Deployment</span><strong>Docker + Nginx VPS</strong></li>
              </ul>
            </div>

            <h2>System Architecture Diagram</h2>
            <figure class="arch-image-card">
              <img
                src="/static/img/call-agent-architecture.png"
                alt="System architecture showing Incoming Caller to Retell AI Voice Engine, splitting into Mid-Call Tools under 500ms and Post-Call Webhook under 50ms with FastAPI BackgroundTasks"
                width="1720"
                height="1240"
                loading="lazy"
                decoding="async"
              />
              <figcaption class="arch-figcaption-bar">
                <span>// System Architecture &amp; Dual-Pipeline Data Flow (architecture-diagram.png)</span>
                <a class="btn btn-secondary btn-sm" href="/static/img/call-agent-architecture.png" download="architecture-diagram.png">⬇ Download architecture-diagram.png</a>
              </figcaption>
            </figure>

            <h2>Carrier-Compliant Toll-Free SMS Opt-In Workflow</h2>
            <p>
              Sending automated follow-up texts from a phone number requires passing strict carrier verification. Using Telnyx SIP trunking and a dedicated toll-free number (<strong>{NOVA_PHONE_DISPLAY}</strong>), the same number handles both inbound voice calls and outbound confirmation texts after obtaining verbal opt-in during the call.
            </p>
            <figure class="arch-image-card">
              <img
                src="/static/img/toll-free-opt-in-workflow.jpg"
                alt="Three-step inbound phone call SMS opt-in verification process: Customer calls +1-888-600-3783, AI Voice Assistant requests verbal consent, and a single SMS confirmation is dispatched"
                width="1376"
                height="768"
                loading="lazy"
                decoding="async"
              />
              <figcaption>// Inbound Phone Call SMS Opt-In Verification Process</figcaption>
            </figure>

            <h2>Repository Structure</h2>
            <figure class="code-figure">
              <figcaption id="repo-structure-caption" class="code-figcaption-bar">
                <span>// Project Directory Layout</span>
                <div class="code-scroll-controls">
                  <span class="scroll-hint-badge" aria-hidden="true">↔ Scroll horizontally</span>
                  <button type="button" class="scroll-step-btn" aria-label="Scroll directory layout left" onclick="document.getElementById('repo-structure-pre').scrollBy({{left: -260, behavior: 'smooth'}})">←</button>
                  <button type="button" class="scroll-step-btn" aria-label="Scroll directory layout right" onclick="document.getElementById('repo-structure-pre').scrollBy({{left: 260, behavior: 'smooth'}})">→</button>
                </div>
              </figcaption>
              <div class="code-scroll-wrapper">
                <pre id="repo-structure-pre" class="architecture-diagram scroller-x" role="region" aria-labelledby="repo-structure-caption" tabindex="0"><code>call-agent/
├── Dockerfile                  # Multi-target container (Hostinger VPS, Cloud Run, Azure)
├── docker-compose.yml          # Compose stack with Nginx &amp; Certbot profile
├── requirements.txt            # Python 3.12+ dependencies
├── assets/
│   ├── architecture-diagram.png        # System architecture &amp; dual-pipeline diagram
│   └── toll-free-opt-in-workflow.jpg   # Carrier SMS verbal opt-in workflow diagram
├── docs/
│   ├── architecture_overview.md        # Architecture specs &amp; integration guide
│   ├── TELNYX_SETUP_GUIDE.md           # SIP trunking &amp; toll-free SMS compliance guide
│   ├── RETELL_WORKSPACE_SETUP_GUIDE.md # Workspace &amp; agent setup SOP
│   ├── NEW_CLIENT_ONBOARDING_GUIDE.md  # End-to-end tenant onboarding SOP
│   └── CLIENT_KNOWLEDGE_UPDATE_GUIDE.md
├── nginx/conf.d/call-agent.conf        # Nginx reverse proxy &amp; TLS 1.2/1.3 config
├── scripts/
│   ├── init_nginx_ssl.sh               # One-command SSL bootstrap script
│   └── provision_client.py             # CLI for onboarding tenants &amp; Retell agents
├── tests/test_webhooks.py              # Pytest suite for webhooks, tools, and security
└── app/
    ├── main.py                 # FastAPI app, lifespan handler, and /health probe
    ├── config.py               # pydantic-settings configuration
    ├── database.py             # Async SQLAlchemy 2.0 (aiosqlite &amp; asyncpg)
    ├── models.py               # Tenant and CallLog database models
    ├── schemas.py              # Pydantic v2 request/response schemas
    ├── core/security.py        # Retell HMAC-SHA256 verification &amp; tenant resolver
    ├── services/
    │   ├── calendar.py         # Async availability lookup &amp; appointment booking
    │   └── sms.py              # Telnyx / Twilio confirmations, alerts &amp; recovery
    └── api/
        ├── tools.py            # Mid-call tool endpoints (&lt;500ms budget)
        ├── webhooks.py         # Post-call webhook &amp; BackgroundTasks recovery
        └── admin.py            # Multi-tenant onboarding endpoints</code></pre>
              </div>
            </figure>

            <h2>Try the AI Voice Assistant Live</h2>
            <div class="sandbox-panel">
              <p>
                Nova is connected to my live calendar. Call the toll-free number from your phone to try it out. If you hang up before booking a time, the post-call pipeline will text you a link to my calendar.
              </p>
              <div class="sandbox-actions">
                <a class="btn btn-primary btn-call-phone" href="tel:{NOVA_PHONE_E164}"><span>📞 Call</span><span class="btn-phone-number">{NOVA_PHONE_DISPLAY}</span></a>
                <button type="button" class="copy-btn phone-btn btn-call-phone" onclick="copyPhone(this)">
                  <span>📋 Copy</span>
                  <span class="btn-phone-number">{NOVA_PHONE_DISPLAY}</span>
                  <span class="copy-toast">Copied Phone to Clipboard!</span>
                </button>
              </div>
            </div>

            <div class="back-home-row">
              <a class="btn btn-secondary" href="/#case-studies">← All Case Studies</a>
            </div>
          </article>
        </div>
      </section>
    </main>
    """
    return render_page("My AI Voice Assistant", "/projects/call-agent", body)


@app.get("/projects/call-agent", response_class=HTMLResponse)
@app.get("/projects/ai-voice-assistant", response_class=HTMLResponse)
async def project_call_agent():
    return render_call_agent_page()


@app.get("/health")
async def health_check():
    return {"status": "healthy", "runtime": "Python 3.13"}


@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots_txt():
    content = """User-agent: *
Allow: /

Sitemap: https://www.nathanscottlester.com/sitemap.xml
"""
    return PlainTextResponse(content, media_type="text/plain")


@app.get("/sitemap.xml")
async def sitemap_xml():
    routes = [
        "",
        "/projects/call-agent",
    ]
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for route in routes:
        loc = f"https://www.nathanscottlester.com{route}"
        xml_lines.append(f"  <url><loc>{loc}</loc><changefreq>weekly</changefreq><priority>{'1.0' if route == '' else '0.8'}</priority></url>")
    xml_lines.append("</urlset>")

    return Response(content="\n".join(xml_lines), media_type="application/xml")
