import time
import allure

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite('Widgets')
class TestWidgets:
    @allure.feature('Accordian Page')
    class TestAccordianPage:
        @allure.title('Проверка текста в виджетах')
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_content_text('first')
            second_title, second_content = accordian_page.check_content_text('second')
            third_title, third_content = accordian_page.check_content_text('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    @allure.feature('Autocomplete page')
    class TestAutoCompletePage:
        @allure.title('Проверка что автозаполнение заполнено')
        def test_fill_multi_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result

        @allure.title('Проверка удаления из мультиавтозаполенния')
        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        @allure.title('Проверка удаления из единственного автозаполнения')
        def test_fill_single_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, 'the added colors are missing in the input'

    @allure.feature('Date Picker Page')
    class TestDatePickerPage:
        @allure.title('Проверка даты изменения')
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'the date has not been changed'

        @allure.title('Проверка даты и времени изменения')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, 'the date and time have not been changed'

    @allure.feature('Slider Page')
    class TestSliderPage:
        @allure.title('Проверка перемещения ползунка')
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after, 'the slider value has not been changed'

    @allure.feature('Progress Bar Page')
    class TestProgressBarPage:
        @allure.title('Проверка измененного индикатора выполнения')
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after, after_all, before_reset = progress_bar.change_progress_bar_value()
            assert before != after != after_all != before_reset, 'the progress bar value has not been changed'

    @allure.feature('Test Tabs Page')
    class TestTabsPage:
        @allure.title('Проверка переключения вкладки')
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('What')
            origin_button, origin_content = tabs.check_tabs('Origin')
            use_button, use_content = tabs.check_tabs('Use')
            assert what_button == 'What' and what_content != 0
            assert origin_button == 'Origin' and origin_content != 0
            assert use_button == 'Use' and use_content != 0

    @allure.feature('Tool Tips')
    class TestToolTips:
        @allure.title('Проверка появления подсказки')
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button, field, contrary, section = tool_tips_page.check_tool_tips()
            assert button == 'You hovered over the Button', 'hover missing or incorrect content'
            assert field == 'You hovered over the text field', 'hover missing or incorrect content'
            assert contrary == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert section == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    @allure.feature('Menu Page')
    class TestMenu:
        @allure.title('Проверка всех пунктов меню')
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3']
