from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) #Luanch the browser
        page = browser.new_page() #Creates the new tab

        page.goto("https://www.google.com") #Navigate to the URL
        page.fill("#APjFqb", "Twinkle") #Enter the test into the search box
        page.press("#APjFqb", "Enter") #Pressing the Enter

        page.wait_for_selector("h3") #Wait for the element to load
        page.locator("a:has(h3)").first.click() #Click on the First result

        browser.close() #Close the broswer
