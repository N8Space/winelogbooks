from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"
AI_SDLC_STUDIO_FILE = TEMPLATES_DIR / "ai_sdlc_studio.html"
AI_SDLC_STUDIO_HTML = AI_SDLC_STUDIO_FILE.read_text(encoding="utf-8") if AI_SDLC_STUDIO_FILE.exists() else ""
AI_ENGINEER_BLUEPRINT_FILE = TEMPLATES_DIR / "ai_engineer_blueprint.html"
AI_ENGINEER_BLUEPRINT_HTML = AI_ENGINEER_BLUEPRINT_FILE.read_text(encoding="utf-8") if AI_ENGINEER_BLUEPRINT_FILE.exists() else ""

app = FastAPI(
    title="Nathan Lester | AI Enablement & Innovation Leader Applying AI",
    description="Portfolio showcasing practical AI enablement, solution architecture, and governance in enterprise environments.",
    version="0.2.0",
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

CERTIFICATIONS = [
    {
        "name": "AI-103",
        "description": "Designing and implementing Microsoft Azure AI solutions",
        "status": "Target: Oct 2026",
    },
    {
        "name": "AZ-104",
        "description": "Microsoft Azure Administrator certification path",
        "status": "Target: Dec 2026",
    },
    {
        "name": "Azure AI Foundry & FinOps",
        "description": "Responsible AI, prompt engineering, and enterprise cloud governance",
        "status": "Applied learning",
    },
]

PROJECTS = [
    {
        "slug": "intelligent-knowledge-hub",
        "title": "Enterprise Knowledge Hub: Intelligent Search & Retrieval",
        "category": "Enterprise Search & Knowledge Management",
        "summary": "A secure hybrid retrieval system built on Azure AI Search. Helps support and operations teams find verified answers in seconds without manual document searching or ungrounded responses.",
        "outcome": "Delivered sub-second retrieval (<850ms), eliminated manual documentation desynchronization, enforced role-based data isolation, and lowered query compute costs by ~65%.",
        "stack": [
            "Azure AI Search",
            "Vector Embeddings",
            "FastAPI & Python",
            "Hybrid BM25 + Vector",
            "Continuous Evaluation",
            "Entra ID & RBAC",
        ],
        "story": "We tested an internal customer service chatbot using a ChatGPT Custom GPT and quickly encountered typical enterprise obstacles: the context window could not hold our full documentation library, manual files frequently desynchronized from living articles, and high-reasoning models increased latency and token spend. We solved this by architecting a production Azure AI Search hybrid knowledge hub with automated accuracy benchmarking and role-based access control.",
        "github_url": "https://github.com/N8Space/intelligent-knowledge-hub",
        "demo_url": "https://intelligent-knowledge-hub-audyhad0ebbhbzc3.southcentralus-01.azurewebsites.net",
        "is_featured": True,
    },
    {
        "slug": "ai-sdlc-studio",
        "title": "Semi-Autonomous Agent Factory & Harness",
        "category": "Semi-Autonomous Agent Factory & Software Testing",
        "summary": "A semi-autonomous development factory that helps teams take AI prototypes to production readiness. Combines test-driven validation, cost controls, and responsive UI verification.",
        "outcome": "Shipped the 'RegPulse' regulatory monitoring tool with 100% automated test pass rate, Grade A+ accessibility, and fast-path cost controls.",
        "stack": [
            "Multi-Agent Systems",
            "ChromaDB Vector Store",
            "Self-Healing TDD",
            "FastAPI & SQLite WAL",
            "Enterprise Webhook Gates",
        ],
        "story": "Generative AI is an outstanding partner for rapidly turning business ideas into interactive prototypes. However, moving from prototype to reliable software requires repeatable engineering discipline: codifying lessons into an automated test harness, enforcing cost fast-paths via DOM sanitization and SHA-256 fingerprinting, preserving memory with ChromaDB, and including human-in-the-loop approval gates.",
        "github_url": "https://github.com/N8Space",
        "demo_url": None,
        "is_featured": True,
    },
    {
        "slug": "resume-refine",
        "title": "Resume Refine: AI-Powered Career Assistant (Mobile iOS)",
        "category": "Mobile Product & Cloud AI Integration",
        "summary": "A consumer-grade native iOS application that empowers job seekers to analyze, polish, and tailor their resumes in real time using Google Gemini and FastAPI cloud services.",
        "outcome": "Delivered an intuitive, responsive mobile experience with sub-second perceived response time, resilient prompt guardrails, and robust offline state handling.",
        "stack": [
            "SwiftUI / iOS",
            "Google Gemini",
            "FastAPI & Python",
            "Automated Workflows",
            "API Gateway",
        ],
        "story": "Building a commercial mobile application provided hands-on experience solving real user ergonomics: network latency, prompt resilience, structured JSON validation, and tactile mobile interactions. The client connects a SwiftUI interface through an API Gateway to a FastAPI/Python backend worker and Google Gemini with schema validation.",
        "github_url": "https://github.com/N8Space",
        "demo_url": None,
        "is_featured": True,
    },
    {
        "slug": "ai-engineer-blueprint",
        "title": "The AI Decision Blueprint: Architecture & Deployment Guide",
        "category": "Solution Design & Decision Framework",
        "summary": "A pragmatic decision framework that helps teams choose the right AI approach (from direct prompting to single agents and cloud services) without over-engineering or unnecessary cost.",
        "outcome": "Codified practical architectural decision logic into an interactive reference, preventing over-engineering and token waste while establishing clean software engineering standards.",
        "stack": [
            "Systems Architecture",
            "Decision Frameworks",
            "Two-Stage Evaluation",
            "Engineering Guidelines",
            "FastAPI & Uvicorn",
        ],
        "story": "Enterprise AI initiatives frequently fall into the over-engineering trap: deploying complex multi-agent swarms for simple tasks or overpaying for cloud infrastructure when simpler alternatives work better. I developed a structured two-stage framework evaluating task complexity, determinism, data sovereignty, and operational boundaries.",
        "github_url": "https://github.com/N8Space",
        "demo_url": None,
        "is_featured": False,
    },
    {
        "slug": "newsgenie",
        "title": "NewsGenie: Multi-Tool Real-Time News & Research Agent",
        "category": "Agentic AI + LangGraph",
        "summary": "An intelligent conversational agent built with LangGraph and Google Gemini that routes dynamically between real-time headlines (NewsAPI) and live search (Tavily).",
        "outcome": "Demonstrated production agentic patterns (cyclical tool routing, state management, fallback recovery) and delivered an interactive Streamlit UI for live queries.",
        "stack": ["LangGraph", "LangChain", "Google Gemini", "NewsAPI", "Tavily Search", "Streamlit", "Azure App Service"],
        "story": "NewsGenie addresses LLM knowledge cutoff limitations through graph-based multi-tool routing. The system analyzes user intent to either answer from training data, query categorized news headlines via NewsAPI, or perform live web research via Tavily with structured error handling.",
        "github_url": "https://github.com/N8Space/NewsGenie",
        "demo_url": "https://newsgenie-lesterlabs.azurewebsites.net",
    },
    {
        "slug": "azure-governance-dashboard",
        "title": "AI Governance & Security Dashboard",
        "category": "Cloud Governance",
        "summary": "A governance dashboard that connects model usage, cost controls, security posture, and operational guardrails for AI-driven teams.",
        "outcome": "Creates a clear operating model for scale-up AI adoption with policy oversight and business-friendly reporting.",
        "stack": ["Azure Monitor", "Cost Management", "Entra ID", "Policy", "Dashboards"],
        "story": "This work frames AI enablement as a platform capability, showing how to align technical delivery with compliance, cost visibility, and adoption metrics.",
        "github_url": None,
        "demo_url": None,
    },
]

STATS = [
    ("3", "Midwest anchor hubs (CHI • MKE • IND)"),
]


def render_page(title: str, current_path: str, main_content: str) -> HTMLResponse:
    nav_items = [
        ("/", "Home"),
        ("/projects", "Case Studies"),
        ("/about", "Executive Story"),
        ("/docs", "API Docs"),
    ]
    links = []
    for path, label in nav_items:
        active = ' class="active"' if path == current_path else ""
        target = ' target="_blank"' if path == "/docs" else ""
        links.append(f'<a href="{path}"{active}{target}>{label}</a>')

    canonical_path = current_path if current_path != "/" else ""
    canonical_url = f"https://www.nathanscottlester.com{canonical_path}"

    return HTMLResponse(
        f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Portfolio of Nathan Lester: AI Enablement &amp; Innovation Leader Applying AI. Proven track record from McDonald's and Scooter's Coffee to regulated insurance environments." />
    <title>{title} - Nathan Lester | AI Enablement &amp; Innovation Leader Applying AI</title>
    <link rel="canonical" href="{canonical_url}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:site_name" content="Nathan Lester | AI Enablement &amp; Innovation Leader Applying AI" />
    <meta property="og:title" content="{title} - Nathan Lester | AI Enablement &amp; Innovation Leader Applying AI" />
    <meta property="og:description" content="Portfolio of Nathan Lester: AI Enablement &amp; Innovation Leader Applying AI. Proven track record from McDonald's and Scooter's Coffee to regulated insurance environments." />
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
        <div>Targeting roles in Chicago • Milwaukee • Indianapolis • Remote • <a href="mailto:hello@nathanscottlester.com">hello@nathanscottlester.com</a></div>
      </div>
    </footer>
    <script>
      function copyEmail(btn) {{
        navigator.clipboard.writeText("hello@nathanscottlester.com").then(function() {{
          var toast = btn.querySelector(".copy-toast");
          if (toast) {{
            toast.classList.add("visible");
            setTimeout(function() {{ toast.classList.remove("visible"); }}, 2200);
          }}
        }});
      }}
    </script>
  </body>
</html>"""
    )


def render_project_cards(project_list):
    cards = []
    for project in project_list:
        featured_cls = " featured-project" if project.get("is_featured") else ""
        stack_items = ''.join(f'<li>{item}</li>' for item in project["stack"])
        cards.append(
            f"""
            <article class="project-card{featured_cls}">
              <div>
                <span class="tag">{project['category']}</span>
                <h3>{project['title']}</h3>
                <p>{project['summary']}</p>
              </div>
              <div>
                <ul>{stack_items}</ul>
                <div class="card-action">
                  <a href="/projects/{project['slug']}">View Case Study →</a>
                </div>
              </div>
            </article>
            """
        )
    return '\n'.join(cards)


@app.get("/", response_class=HTMLResponse)
async def home():
    body = f"""
    <main>
      <!-- =================================================================
           SECTION 1: HERO SECTION - HOOK & PRACTICAL ENABLEMENT
           ================================================================= -->
      <section class="hero">
        <div class="container hero-grid">
          <div>
            <span class="kicker">AI Enablement &amp; Innovation Leader Applying AI</span>
            <h1>Turning Enterprise Strategy into <span class="gradient-text">Practical AI Solutions.</span></h1>
            <p>
              Innovation and enablement leader with hands-on technical execution. From testing early voice AI in McDonald's drive-thrus and building IoT simulations at Scooter's Coffee, to architecting secure search systems at a regulated insurance carrier - I focus on what works. I partner with cross-functional teams to design practical roadmaps, establish responsible governance, and build production tools that eliminate routine drudgery and deliver measurable business value.
            </p>
            <div class="proof-chips">
              <span class="proof-chip highlight"><span class="chip-dot green"></span>Targeting Roles in Chicago • Milwaukee • Indianapolis • Remote</span>
            </div>
            <div class="hero-actions">
              <a class="btn btn-primary" href="#case-studies">Explore Practical Case Studies ↓</a>
              <a class="btn btn-secondary" href="/static/Nathan_Lester_Executive_Resume.pdf" target="_blank" rel="noopener noreferrer">Download Resume (PDF)</a>
            </div>
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
              <h3>Nathan Lester</h3>
              <div class="profile-role">AI Enablement &amp; Innovation Leader Applying AI</div>
              <p>Specializing in practical AI enablement, solution architecture, operational readiness, and cloud governance across enterprise environments.</p>
            </div>
          </aside>
        </div>
      </section>

      <!-- =================================================================
           SECTION 2: THE DIFFERENTIATOR GRID - WHY HANDS-ON ENABLEMENT MATTERS
           ================================================================= -->
      <section class="section" style="padding-top: 2rem;">
        <div class="container">
          <div class="quote-banner">
            <blockquote>"Everyone can build with AI today. The real question is: What should you build, and how do you design it so teams adopt it safely and reliably?"</blockquote>
            <span class="quote-author">Nathan Lester - AI Enablement &amp; Innovation Perspective</span>
          </div>
          <div class="section-header">
            <div>
              <h2>Why Hands-On AI Enablement Matters</h2>
              <p>Slide decks that never become working software create cynicism. Point tools built without understanding business workflows create confusion. An enablement leader who builds connects both worlds.</p>
            </div>
          </div>
          <div class="differentiator-grid">
            <article class="differentiator-card">
              <div>
                <span class="pillar-num">01 // Purpose &amp; Value</span>
                <h3>Human-Centered Enablement &amp; Business Value</h3>
                <p class="pillar-philosophy">
                  AI is never about replacing human purpose. It is about eliminating routine drudgery so cross-functional teams can unlock creativity, empathy, and higher-order problem solving.
                </p>
              </div>
              <div class="contrast-block">
                <span class="label-bad">Why Point Tools Stall</span>
                <p>They build clever point solutions in isolation without understanding change management, employee adoption curves, or practical workflow integration.</p>
                <span class="label-good">The Enablement Leader Value</span>
                <p class="highlight-solution">Translates business priorities into pragmatic, shippable solutions with clear ROI, user enablement, and responsible adoption.</p>
              </div>
            </article>

            <article class="differentiator-card">
              <div>
                <span class="pillar-num">02 // Practical Engineering</span>
                <h3>Production Reality &amp; The Edge-Case Test</h3>
                <p class="pillar-philosophy">
                  Happy-path demos are easy. Real enterprise AI lives and dies in the unproven edge cases - whether dealing with roaring diesel engines in a McDonald's drive-thru or complex policy rules at a regulated insurance carrier.
                </p>
              </div>
              <div class="contrast-block">
                <span class="label-bad">Why Pure Strategists Fall Short</span>
                <p>They rely on vendor pitch decks and black-box tools that choke when context windows overflow, token budgets spike, or APIs fail.</p>
                <span class="label-good">The Enablement Leader Value</span>
                <p class="highlight-solution">Hands-on design of hybrid search, deterministic cost controls, containerized FastAPI services, and self-healing test harnesses.</p>
              </div>
            </article>

            <article class="differentiator-card">
              <div>
                <span class="pillar-num">03 // Governance &amp; Cost Control</span>
                <h3>Responsible Governance &amp; Cloud Discipline</h3>
                <p class="pillar-philosophy">
                  Innovation without guardrails is an operational liability. Battle-tested across high-trust, regulated environments such as insurance and financial services.
                </p>
              </div>
              <div class="contrast-block">
                <span class="label-bad">The Risk of Unguarded AI</span>
                <p>Uncontrolled experiments trigger confidential data exposure, hallucination issues, compliance gaps, and runaway cloud invoices.</p>
                <span class="label-good">The Enablement Leader Value</span>
                <p class="highlight-solution">Embeds role-based access control, data isolation, continuous quality evaluation, and practical token cost caps from Day 1.</p>
              </div>
            </article>
          </div>
        </div>
      </section>

      <!-- =================================================================
           SECTION 3: FEATURED CASE STUDIES - FROM PROTOTYPE TO PRODUCTION
           ================================================================= -->
      <section class="section" id="case-studies">
        <div class="container">
          <div class="section-header">
            <div>
              <h2>Featured Case Studies: From Prototype to Production</h2>
              <p>Practical implementations engineered to solve real organizational friction and deliver reliable business value.</p>
            </div>
          </div>

          <!-- Case Study 1: Enterprise Knowledge Hub -->
          <article class="case-study-card featured-project">
            <div class="case-study-header">
              <div>
                <span class="category-badge">Enterprise Search &amp; Knowledge Management</span>
                <h3>Case Study 1: Enterprise Knowledge Hub: Intelligent Search &amp; Retrieval</h3>
              </div>
              <a class="btn btn-primary" href="/projects/intelligent-knowledge-hub">View Case Study →</a>
            </div>
            <div class="case-story-grid">
              <div class="story-narrative">
                <h4>// The Organizational Friction</h4>
                <p>
                  Support and operations teams struggled with manual documentation searches across fragmented knowledge bases. Early chatbot tests revealed that context windows could not hold all documentation, and standalone files frequently desynchronized from live knowledge bases.
                </p>
                <div class="real-obstacle">
                  <strong>The Trade-Off Trap:</strong> High-reasoning models increased accuracy but resulted in slow response times and rapid token consumption that hit budget caps.
                </div>
                <h4>// The Practical Solution</h4>
                <p>
                  Architected a secure hybrid retrieval pipeline using <strong>Azure AI Search</strong> (vector embeddings + BM25 keyword matching) with a high-throughput <strong>FastAPI</strong> microservice. Implemented role-based document access and automated evaluation benchmarking to ensure consistent, accurate responses.
                </p>
              </div>
              <div class="architecture-box">
                <h4>// Applied Architecture Pipeline</h4>
                <div class="arch-pipeline">
                  <div class="arch-flow-diagram">
                    <div class="arch-node">
                      <span class="node-title">Living Documentation Sources</span>
                      <span class="node-tech">SharePoint / PDFs / APIs</span>
                    </div>
                    <div class="arch-connector">▼ Hybrid Chunking &amp; Ingestion</div>
                    <div class="arch-node">
                      <span class="node-title">Azure AI Search Hybrid Engine</span>
                      <span class="node-tech">Vector + BM25 + RBAC</span>
                    </div>
                    <div class="arch-connector">▼ Semantic Reranking &amp; Filtering</div>
                    <div class="arch-node">
                      <span class="node-title">FastAPI Service + Guardrails</span>
                      <span class="node-tech">Grounding &amp; Quality Checks</span>
                    </div>
                    <div class="arch-connector">▼ Closed-Loop Evaluation Bank</div>
                    <div class="arch-node">
                      <span class="node-title">Sub-Second Verified Response</span>
                      <span class="node-tech">&lt; 850ms Latency</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="business-impact-strip">
              <div class="impact-item">
                <strong>&lt; 850ms</strong>
                <span>Retrieval Latency</span>
              </div>
              <div class="impact-item">
                <strong>0</strong>
                <span>Manual File Desyncs</span>
              </div>
              <div class="impact-item">
                <strong>100%</strong>
                <span>Role-Based Data Isolation</span>
              </div>
              <div class="impact-item">
                <strong>~65%</strong>
                <span>Cost &amp; Token Reduction</span>
              </div>
            </div>
          </article>

          <!-- Case Study 2: Semi-Autonomous Agent Factory -->
          <article class="case-study-card featured-project">
            <div class="case-study-header">
              <div>
                <span class="category-badge">Semi-Autonomous Agent Factory &amp; Software Testing</span>
                <h3>Case Study 2: Semi-Autonomous Agent Factory &amp; Harness</h3>
              </div>
              <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
                <a class="btn btn-primary" href="/projects/ai-sdlc-studio">Explore Agent Factory →</a>
                <a class="btn btn-secondary" href="/projects/ai-engineer-blueprint">The AI Decision Blueprint →</a>
              </div>
            </div>
            <div class="case-story-grid">
              <div class="story-narrative">
                <h4>// The Organizational Friction</h4>
                <p>
                  Generative AI is an outstanding partner for rapidly turning business ideas into interactive prototypes. However, moving from prototype to reliable software requires repeatable engineering discipline rather than fragile, one-off prompts.
                </p>
                <div class="real-obstacle">
                  <strong>The Uncontrolled Loop Trap:</strong> Unconstrained agent workflows can loop indefinitely, repeat errors, and burn cloud budgets without producing production-grade test coverage or accessible interfaces.
                </div>
                <h4>// The Practical Solution</h4>
                <p>
                  Designed a 9-stage semi-autonomous development factory featuring deterministic $0 compute fast-paths (SHA-256 change fingerprinting), persistent vector memory (ChromaDB + JSON), automated test harnesses (pytest), and human-in-the-loop approval gates. Validated by shipping the "RegPulse" regulatory monitor with 100% automated test coverage.
                </p>
              </div>
              <div class="architecture-box">
                <h4>// Semi-Autonomous AI Factory</h4>
                <div class="arch-pipeline">
                  <div class="arch-flow-diagram">
                    <div class="arch-node">
                      <span class="node-title">Stage 01: Spec &amp; Requirements Agent</span>
                      <span class="node-tech">Decoupled Decision Logic • HITL Gate</span>
                    </div>
                    <div class="arch-connector">▼ $0 Change Fingerprint Check</div>
                    <div class="arch-node">
                      <span class="node-title">Stage 02-04: Automated TDD &amp; Coding</span>
                      <span class="node-tech">ChromaDB Persistent Memory</span>
                    </div>
                    <div class="arch-connector">▼ Self-Healing Test Execution</div>
                    <div class="arch-node">
                      <span class="node-title">Stage 05-07: UI/UX Audit &amp; Marketing</span>
                      <span class="node-tech">Desktop / Tablet / Mobile • HITL Gate</span>
                    </div>
                    <div class="arch-connector">▼ Enterprise Webhook Approval</div>
                    <div class="arch-node">
                      <span class="node-title">Stage 08-09: Deployment Readiness</span>
                      <span class="node-tech">GTM Packaging • Containerized App</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="business-impact-strip">
              <div class="impact-item">
                <strong>9 Stages</strong>
                <span>Supervised AI Factory</span>
              </div>
              <div class="impact-item">
                <strong>20 / 20</strong>
                <span>Automated Tests Passed</span>
              </div>
              <div class="impact-item">
                <strong>$0</strong>
                <span>Deterministic Fast-Paths</span>
              </div>
              <div class="impact-item">
                <strong>Grade A+</strong>
                <span>WCAG 2.1 AA Accessibility</span>
              </div>
            </div>
          </article>

          <!-- Case Study 3: Resume Refine Mobile iOS -->
          <article class="case-study-card">
            <div class="case-study-header">
              <div>
                <span class="category-badge">Mobile Product &amp; Cloud AI Integration</span>
                <h3>Case Study 3: Resume Refine: AI-Powered Career Assistant (Mobile iOS)</h3>
              </div>
              <a class="btn btn-primary" href="/projects/resume-refine">View Case Study →</a>
            </div>
            <div class="case-story-grid">
              <div class="story-narrative">
                <h4>// The User Friction</h4>
                <p>
                  Job applicants often struggle to tailor their resumes effectively for distinct roles and career transitions. Standard chatbot interfaces feel clunky on mobile devices and lack clear, structured guidance.
                </p>
                <div class="real-obstacle">
                  <strong>The Mobile AI Challenge:</strong> Delivering an AI-powered experience on mobile requires solving sub-second responsiveness, structured JSON formatting, prompt resilience, and graceful handling of poor network connectivity.
                </div>
                <h4>// The Practical Solution</h4>
                <p>
                  Developed a native iOS application in SwiftUI backed by a secure API Gateway, Python backend workers, and Google Gemini with structured schema validation. Provides job seekers with instant, constructive feedback and actionable resume enhancements.
                </p>
              </div>
              <div class="architecture-box">
                <h4>// Mobile-to-Cloud Architecture</h4>
                <div class="arch-pipeline">
                  <div class="arch-flow-diagram">
                    <div class="arch-node">
                      <span class="node-title">Native iOS SwiftUI Client</span>
                      <span class="node-tech">Tactile UX • Offline-First State</span>
                    </div>
                    <div class="arch-connector">▼ Secure API Gateway &amp; Rate Limiter</div>
                    <div class="arch-node">
                      <span class="node-title">Backend Worker &amp; Orchestration</span>
                      <span class="node-tech">FastAPI • Python Workflows</span>
                    </div>
                    <div class="arch-connector">▼ Structured Schema &amp; Guardrails</div>
                    <div class="arch-node">
                      <span class="node-title">Gemini Multimodal Model</span>
                      <span class="node-tech">Schema Validation &amp; Retries</span>
                    </div>
                    <div class="arch-connector">▼ Real-Time UI Render</div>
                    <div class="arch-node">
                      <span class="node-title">Intuitive Career Tool</span>
                      <span class="node-tech">App Store Quality Mobile UX</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="business-impact-strip">
              <div class="impact-item">
                <strong>0-to-1</strong>
                <span>Full Lifecycle Delivery</span>
              </div>
              <div class="impact-item">
                <strong>Sub-Second</strong>
                <span>Perceived Native Latency</span>
              </div>
              <div class="impact-item">
                <strong>Zero-Crash</strong>
                <span>Structured Prompt Resilience</span>
              </div>
              <div class="impact-item">
                <strong>Native iOS</strong>
                <span>App Store Quality Experience</span>
              </div>
            </div>
          </article>
        </div>
      </section>

      <!-- =================================================================
           SECTION 4: SOCIAL PROOF & MIDWEST FOCUS
           ================================================================= -->
      <section class="section" id="contact" style="padding-top: 1rem;">
        <div class="container">
          <div class="midwest-banner">
            <span class="midwest-badge">Midwest Focus // AI Enablement &amp; Innovation</span>
            <h2>Rooted in the Midwest. Ready to help teams adopt AI with confidence.</h2>
            <p>
              With aging family in the region and hands-on experience spanning global QSR innovation at McDonald's, operational systems at Scooter's Coffee, and regulated insurance carrier workflows, I bring practical Midwestern grit, authentic commitment, and hands-on execution to organizations across Chicago, Milwaukee, Indianapolis, and remote teams.
            </p>
            <div class="contact-action-bar">
              <button class="copy-btn" onclick="copyEmail(this)">
                <span>✉</span> Copy Direct Email (hello@nathanscottlester.com)
                <span class="copy-toast">Copied to Clipboard!</span>
              </button>
              <a class="btn btn-primary" href="mailto:hello@nathanscottlester.com?subject=Inquiry%20-%20Nathan%20Lester">Start a Conversation →</a>
              <a class="btn btn-secondary" href="https://github.com/N8Space" target="_blank" rel="noopener noreferrer">GitHub Code ↗</a>
            </div>
          </div>
        </div>
      </section>
    </main>
    """
    return render_page("AI Enablement & Innovation Leader Applying AI", "/", body)


@app.get("/projects", response_class=HTMLResponse)
async def projects():
    project_cards = render_project_cards(PROJECTS)
    body = f"""
    <main>
      <section class="page-hero">
        <div class="container">
          <span class="kicker">Case Studies &amp; Architecture</span>
          <h1>Production AI Systems Built for Enterprise Reality.</h1>
          <p>Each case study reflects how I approach AI leadership: unmasking demo hype, solving real edge cases, establishing rigorous governance, and delivering measurable business ROI.</p>
        </div>
      </section>
      <section class="section">
        <div class="container project-grid">{project_cards}</div>
      </section>
    </main>
    """
    return render_page("Production Case Studies", "/projects", body)


def get_ai_sdlc_studio_html() -> str:
    if AI_SDLC_STUDIO_FILE.exists():
        return AI_SDLC_STUDIO_FILE.read_text(encoding="utf-8")
    return AI_SDLC_STUDIO_HTML


def get_ai_engineer_blueprint_html() -> str:
    if AI_ENGINEER_BLUEPRINT_FILE.exists():
        return AI_ENGINEER_BLUEPRINT_FILE.read_text(encoding="utf-8")
    return AI_ENGINEER_BLUEPRINT_HTML


@app.get("/projects/ai-sdlc-studio", response_class=HTMLResponse)
async def project_ai_sdlc_studio():
    return HTMLResponse(get_ai_sdlc_studio_html())


@app.get("/projects/ai-engineer-blueprint", response_class=HTMLResponse)
async def project_ai_engineer_blueprint():
    return HTMLResponse(get_ai_engineer_blueprint_html())


@app.get("/projects/{slug}", response_class=HTMLResponse)
async def project_detail(slug: str):
    if slug == "ai-sdlc-studio":
        return HTMLResponse(get_ai_sdlc_studio_html())
    if slug == "ai-engineer-blueprint":
        return HTMLResponse(get_ai_engineer_blueprint_html())

    project = next((item for item in PROJECTS if item["slug"] == slug), None)
    if project is None:
        return render_page(
            "Project Not Found",
            "/projects",
            """
            <main>
              <section class="page-hero">
                <div class="container">
                  <span class="kicker">404</span>
                  <h1>Project not found.</h1>
                  <p>The requested project case study does not exist yet. Explore the active production case studies below.</p>
                  <a class="btn btn-primary" href="/projects">View all case studies</a>
                </div>
              </section>
            </main>
            """,
        )

    related = ''.join(
        f'<li><a href="/projects/{item["slug"]}">{item["title"]}</a></li>'
        for item in PROJECTS if item["slug"] != project["slug"]
    )
    tools = ''.join(f'<li>{tool}</li>' for tool in project["stack"])
    
    links_html = ""
    if project.get("demo_url") or project.get("github_url"):
        links = []
        if project.get("demo_url"):
            links.append(f'<a class="btn btn-primary" href="{project["demo_url"]}" target="_blank" rel="noopener noreferrer">Launch Live App ↗</a>')
        if project.get("github_url"):
            links.append(f'<a class="btn btn-secondary" href="{project["github_url"]}" target="_blank" rel="noopener noreferrer">View GitHub Repo ↗</a>')
        links_html = f'<div class="hero-actions" style="margin-top: 1.5rem; display: flex; gap: 0.75rem; flex-wrap: wrap;">{"".join(links)}</div>'

    body = f"""
    <main>
      <section class="page-hero">
        <div class="container">
          <span class="kicker">{project['category']}</span>
          <h1>{project['title']}</h1>
          <p>{project['summary']}</p>
        </div>
      </section>
      <section class="section">
        <div class="container detail-shell">
          <article class="article-panel">
            <h2>The Challenge &amp; Story</h2>
            <p>{project['story']}</p>
            <h2>Measurable Business Outcome</h2>
            <p>{project['outcome']}</p>
            <h2>Architectural Stack &amp; Tools</h2>
            <ul>{tools}</ul>
            {links_html}
          </article>
          <aside class="sidebar-panel">
            <h3>Why It Matters</h3>
            <p>Demonstrating the practical problem solving and situational awareness needed in AI enablement: real edge-case resolution, cost discipline, and dependable engineering execution.</p>
            <h3>Related Case Studies</h3>
            <ul class="sidebar-list">{related}</ul>
          </aside>
        </div>
      </section>
    </main>
    """
    return render_page(project["title"], "/projects", body)


@app.get("/about", response_class=HTMLResponse)
async def about():
    cert_list = ''.join(
        f'<li><strong>{cert["name"]}</strong> - {cert["status"]}</li>' for cert in CERTIFICATIONS
    )
    body = f"""
    <main>
      <section class="page-hero">
        <div class="container">
          <span class="kicker">Background &amp; Philosophy</span>
          <h1>Connecting Business Strategy, Responsible Governance &amp; Applied AI.</h1>
          <p>The practitioner's journey: from testing voice AI in McDonald's drive-thrus and operational IoT simulations at Scooter's Coffee to secure enterprise search at a regulated insurance carrier.</p>
        </div>
      </section>
      <section class="section">
        <div class="container detail-shell">
          <article class="article-panel">
            <h2>The Catalyst: Beyond the Demo Hype</h2>
            <p>
              My journey with applied AI started early. At <strong>McDonald's</strong>, I tested voice and generative AI in what we called the Voice-Activated Drive-Thru Order Taker. It was an unforgiving proving ground: roaring diesel engines, ambient outdoor noise, regional accents, sub-second latency requirements, and zero room for order errors. That experience taught me an indelible lesson: <em>happy-path demos in a clean boardroom mean nothing; real AI lives and dies in the unproven edge cases.</em>
            </p>
            <p>
              In December 2022, as Innovation Director for <strong>Scooter's Coffee</strong>, I harnessed the emerging power of generative AI to create operational simulation tools and IoT test suites. Later at a <strong>regulated insurance carrier</strong>, I watched the industry's vaporware hype cycle explode - countless point solutions that promised magic but collapsed under enterprise regulatory rules and fragmented data silos.
            </p>

            <h2>My Core Philosophy: Elevating Human Purpose</h2>
            <p>
              I have never viewed AI as a tool to displace human workers. Rather, it is the ultimate lever to eliminate routine drudgery - freeing cross-functional teams to do their best work with greater creativity, purpose, and empathy. The best way to prove or disprove how generative AI truly works is not through abstract slide decks, but by rolling up your sleeves and building reliable, secure solutions that teams love using.
            </p>

            <h2>The Pragmatic Approach</h2>
            <p>
              <strong>"Today, everyone can build with AI. The real question is: What should you build, and how do you design it so teams adopt it safely and reliably?"</strong>
            </p>
            <p>
              Generating simple code with an LLM is easy. Designing hybrid Azure vector search, deterministic $0 cost fast-paths, self-healing test harnesses, and continuous evaluation systems that protect data and budgets is what separates dependable solutions from sandbox experiments.
            </p>

            <h2>The Midwest Anchor</h2>
            <p>
              My focus on <strong>Chicago, IL, Milwaukee, WI, and Indianapolis, IN</strong> is deeply personal. My extended family is aging and located across the Midwest, and being close to them is a vital priority for my family. Combining Midwestern work ethic with multi-industry experience at enterprise scale, I am committed to helping organizations in this corridor adopt AI responsibly and effectively.
            </p>
          </article>
          <aside class="sidebar-panel">
            <h3>Certifications &amp; Learning Path</h3>
            <ul class="sidebar-list">{cert_list}</ul>
            <h3 style="margin-top: 2rem;">Get in Touch</h3>
            <p>Targeting AI Enablement Manager &amp; Associate Director roles in Chicago, Milwaukee, Indianapolis, or Remote.</p>
            <a class="btn btn-primary" href="mailto:hello@nathanscottlester.com" style="width: 100%; text-align: center;">Contact Nathan →</a>
          </aside>
        </div>
      </section>
    </main>
    """
    return render_page("Background & Philosophy", "/about", body)



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
        "/projects",
        "/projects/ai-sdlc-studio",
        "/projects/ai-engineer-blueprint",
        "/about",
    ]
    for project in PROJECTS:
        slug_route = f"/projects/{project['slug']}"
        if slug_route not in routes:
            routes.append(slug_route)

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for route in routes:
        loc = f"https://www.nathanscottlester.com{route}"
        xml_lines.append(f"  <url><loc>{loc}</loc><changefreq>weekly</changefreq><priority>{'1.0' if route == '' else '0.8'}</priority></url>")
    xml_lines.append("</urlset>")

    return Response(content="\n".join(xml_lines), media_type="application/xml")