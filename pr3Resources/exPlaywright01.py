from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.chromium.launch(
    headless=False,
    executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
  page = browser.new_page()
  page.goto("https://www.clemson.edu")
  input("Press Enter...")

  page.evaluate("window.scrollTo({top: 1000, behavior: 'smooth'})")
  input("Press Enter2...")
