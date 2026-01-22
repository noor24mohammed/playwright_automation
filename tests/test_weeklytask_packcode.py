import json
import os
import pytest
from playwright.async_api import async_playwright
from playwright.async_api import async_playwright, expect
from playwright.async_api import Page
import re
import asyncio

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
        # await page.goto("https://in.pmiandu.com", wait_until="domcontentloaded")

        await page.locator("#input-3").fill(login_data["mobile"])
        await page.locator("#input-5").fill(login_data["password"])

        await page.locator("text=Log In").click()
        await page.wait_for_timeout(5000)

        await page.locator("//input[@type='checkbox' and contains(@id,'Logout_from_Other_sessions')]").check()
        await page.locator("//input[@id='thePage:j_id2:i:f:pb:pbb:nextAjax']").click()
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.wait_for_timeout(10000)
        
        assert not page.is_closed()
        tasks_link = page.locator('a[href="https://in.pmiandu.com/s/pmi-all-tasks"]').first
        element_handle = await tasks_link.element_handle()
        await page.evaluate('(el) => el.click()', element_handle)
        await page.wait_for_timeout(10000)

        tasks_frame = page.frame_locator('iframe[src*="irepo.in/tasks"]')
        pack_code_card = tasks_frame.locator(
        "div.MuiBox-root.css-1a88jnx",
        has=tasks_frame.locator(
        "span",
        has_text=re.compile(r"Pack Code", re.IGNORECASE)
        )
        ).first

        await expect(pack_code_card).to_be_visible(timeout=15000)
        print("Pack Code card found")

        cta_button = pack_code_card.locator(
        "button",
        has_text=re.compile(r"(Start The Task|Resume Task)", re.IGNORECASE)
        ).first

        await expect(cta_button).to_be_visible(timeout=15000)
        await expect(cta_button).to_be_enabled()

        await cta_button.click(force=True)
        await page.wait_for_timeout(5000)


        # 1️⃣ Wait for the iframe to appear
        iframe_el = page.locator('#iframeContainer iframe')
        await expect(iframe_el).to_be_visible(timeout=15000)

        # 2️⃣ Get the iframe element handle
        iframe_handle = await iframe_el.element_handle()  # ✅ element handle

        # 3️⃣ Get the actual Frame object from element handle
        task_frame = await iframe_handle.content_frame()  # ✅ now you have a Frame

        # 4️⃣ Locate the "Start the task" button inside the iframe
        start_task_button = task_frame.locator(
        "button",
        has_text=re.compile(r"Start the task", re.IGNORECASE)
        ).first

        # 5️⃣ Ensure the button is visible & enabled
        await expect(start_task_button).to_be_visible(timeout=15000)
        await expect(start_task_button).to_be_enabled()

        # 6️⃣ Click the button
        await start_task_button.click(force=True)
        await page.wait_for_timeout(10000)

       # 1️⃣ Wait for the outer iframe to appear
        iframe_element = await page.wait_for_selector("div#iframeContainer > iframe", timeout=120000)

        # 2️⃣ Get the content frame of the iframe
        iframe = await iframe_element.content_frame()
        if not iframe:
            raise Exception("Iframe content frame is not available!")

        # 3️⃣ Wait for the input field inside the iframe
        enter_code_input = iframe.locator("input[placeholder='Enter Code']").first
        await enter_code_input.wait_for(state="visible", timeout=60000)

        # 4️⃣ Enter your code
        await enter_code_input.fill("123456789012")

        # 5️⃣ Click the Submit button (optional, if required)
        submit_button = enter_code_input.locator("xpath=following-sibling::button[contains(@class,'submit-barcode')]")
        await submit_button.click()

        # 6️⃣ Optional: wait a bit for the action to complete
        await page.wait_for_timeout(5000)


        # dotcode_iframe_el = None
        # for _ in range(60):  # check every second up to 60s
        #     iframes = await page.locator("iframe").all()
        #     for iframe in iframes:
        #         src = await iframe.get_attribute("src")
        #         if src and "mitrapp2.com/wsa/app" in src:
        #             dotcode_iframe_el = iframe
        #             break
                
        #     if dotcode_iframe_el:
        #         break
        #     await asyncio.sleep(1)
                    
        # if not dotcode_iframe_el:
        #     raise Exception("Dot Code iframe never appeared!")
                        
                        # 2️⃣ Get content frame
                        
        # dotcode_frame = await dotcode_iframe_el.content_frame()
        # if not dotcode_frame:
        #     raise Exception("Dot Code iframe content frame not available yet!")
                            
        #  # 3️⃣ Wait for input inside iframe
        # enter_code_input = dotcode_frame.locator("input[placeholder='Enter Code']").first
        # await enter_code_input.wait_for(state="visible", timeout=60000)
                            
        # # 4️⃣ Enter code
        # await enter_code_input.fill("123456789012")
        # await page.wait_for_timeout(10000)

       