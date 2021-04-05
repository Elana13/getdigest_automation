from selenium.webdriver.common.by import By

from tests.acceptance.locators.contactus_page import ContactUsPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ContactUsPage(BasePage):
    @property
    def url(self):
        return super(ContactUsPage, self).url + '/en/contact'

    @property
    def form(self):          #whole form
        return self.driver.find_element(*ContactUsPageLocators.CONTACT_FORM)

    def form_field(self, name):        #access to every form field by DOM name property; element should be a child of form!
        return self.form.find_element(By.NAME, name)    #possible to find by id as well

    @property
    def submit_button(self):
        return self.driver.find_element(*ContactUsPageLocators.SUBMIT_BUTTON)

    @property
    def agreement_checkbox(self):
        return self.driver.find_element(*ContactUsPageLocators.AGREEMENT_CHECKBOX)

    @property
    def captcha(self):
        return self.driver.find_element(*ContactUsPageLocators.CAPTCHA)

