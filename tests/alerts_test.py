from pages.alerts_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:
        def test_browser_new_tab(self, driver):
            form_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            form_page.open()
            text_result = form_page.new_tab()
            assert text_result == 'This is a sample page', 'the new tab has not opened or an incorrect tab has opened'

        def test_browser_new_windows(self, driver):
            form_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            form_page.open()
            text_result = form_page.new_tab()
            assert text_result == 'This is a sample page', 'the new window has not opened or an incorrect window has ' \
                                                           'opened'

    class TestAlerts:
        def test_browser_alerts_see_alert(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            alert_text = form_page.alerts_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        def test_browser_alerts_five_sec(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            alert_text = form_page.alerts_five_sec()
            assert alert_text == "This alert appeared after 5 seconds", 'Alert did not show up'

        def test_confirm_alert(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            alert_text = form_page.alerts_will_appear()
            assert alert_text == "You selected Ok", 'Alert did not show up'

        def test_prompt_alert(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            text, alert_text = form_page.alerts_prompt_alert()
            assert alert_text == f"You entered {text}", 'Alert did not show up'


