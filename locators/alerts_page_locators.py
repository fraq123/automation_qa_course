from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TITLE_NEW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    SEE_ALERT = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    ALERT_BUTTON_5SEC = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    ALERT_BUTTON_OK = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    ALERT_BUTTON_SEND = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_ALERT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


