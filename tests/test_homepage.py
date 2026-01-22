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
		
		# check
		# # # Make sure page is still alive
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


		# STATIC code for the MONTHLY and WEEKLY TASK DOT SLEEK cards 
		# assert not page.is_closed()
		# view_details = page.locator("a.btntop:visible").first
		# await view_details.click()

		# await page.wait_for_url("**/s/top", timeout=15000)
		# assert page.url.endswith("/s/top")
		# # await page.wait_for_timeout(10000)
		# await page.locator("a.back.d-flex").first.click()
		# await page.goto("https://in.pmiandu.com/s/")
		# await page.wait_for_timeout(5000)
		# await page.locator("button[role='tab'][aria-label='2 of 6']").click(force=True)
		# await page.wait_for_timeout(5000)

		# start_task = page.get_by_role("link", name="Start the Task")
		# await expect(start_task).to_be_visible(timeout=10000)
		# await start_task.click()
		# await page.wait_for_timeout(10000)
		# await page.locator("a.back.d-flex").first.click()
		# await page.goto("https://in.pmiandu.com/s/")
		# await page.wait_for_timeout(10000)


		 DYNAMIC CODE for the MONTHLY and WEEKLY TASK DOT SLEEK CARDS
		Pause autoplay (critical)

		await page.evaluate("$('.task-slider').slick('slickPause')")

		dots = page.locator(".task-slider .slick-dots li button")
		dot_count = await dots.count()

		for i in range(dot_count):
			# Move slider
			await dots.nth(i).click()
			await page.wait_for_timeout(3000)
			
			# Get ACTIVE, NON-CLONED card
			active_card = page.locator(
        		".task-slider .slick-slide.slick-active:not(.slick-cloned)"
    		).first
			
			await active_card.wait_for(state="visible", timeout=5000)
			
			# Click CTA inside card (Start the Task / View Details)
			cta = active_card.locator("a[href*='/s/']")
			
			if await cta.count() > 0:
				href = await cta.get_attribute("href")
				print(f"Clicking card: {href}")
				
				await cta.first.click(force=True)
				# Wait for navigation
				await page.wait_for_load_state("domcontentloaded")
				await page.wait_for_timeout(5000)
				
				# Go back
				await page.go_back()
				await page.wait_for_load_state("domcontentloaded")
			else:
				print("No clickable CTA in this card")


		 DYNAMIC CODE for IMAGE and VIDEO section DOT SLEEK CARDS
		# Pause autoplay once
		await page.evaluate("$('.video-slider').slick('slickPause');")

		dots = page.locator(".video-slider .slick-dots li button")
		dot_count = await dots.count()

		for i in range(dot_count):
			await dots.nth(i).click()
			await page.wait_for_timeout(10000)
			
			# 1️⃣ Get active slide ONLY
			active_slide = page.locator(
				".video-slider .slick-slide.slick-current.slick-active:not(.slick-cloned)"
			)
			
			await active_slide.wait_for(state="visible", timeout=5000)
			# 2️⃣ Check if IMAGE card exists
			image_card = active_slide.locator("a[data-fancybox]")
			
			if await image_card.count() > 0:
				# ---------- IMAGE ----------
				href = await image_card.get_attribute("href")
				print(f"IMAGE card → {href}")
				
				await image_card.click(force=True)
				await page.wait_for_load_state("load")
				await page.wait_for_timeout(10000)
				await page.go_back()
				await page.wait_for_load_state("domcontentloaded")
				
			else:
				# ---------- VIDEO ----------
				print("VIDEO card detected")
				# Click the video card itself (NOT a[data-fancybox])
				await active_slide.click(force=True)
				# Wait until iframe is injected
				await page.wait_for_function(
            		"""
            		() => Array.from(document.querySelectorAll('iframe'))
                	.some(f => f.src && f.src.includes('videomarketingplatform'))
            		""",
            		timeout=30000
        		)
				
				# 3️⃣ Wait for the play button 
				play_button = page.locator("button.big-play-button")

				# await play_button.wait_for(state="visible", timeout=20000)

				# # Ensure it is clickable
				# await play_button.scroll_into_view_if_needed()

				# Click PLAY
				await play_button.click(force=True)

				# Let video start
				await page.wait_for_timeout(15000)

		cta = page.locator("a.btnRed[href*='pmi-reward-page']")
		await cta.wait_for(state="visible", timeout=10000)
		await cta.scroll_into_view_if_needed()
		await cta.click()
		await page.wait_for_timeout(10000)
		await page.locator("a.back.d-flex").first.click()
		await page.wait_for_timeout(5000)


				