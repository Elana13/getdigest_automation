from tests.acceptance.page_model.base_page import BasePage


class ContactUsPageSuccess(BasePage):
    @property
    def url(self):
        return super(ContactUsPageSuccess, self) + '/en/contact?succeed=True'

    @property
    def title(self):
        return self.driver.find_element(*ContactUsPageSuccess.TITLE)



