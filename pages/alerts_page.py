import time
from locators.alerts_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def alerts_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT).click()
        confirm = self.driver.switch_to.alert
        confirm.accept()

    def alerts_five_sec(self):
        self.element_is_visible(self.locators.ALERT_BUTTON_5SEC).click()
        time.sleep(6)
        confirm = self.driver.switch_to.alert
        confirm.accept()
