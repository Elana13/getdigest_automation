from behave import *

from tests.acceptance.page_model.base_page import BasePage

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

