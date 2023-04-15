# do this stuff first
# pip install pytest-playwright
# playwright install

url = 'https://www.parkrun.org.uk/edinburgh/results/599/'
from playwright.sync_api import sync_playwright

def run(playwright):
    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_13,
    )

    # browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    print(page.content())
    html = page.content()
    f = open('./saved.html','w')
    f.write(html)
    f.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


