from playwright.sync_api import Page, expect

#Test1 asserting visibility of main modules 
def test_visibility(page: Page) -> None:
    page.goto("/")
    expect(page.locator("#empire-header").get_by_role("button", name="Deposit")).to_be_visible()
    expect(page.locator("#empire-header").get_by_role("button", name="Sign In")).to_be_visible()
    expect(page.locator("#empire-header").get_by_role("button", name="Withdraw")).to_be_visible()
    expect(page.locator("#headlessui-listbox-button-2")).to_be_visible()
    
    
#Expecting no accesss to deposit, if you have no account
def test_noSIGNINaccess(page: Page) -> None:
    page.goto("/")
    page.click("text=Deposit")
    page.click("text=CS:GO")
    expect(page.get_by_role("heading", name="Sign in").nth(1)).to_be_visible()

#New visitors can easily access faqs, its important because of trust players issues
def test_aboutInfo(page: Page) -> None:
    page.goto("/")
    faq_button = page.locator("#empire-header").get_by_role('link', name ="About")
    faq_button.click()
    assert page.inner_text('h4')

#Test asserting visibility of tab modules
def test_tabsSAME(page: Page) -> None:
    page.goto("/")
    link_locators = page.locator('.link mr-3 shrink-0 ').get_by_role('link').all()
    for _ in link_locators:
        print(_.get_attribute('href'))
    
#filling in dialogue box
def test_betAmount(page: Page) -> None:
    page.goto("/")
    page.get_by_placeholder("Enter bet amount...").click()
    page.get_by_placeholder("Enter bet amount...").fill("266666")
    page.get_by_role("button", name="Clear").click()

# def test_multiple_browsers(page: Page) -> None:
#     page.makepyfile(
#         """
#         def test_multiple_browsers(page):
#             page.set_content('<span id="foo">bar</span>')
#             assert page.query_selector("#foo")
#     """
#     )
#     result = page.runpytest(
#         "--browser", "chromium", "--browser", "firefox", "--browser", "webkit"
#     )
#     result.assert_outcomes(passed=3)


# def test_only_browser(page: Page) -> None:
#     result = page.runpytest(
#         "--browser", "chromium", "--browser", "firefox", "--browser", "webkit"
#     )
#     result.assert_outcomes(passed=1, skipped=2)
    
