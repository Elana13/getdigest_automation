from behave import *
from selenium import webdriver

from tests.acceptance.page_model.addon_page import AddonPage
from tests.acceptance.page_model.forbusiness_page import ForBusinessPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@given('User is on Homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('c:\\ChromeDriver\\chromedriver.exe')
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('User is on "Addon" page')
def step_impl(context):
    context.driver = webdriver.Chrome('c:\\ChromeDriver\\chromedriver.exe')
    page = AddonPage(context.driver)
    context.driver.get(page.url)

@given('User is on "ForBusiness" page')
def step_impl(context):
    context.driver = webdriver.Chrome('c:\\ChromeDriver\\chromedriver.exe')
    page = ForBusinessPage(context.driver)
    context.driver.get(page.url)

@then('User is on the "Addon" page')
def step_impl(context):
    expected_url = AddonPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('User is on the Homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url


