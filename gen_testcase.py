# gen_testcase.py
from pathlib import Path

ticket = Path("prompts/ticket_001.md").read_text()

# ✨ Prompt GitHub Copilot/Cursor:
# 👉 "Based on this ticket, generate a Playwright test case for login page on https://practicesoftwaretesting.com/ supporting CAPTCHA toggle"

output = f"""
import {{ test, expect }} from '@playwright/test';

test('login with CAPTCHA enabled on Firefox', async ({{ page }}) => {{
  await page.goto('https://practicesoftwaretesting.com/');
  await page.click('text=My Account');
  await page.fill('[name="email"]', 'testuser@example.com');
  await page.fill('[name="password"]', 'Test@123');
  await page.click('text=Sign In');
  await expect(page.locator('[data-test="user-menu"]')).toBeVisible();
}});
"""

Path("tests/login.spec.ts").write_text(output.strip())
