import os
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER_INPUT).send_keys(person.mobile_number)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(person.current_address)
        self.element_is_visible(self.locators.SUBJECTS).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.PICTURE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON_CLICK).click()
        return person

    def for_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
