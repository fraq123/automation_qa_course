import random
import time

import allure

from locators.alerts_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramePageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('проверка открытия новой вкладки')
    def new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    @allure.step('проверка открытия нового окна')
    def new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('получения подтверждения')
    def alerts_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT).click()
        confirm = self.driver.switch_to.alert
        return confirm.text

    @allure.step('проверка появления подтверждения через 5 секунд')
    def alerts_five_sec(self):
        self.element_is_visible(self.locators.ALERT_BUTTON_5SEC).click()
        time.sleep(6)
        confirm = self.driver.switch_to.alert
        return confirm.text

    @allure.step('проверка появления подтверждения или отклонения')
    def alerts_will_appear(self):
        self.element_is_visible(self.locators.ALERT_BUTTON_OK).click()
        confirm = self.driver.switch_to.alert
        confirm.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('проверка появления окна куда вписать своё имя')
    def alerts_prompt_alert(self):
        text = f'autotest{random.randint(0, 999)}'
        self.element_is_visible(self.locators.ALERT_BUTTON_SEND).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_ALERT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('проверка фрейма')
    def frame_first(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]


class NestedFramePage(BasePage):
    locators = NestedFramePageLocators()

    @allure.step('проверка вложенного фрейма')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_IFRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()

    @allure.step('проверка модальных диалогов')
    def check_small_modal(self):
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        title_small_text = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.BODY_SMALL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE).click()
        self.element_is_visible(self.locators.LARGE_MODAL).click()
        title_large_text = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE).text
        return [title_small_text, len(body_small_text)], [title_large_text, len(body_large_text)]
