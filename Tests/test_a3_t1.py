import pytest
from playwright.async_api import expect
@pytest.mark.asyncio
async def test_drop(async_page):
  await async_page.goto(" https://testautomationpractice.blogspot.com/")
  
  #static dropdown
  drop_down= async_page.get_by_role("textbox", name="Select an item")
  await drop_down.click()
  await async_page.get_by_text("Item 5",exact=True).click()
  await async_page.wait_for_timeout(5000)

  await expect(drop_down).to_have_value("Item 10")
  await async_page.wait_for_timeout(3000)

#Read all available dropdown options and print them.

#   all_options = await drop_down.all_inner_texts()

#   print(f"Total options found: {len(all_options)}")
#   print("Available options:")
#   for idx, text in enumerate(all_options, start=1):
#     print(f"  {idx}. {text.strip()}")
  