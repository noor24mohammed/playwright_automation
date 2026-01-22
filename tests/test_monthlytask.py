import json
import os
import pytest
from playwright.async_api import async_playwright
from playwright.async_api import async_playwright, expect
from playwright.async_api import Page
import re 

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
        # Create a locator for the button with text matching either option
        cta_button = tasks_frame.locator(
            "button",
            has_text=re.compile(r"(Start The Task|Resume Task)", re.IGNORECASE)
            )
            
            # Wait for the button to be visible, then click it
        await cta_button.first.wait_for(state="visible", timeout=30000)
        await cta_button.first.click()
        await page.wait_for_timeout(10000)

        scan_frame = page.frame_locator('iframe[src*="/tasks/"]')
        scan_cta = scan_frame.locator(
            'button:has-text("Scan Pack To Earn Points")'
        )
        
        # Ensure visible
        await expect(scan_cta).to_be_visible(timeout=20000)
        
        # Scroll + force focus
        await scan_cta.scroll_into_view_if_needed()
        await page.wait_for_timeout(500)
        
        # JS click INSIDE iframe (CRITICAL FIX)
        await scan_cta.evaluate(
            """(btn) => {
            btn.focus();
            btn.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
            btn.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
            btn.click();
            }"""
            )
        await page.wait_for_timeout(5000)
        await page.locator("a.back.d-flex").first.click()
        await page.wait_for_timeout(5000)
   

        tasks_link = page.locator('a[href="https://in.pmiandu.com/s/pmi-all-tasks"]').first
        element_handle = await tasks_link.element_handle()
        await page.evaluate('(el) => el.click()', element_handle)
        await page.wait_for_timeout(10000)
        tasks_frame = page.frame_locator('iframe[src*="irepo.in/tasks"]')
        # Create a locator for the button with text matching either option
        cta_button = tasks_frame.locator(
            "button",
            has_text=re.compile(r"(Start The Task|Resume Task)", re.IGNORECASE)
            )
        in_review_tab = tasks_frame.locator("#simple-tab-1")
        await in_review_tab.wait_for(state="attached", timeout=30000)
        await in_review_tab.click()
        await page.wait_for_timeout(10000)
        await tasks_frame.locator("#simple-tab-2").click()
        await page.wait_for_timeout(10000)