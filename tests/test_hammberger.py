import json
import os
import pytest
from playwright.async_api import async_playwright

def load_login_data():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "data",
        "dte_app_login_data.json"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)["logins"] 

@pytest.mark.asyncio
@pytest.mark.parametrize("login_data", load_login_data())
async def test_login(login_data):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        context = await browser.new_context(
        permissions=["geolocation"],
        geolocation={"latitude": 12.9716, "longitude": 77.5946}  # any valid coords
    )
        page = await context.new_page()
        await page.goto("https://in.pmiandu.com/s/")

        await page.locator("#input-3").fill(login_data["mobile"])
        await page.locator("#input-5").fill(login_data["password"])

        await page.locator("text=Log In").click()
        await page.wait_for_timeout(10000)
       

        await page.locator("//input[@type='checkbox' and contains(@id,'Logout_from_Other_sessions')]").check()
        await page.locator("//input[@id='thePage:j_id2:i:f:pb:pbb:nextAjax']").click()
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.wait_for_timeout(10000)

        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.wait_for_timeout(3000)
        # await page.locator("button.closeIcon.openMenu").click()
        # await page.goto("https://in.pmiandu.com/s/")

        await page.locator("#navbarSupportedContent").get_by_role("link", name="Home").click()
        await page.wait_for_timeout(3000)
        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.locator("a.nav-link").get_by_text("Profile", exact=True).click()
        await page.wait_for_load_state("networkidle")

        await page.goto("https://in.pmiandu.com/s/")
        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.locator("a.nav-link").get_by_text("Tasks").click()
        await page.wait_for_timeout(5000)
        await page.locator("div.pmi-custom-header a.back").click()
        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.wait_for_timeout(5000)
        await page.locator("a.nav-link").get_by_text("Rewards", exact=True).click()
        await page.wait_for_timeout(5000)
        await page.locator("a.back.d-flex[href='https://in.pmiandu.com/s/']").click()
        await page.wait_for_timeout(5000)
        
        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.locator("a.nav-link").get_by_text("Brands", exact=True).click()
        await page.wait_for_load_state("networkidle")
        await page.goto("https://in.pmiandu.com/s/")
        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.wait_for_timeout(5000)

        await page.locator("a.nav-link:has-text('Points History')").click()
        await page.wait_for_timeout(5000)
        await page.locator("a.back.d-flex").first.click()
        await page.goto("https://in.pmiandu.com/s/")
        await page.wait_for_timeout(5000)

        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.locator("a.nav-link").get_by_text("About Us", exact=True).click()
        await page.wait_for_timeout(5000)
        await page.locator("a.back.d-flex").first.click()
        await page.goto("https://in.pmiandu.com/s/")
        await page.wait_for_timeout(5000)

        await page.locator("//button[contains(@class,'navbar-toggler')]").click()
        await page.locator("a.nav-link").get_by_text("Top Outlet Program", exact=True).click()
        await page.wait_for_timeout(5000)
        await page.locator("a.back.d-flex").first.click()
        await page.goto("https://in.pmiandu.com/s/")
        await page.wait_for_timeout(5000)