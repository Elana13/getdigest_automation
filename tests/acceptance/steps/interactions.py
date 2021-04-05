from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.contactus_page import ContactUsPage

use_step_matcher('re')


@when('User click "(.*)" item in menu')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.top_menu
    matching_links = []
    for l in links:
        if l.text == link_text:
            matching_links.append(l)

    # matching_links = [link for link in links if link.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('User enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = ContactUsPage(context.driver)
#    print(field_name)
    page.form_field(field_name).send_keys(content)


@when('User check agreement')
def step_impl(context):
    page = ContactUsPage(context.driver)
    page.agreement_checkbox.click()

@when('User check captcha')
def step_impl(context):
    page = ContactUsPage(context.driver)
    page.Swi
    page.captcha.click()


@when('User press "Submit" button')
def step_impl(context):
    page = ContactUsPage(context.driver)
    page.submit_button.click()