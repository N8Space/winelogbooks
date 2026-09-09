# Workspace Agent Guidelines

## UI/UX & Browser Testing Policy
- **Never use Playwright**: Do not use Playwright or attempt to download external browser driver binaries.
- **Use macOS Native Safari & Selenium**: For all local webpage UI/UX testing, visual audits, and screenshot captures, use Selenium with macOS native `safaridriver`.
- **Harness Runner**: Execute `.agents/skills/safari-ui-testing/scripts/verify_ui.py --url <URL>`. The runner drives native Safari, with seamless fallback to system Chrome headless if Safari's Remote Automation toggle is awaiting user activation.
- **Viewports**: Standard test runs audit Desktop (1440x900), Tablet (768x1024), and Mobile (375x812).
