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
        # await page.goto("https://in.pmiandu.com/s/")
        await page.goto("https://in.pmiandu.com", wait_until="domcontentloaded")

        await page.locator("#input-3").fill(login_data["mobile"])
        await page.locator("#input-5").fill(login_data["password"])

        await page.locator("text=Log In").click()
        await page.wait_for_timeout(5000)

        await page.locator("//input[@type='checkbox' and contains(@id,'Logout_from_Other_sessions')]").check()
        await page.locator("//input[@id='thePage:j_id2:i:f:pb:pbb:nextAjax']").click()
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.wait_for_timeout(10000)
        
        # # Make sure page is still alive
        # assert not page.is_closed()
        # # Wait until notification icon is visible
        # notif = page.locator("a.notifications")
        # await notif.wait_for(state="visible", timeout=15000)
        # # Click notification icon
        # await notif.click()
        # # Wait for redirect to notification page
        # await page.wait_for_url("**/pmi-notifications", timeout=15000)
        # await page.wait_for_timeout(5000)
        # await page.locator("a.back.d-flex").first.click()
        # await page.goto("https://in.pmiandu.com/s/")
        # await page.wait_for_timeout(5000)

    #     assert not page.is_closed()

    #     view_details = page.locator("a.btntop:visible").first
    #     await view_details.click()

    #     await page.wait_for_url("**/s/top", timeout=15000)
    #     assert page.url.endswith("/s/top")
    #     await page.wait_for_timeout(10000)
    #     await page.locator("a.back.d-flex").first.click()
    #     await page.goto("https://in.pmiandu.com/s/")
    #     await page.wait_for_timeout(5000)
    #     await page.locator("button[role='tab'][aria-label='2 of 27']").click(force=True)
    #     await page.wait_for_timeout(5000)
   
    #     dots = page.locator("div.video-slider ul.slick-dots button")

    #     total = await dots.count()
    #     print("Total dots:", total)

    #     for i in range(total):
    #      dot = dots.nth(i)
    #     await dot.scroll_into_view_if_needed()
    #     await dot.click(force=True)
    #     await page.wait_for_timeout(1000)
        

    # await page.wait_for_timeout(2000)

    # if len(page.context.pages) > 1:
    #     page = page.context.pages[-1]

    # assert not page.is_closed(), "Page closed after login!"

    # # ⏳ Safe wait
    # await page.wait_for_load_state("domcontentloaded")

    # # 🔴 CTA
    # cta = page.locator("a.btnRed", has_text="View all tasks")

    # await cta.wait_for(state="visible", timeout=15000)

    # async with page.context.expect_page(timeout=10000) as page_info:
    #     await cta.click()

    # try:
    #     new_page = await page_info.value
    # except:
    #     new_page = page

    # await new_page.wait_for_load_state("domcontentloaded")

    # assert "pmi-all-tasks" in new_page.url



















# # 1️⃣ Check image element is visible
#         await img.wait_for(state="visible")

# # 2️⃣ Check src attribute exists
#         src = await img.get_attribute("src")
#         assert src is not None, "Navbar toggle image src is missing"

# # 3️⃣ (Optional) Verify image file name
#         assert src.endswith("hamberger+3+dots.svg")

#     from urllib.parse import urlparse
#     img = page.locator("img[src*='hamberger']")

#     src = await img.get_attribute("src")

#     parsed = urlparse(src)
#     actual_path = parsed.netloc + parsed.path

#     expected = "llp-pmi-prod-assets.s3.ap-south-1.amazonaws.com/Banner/hamberger+3+dots.svg"

#     assert actual_path == expected

    # notification_link = page.locator("a.notifications")

    # await notification_link.wait_for(state="visible")
    # await notification_link.click()




        

       