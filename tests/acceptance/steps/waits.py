from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.for_business import ForBusinessPageLocators

use_step_matcher('re')

@given('User is waiting for the banner to load')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_elements_located(ForBusinessPageLocators.BANNER)
    )