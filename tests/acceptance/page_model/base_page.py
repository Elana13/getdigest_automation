from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://dev.getdigest.com'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def top_menu(self):
        return self.driver.find_element(*BasePageLocators.MENU_LINKS)
