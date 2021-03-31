from tests.acceptance.locators.for_business import ForBusinessPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ForBusinessPage(BasePage):
    @property
    def url(self):
        return super(ForBusinessPage, self).url + '/en/gd-for-business'

    @property
    def banner(self):
        return self.driver.find_element(*ForBusinessPageLocators.BANNER)
