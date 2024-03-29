import random
import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from generator.generator import generator_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    ProgressBarPageLocators, SliderPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step('Проверка текста в виджетах')
    def check_content_text(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD}
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step('заполнение окошка множеством цветов')
    def fill_input_multi(self):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('удаление из окошка')
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step('проверка цвета в мультизаполнении')
    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('проверка удаления')
    def check_remove(self):
        remove_list = self.element_is_visible(self.locators.MULTI_DELETE_ALL)
        remove_list.click()
        count_value_before = self.element_is_visible(self.locators.MULTI_VALUE)
        return count_value_before

    @allure.step('заполнение одиночного ввода автозаполнения')
    def fill_input_single(self):
        color = random.sample(next(generator_color()).color_name, k=1)
        input_singe = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_singe.send_keys(color)
        input_singe.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('проверка цвета в одиночном автозаполнении')
    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_CONTAINER)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('дата изменения')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('изменения выбранной даты и времени')
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        time.sleep(2)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('выбираем дату по тексту')
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('выбрать элементы даты из списка')
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('изменения значения ползунка')
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.INPUT_SLIDER).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step('изменения значения индикатора выполнения')
    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 4))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button.click()
        time.sleep(11)
        value_after_all_progress = self.element_is_present(self.locators.PROGRESS_BAR_VALUE_ALL).text
        self.element_is_visible(self.locators.PROGRESS_BAR_RESET).click()
        value_before_reset = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after, value_after_all_progress, value_before_reset


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('проверка вкладок')
    def check_tabs(self, new_tab):
        tabs = {'What':
                    {'title': self.locators.TABS_WHAT_BUTTON,
                     'content': self.locators.TABS_WHAT_TEXT},
                'Origin':
                    {'title': self.locators.TABS_ORIGIN_BUTTON,
                     'content': self.locators.TABS_ORIGIN_TEXT},
                'Use':
                    {'title': self.locators.TABS_USE_BUTTON,
                     'content': self.locators.TABS_USE_TEXT}
                }

        button = self.element_is_visible(tabs[new_tab]['title'])
        button.click()
        content = self.element_is_visible(tabs[new_tab]['content']).text
        return button.text, len(content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step('получения текста из всплывающих подсказок')
    def get_text_from_tool_tips(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        time.sleep(0.5)
        self.element_is_visible(wait_element)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS).text
        return tool_tip_text

    @allure.step('проверка подсказку')
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.HOVER_BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,
                                                              self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('проверка пункт меню')
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data