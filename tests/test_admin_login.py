# import pytest
# from playwright.async_api import async_playwright

# @pytest.mark.asyncio
# async def test_login():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()

#         await page.goto("https://in.pmiandu.com/s/")
#         print("[CHROMIUM] Test ran in chromium")

#         await page.locator("xpath=//*[@id='input-3']").fill("+917676340719")
#         await page.locator("xpath=//*[@id='input-5']").fill("Jeet@123")
#         await page.locator("text=Log In").click()
#         await page.wait_for_timeout(3000)

#         await browser.close()
