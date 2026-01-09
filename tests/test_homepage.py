import json
import os
import pytest
from playwright.async_api import async_playwright
from playwright.async_api import async_playwright, expect

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
		
		# # check
		# # Make sure page is still alive
		assert not page.is_closed()
		# Wait until notification icon is visible
		notif = page.locator("a.notifications")
		await notif.wait_for(state="visible", timeout=15000)
		# Click notification icon
		await notif.click()
		# Wait for redirect to notification page
		await page.wait_for_url("**/pmi-notifications", timeout=15000)
		await page.wait_for_timeout(5000)
		await page.locator("a.back.d-flex").first.click()
		await page.goto("https://in.pmiandu.com/s/")
		await page.wait_for_timeout(5000)

		assert not page.is_closed()

		view_details = page.locator("a.btntop:visible").first
		await view_details.click()

		await page.wait_for_url("**/s/top", timeout=15000)
		assert page.url.endswith("/s/top")
		await page.wait_for_timeout(10000)
		await page.locator("a.back.d-flex").first.click()
		await page.goto("https://in.pmiandu.com/s/")
		await page.wait_for_timeout(5000)
		await page.locator("button[role='tab'][aria-label='2 of 27']").click(force=True)
		await page.wait_for_timeout(5000)

		start_task = page.get_by_role("link", name="Start the Task")
		await expect(start_task).to_be_visible(timeout=10000)
		await start_task.click()
		await page.wait_for_timeout(10000)
		await page.locator("a.back.d-flex").first.click()
		await page.goto("https://in.pmiandu.com/s/")
		await page.wait_for_timeout(10000)
		
		assert not page.is_closed()
		# Wait for the carousel to be visible
		await page.wait_for_selector(".video-slider.slick-initialized", state="visible", timeout=20000)
		
		# Locate the image by its exact src
		image_card = page.locator("img[src='https://llp-pmi-prod-assets.s3.ap-south-1.amazonaws.com/My_time_my_gold_2x_1.png']")
		
		# Wait until it's visible
		await image_card.wait_for(state="visible", timeout=5000)
		
		
		