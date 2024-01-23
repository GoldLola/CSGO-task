from playwright.sync_api import Page, expect


def test_visibility(page: Page) -> None:
    page.goto("/")
    expect(page.locator("#empire-header").get_by_role("button", name="Deposit")).to_be_visible()
    expect(page.locator("#empire-header").get_by_role("button", name="Sign In")).to_be_visible()
    expect(page.locator("#empire-header").get_by_role("button", name="Withdraw")).to_be_visible()
    expect(page.locator("#headlessui-listbox-button-2")).to_be_visible()
    assert("text=About")
    


def test_noSIGNINaccess(page: Page) -> None:
    page.goto("/")
    page.click("text=Deposit")
    page.click("text=CS:GO")
    expect(page.get_by_role("heading", name="Sign in").nth(1)).to_be_visible()


