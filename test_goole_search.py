from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")
        page.fill("#APjFqb", "Twinkle")
        page.press("#APjFqb", "Enter")

        page.wait_for_selector("h3")
        page.locator("a:has(h3)").first.click()

        browser.close()