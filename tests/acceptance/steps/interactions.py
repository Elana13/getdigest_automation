from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.contactus_page import ContactUsPage

use_step_matcher('re')


@when('User click "(.*)" item in menu')
# "(.*)" regular expression which groups everything inside "" in scenario and passed into parameter
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.top_menu        # select all links on the page
    link = [l for l in links if l.text == link_text]

    if len(link) > 0:
        link[0].click()
    else:
        raise RuntimeError()

#   link = context.driver.find_element_by_css_selector(f'.menu a[href="/{menu_item}"]')

@when('User enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = ContactUsPage(context.driver)
    page.form_fields(field_name).send_keys(content)

@when('User check agreement')
def step_impl(context):
    page = ContactUsPage(context.driver)
    page.agreement_checkbox.click()

@when('User press "Submit" button')
def step_impl(context):
    page = ContactUsPage(context.driver)
    page.submit_button.click()