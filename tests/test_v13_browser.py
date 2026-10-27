"""Browser smoke tests for FrameShift v13. Requires `pip install playwright` and Chromium."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

def test_v13_browser_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1440, "height": 950})
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.set_content(HTML, wait_until="domcontentloaded")

        # Start at high difficulty and verify route heading focus.
        page.locator('input[name="difficulty"][value="high"]').check()
        page.get_by_role("button", name="Start the drill").click()
        page.wait_for_function("document.activeElement && document.activeElement.id === 'q1HeadTitle'")
        assert not page.locator("#q1TitaWrap").evaluate("el => el.classList.contains('hidden')")

        # Debounce remains quiet while typing; immediate submission clears pending timer/state.
        field = page.locator('#q1Tita')
        field.fill('Z')
        assert page.locator('#q1check').is_disabled()
        page.wait_for_timeout(650)
        assert page.locator('#q1Tita').get_attribute('aria-invalid') == 'true'
        assert 'enter a label' in page.locator('#q1TitaValidation').inner_text()
        page.evaluate("window.titaTopDown=null;window.titaTopBlur=null;document.querySelector('#q1check').addEventListener('mousedown',()=>window.titaTopDown=document.querySelector('#q1check').getBoundingClientRect().top);document.querySelector('#q1Tita').addEventListener('blur',()=>window.titaTopBlur=document.querySelector('#q1check').getBoundingClientRect().top)")
        field.fill('G')
        assert not page.locator('#q1check').is_disabled()
        page.locator('#q1check').click()
        page.wait_for_function("document.querySelector('#q1feedback').classList.contains('show')", timeout=5000)
        assert abs(page.evaluate('window.titaTopDown - window.titaTopBlur')) < 0.5, 'Clearing TITA validation shifted the submit button during click.'
        assert page.locator('#q1Tita').get_attribute('aria-invalid') == 'false'
        assert page.locator('#q1TitaValidation').inner_text() == ''
        assert page.evaluate("titaValidationTimeouts.q1 === null")

        # Each screen transition moves focus to its main heading.
        page.locator('#q1next').click()
        page.wait_for_function("document.activeElement && document.activeElement.id === 'mixedTitle'")
        for _ in range(4):
            page.locator('#mixedOptions .opt').first.click()
            page.locator('#mixedCheck').click()
            page.locator('#mixedNext').click()
        page.wait_for_function("document.activeElement && document.activeElement.id === 'q2HeadTitle'")
        field2 = page.locator('#q2Tita')
        field2.fill('C')
        page.locator('#q2check').click()
        page.wait_for_function("document.querySelector('#q2feedback').classList.contains('show')")
        page.locator('#q2finish').click()
        page.wait_for_function("document.activeElement && document.activeElement.id === 'resultTitle'")
        assert page.locator('#personalFeedbackModal').evaluate("el => el.hidden")

        # Explicit recap opens, traps focus, and returns focus to its invocation point.
        page.locator('#openRecapBtn').click()
        page.wait_for_function("document.activeElement && document.activeElement.id === 'closeFeedbackBtn'")
        page.locator('#feedbackOpenCoach').focus()
        page.keyboard.press('Tab')
        assert page.evaluate("document.activeElement.id") == 'closeFeedbackBtn'
        page.keyboard.press('Shift+Tab')
        assert page.evaluate("document.activeElement.id") == 'feedbackOpenCoach'
        page.keyboard.press('Escape')
        page.wait_for_function("document.activeElement && document.activeElement.id === 'openRecapBtn'")

        # Calculator focus trap and focus restoration.
        page.locator('#openCalculatorBtn').click()
        page.wait_for_function("document.activeElement && document.activeElement.id === 'closeCalculatorBtn'")
        calc_last = page.locator('#calculatorLayer [role="dialog"] button:not([disabled])').last
        calc_last.focus()
        page.keyboard.press('Tab')
        assert page.evaluate("document.activeElement.id") == 'closeCalculatorBtn'
        page.keyboard.press('Shift+Tab')
        assert page.evaluate("document.activeElement.id") == 'clearCalcHistoryBtn'
        page.keyboard.press('Escape')
        page.wait_for_function("document.activeElement && document.activeElement.id === 'openCalculatorBtn'")

        # Coach drawer focus trap and return focus.
        page.locator('#openCoachBtn').click()
        page.wait_for_function("!document.querySelector('#coachLayer').hidden")
        page.locator('#coachLayer [role="dialog"] button:not([disabled])').last.focus()
        page.keyboard.press('Tab')
        assert page.evaluate("document.activeElement.id") == 'closeCoachBtn'
        page.keyboard.press('Escape')
        page.wait_for_function("document.activeElement && document.activeElement.id === 'openCoachBtn'")

        assert not errors, f"Browser errors: {errors}"
        print('Playwright v13 browser flow passed: heading focus, TITA cleanup and stable button geometry, full route, opt-in recap focus trap, calculator/Coach drawer traps, Escape close and focus restoration.')
        browser.close()

if __name__ == '__main__':
    test_v13_browser_flow()
