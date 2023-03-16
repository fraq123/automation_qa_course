import allure
from pages.alerts_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramePage, ModalDialogPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        @allure.title('Проверка открытия нового окна')
        def test_browser_new_tab(self, driver):
            form_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            form_page.open()
            text_result = form_page.new_tab()
            assert text_result == 'This is a sample page', 'the new tab has not opened or an incorrect tab has opened'

        @allure.title('Проверка открытия нового маленького окна')
        def test_browser_new_windows(self, driver):
            form_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            form_page.open()
            text_result = form_page.new_tab()
            assert text_result == 'This is a sample page', 'the new window has not opened or an incorrect window has ' \
                                                           'opened'

    @allure.feature('Alerts Page')
    class TestAlerts:
        @allure.title('Нажатие на click me')
        def test_browser_alerts_see_alert(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            alert_text = form_page.alerts_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        @allure.title('Нажатие на click me и ожидание 5 секунд')
        def test_browser_alerts_five_sec(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            alert_text = form_page.alerts_five_sec()
            assert alert_text == "This alert appeared after 5 seconds", 'Alert did not show up'

        @allure.title('Нажатие на click me и подтверждение ok')
        def test_confirm_alert(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            alert_text = form_page.alerts_will_appear()
            assert alert_text == "You selected Ok", 'Alert did not show up'

        @allure.title('Нажатие на click me и пишем своё имя')
        def test_prompt_alert(self, driver):
            form_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            form_page.open()
            text, alert_text = form_page.alerts_prompt_alert()
            assert alert_text == f"You entered {text}", 'Alert did not show up'

    @allure.feature('Frame Page')
    class TestFramesPage:
        @allure.title('Проверка размера окна и текста в окне')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.frame_first('frame1')
            result_frame2 = frame_page.frame_first('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    @allure.feature('Nested Page')
    class TestNestedFramePage:
        @allure.title('Проверка страницы с вложенными фреймами')
        def test_nested_frame(self, driver):
            nested_frame_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    @allure.feature('Modal Dialog Page')
    class TestModalDialogsPage:
        @allure.title('Проверка текста в диалоговых окнах')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_small_modal()
            assert small[1] < large[1], 'text from small dialog is less than text from small dialog'
            assert small[0] == 'Small Modal', 'The header is not "Small modal"'
            assert large[0] == 'Large Modal', 'The header is not "Large modal"'
