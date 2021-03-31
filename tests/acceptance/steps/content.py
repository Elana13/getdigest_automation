from behave import *
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.forbusiness_page import ForBusinessPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
#    title = context.driver.find_element(BasePageLocators.TITLE)
    assert page.title.is_displayed()


@step('The title is "(.*)"')  #we can use step everywhere
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content

@then("Banner is shown on 'For Business' page")
def step_impl(context):
    page = ForBusinessPage(context.driver)

    assert page.banner.is_displayed()



