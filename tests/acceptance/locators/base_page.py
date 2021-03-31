from selenium.webdriver.common.by import By

class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'  #taple
    MENU_LINKS = By.CSS_SELECTOR, '#menu > li a'
