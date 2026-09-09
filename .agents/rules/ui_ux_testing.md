---
trigger: always_on
description: Mandatory rule to use macOS native Safari (safaridriver) and Selenium for UI/UX testing instead of Playwright.
---

# UI/UX Testing & Visual Verification Rule

> [!IMPORTANT]
> **NO PLAYWRIGHT DRIVER DOWNLOADS**: Do not use Playwright or attempt to download external Playwright browser binaries. Playwright's remote CDN downloads frequently fail on macOS arm64.

## Standard UI/UX Testing Protocol

For all UI/UX testing, responsive viewport audits, and screenshot capture of locally developed web pages:
1. **Primary Tool:** Use **macOS native `safaridriver` + Selenium**.
2. **Turnkey Runner:** Always use the workspace harness script:
   ```bash
   python3 .agents/skills/safari-ui-testing/scripts/verify_ui.py --url http://127.0.0.1:8000/<path>
   ```
3. **Execution Behavior:**
   - The runner attempts to drive native Safari (`webdriver.Safari()`).
   - If Safari's "Allow Remote Automation" setting has not yet been toggled by the user, the script automatically falls back to the locally installed system Google Chrome in headless mode.
   - Outputs responsive screenshots for Desktop (1440x900), Tablet (768x1024), and Mobile (375x812) to `static/img/screenshots/`.
4. **Enabling Safari Remote Automation (One-time macOS setup):**
   - Open Safari > Settings > Advanced > check "Show features for web developers".
   - In menu bar: Develop > check "Allow Remote Automation".
