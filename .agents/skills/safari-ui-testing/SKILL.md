---
name: safari-ui-testing
description: |
  Automated UI/UX verification, responsive viewport audits, and screenshot capture for locally developed web applications using macOS native Safari (safaridriver) and Selenium. Use whenever you need to test local web pages, verify UI layouts across viewports, capture screenshots, or run visual audits without relying on Playwright.
---

# macOS Native Safari & Selenium UI/UX Testing Skill

This skill provides automated UI/UX verification, responsive visual testing, and screenshot auditing for local web applications using **macOS native `safaridriver` + Selenium**.

## Why This Skill Exists
- **Zero Driver Downloads:** Avoids Playwright's fragile external binary downloads and CDN 404 issues.
- **Native macOS Execution:** Uses the `safaridriver` already installed with Safari (`/System/Cryptexes/App/usr/bin/safaridriver`), with automatic support for system Chrome as an alternate headless runner.
- **Multi-Viewport Audits:** Tests Desktop (1440x900), Tablet (768x1024), and Mobile (375x812) breakpoints.

## One-Time Safari Setup
To allow Selenium to drive Safari on macOS, enable Remote Automation once:
1. Open **Safari**.
2. Go to **Safari > Settings > Advanced** (or **Preferences**), and check **"Show features for web developers"** (or "Show Develop menu in menu bar").
3. In the menu bar, click **Develop > Allow Remote Automation**.
*(Alternatively, run `sudo safaridriver --enable` in Terminal).*

## Using the UI Verification Runner
A pre-built testing harness is available at `.agents/skills/safari-ui-testing/scripts/verify_ui.py`.

### Basic Usage:
```bash
# Verify a page and capture screenshots across all viewports
python3 .agents/skills/safari-ui-testing/scripts/verify_ui.py --url http://127.0.0.1:8000/projects/ai-engineer-blueprint

# Target specific viewports
python3 .agents/skills/safari-ui-testing/scripts/verify_ui.py --url http://127.0.0.1:8000/projects/ai-engineer-blueprint --viewport mobile

# Force Safari (will prompt if Remote Automation needs to be toggled)
python3 .agents/skills/safari-ui-testing/scripts/verify_ui.py --url http://127.0.0.1:8000/projects/ai-engineer-blueprint --browser safari
```

### Python API Integration:
```python
from selenium import webdriver

# Native Safari
driver = webdriver.Safari()
try:
    driver.set_window_size(1440, 900)
    driver.get("http://127.0.0.1:8000/projects/ai-engineer-blueprint")
    driver.save_screenshot("screenshot_desktop.png")
finally:
    driver.quit()
```
