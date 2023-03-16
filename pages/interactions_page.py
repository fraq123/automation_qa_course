import random
import time
import allure
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step('получения сортируемых элементов')
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    @allure.step('изменения порядка списка')
    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_present(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    @allure.step('изменения порядка сетки')
    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        grid_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_present(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        grid_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return grid_before, grid_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    @allure.step('нажатие на выбранный элемент')
    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step('выбрать элемент списка')
    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    @allure.step('выбрать элемент сетки')
    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.LIST_GRID)
        active_element = self.element_is_visible(self.locators.LIST_GRID_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.step('получения пикселей по ширине и высоте')
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('получения максимального и минимального размера')
    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('поле изменения размера')
    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('изменить размер с изменяемым размером')
    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), random.randint(
            1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), random.randint(
            -200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    @allure.step('удалить простой div')
    def drop_simple(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('принять или отказать div')
    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable = self.element_is_visible(self.locators.ACCEPTABLE)
        no_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(no_acceptable, drop_here)
        drop_rext_not_accept = drop_here.text
        self.action_drag_and_drop_to_element(acceptable, drop_here)
        return drop_rext_not_accept, drop_here.text

    @allure.step('закрытие всех элементов благодаря div')
    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_me = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_me, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_me, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    @allure.step('перетащить div обратно')
    def drop_revert_draggable(self, type_drag):
        drags = {
            'will':
                {'revert': self.locators.WILL_REVERT, },
            'not_will':
                {'revert': self.locators.NOT_REVERT},
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        will_revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_move, position_after_revert


class DragabblePage(BasePage):
    locators = DragabblePageLocators()

    @allure.step('получение позиции до и после')
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('простое перетаскивание')
    def simple_dra_box(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_div)
        return before_position, after_position

    @allure.step('перетаскивание по x и y')
    def axis_restricted_box(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED).click()
        only_x = self.element_is_visible(self.locators.ONLY_X)
        only_y = self.element_is_visible(self.locators.ONLY_Y)
        before_position_x, after_position_x = self.get_before_and_after_position(only_x)
        before_position_y, after_position_y = self.get_before_and_after_position(only_y)
        return before_position_x, after_position_x, before_position_x, before_position_y


