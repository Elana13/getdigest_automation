from selenium.webdriver.common.by import By


class ContactUsPageLocators:
    CONTACT_FORM = By.CLASS_NAME, 'contact-form'
    USERNAME_FIELD = By.ID, 'Contact_Username'
    EMAIL_FIELD = By.ID, 'Contact_Email'
    SUBJECT_FIELD = By.ID, 'Contact_Subject'
    MESSAGE_FIELD = By.ID, 'Contact_Comment'
    AGREEMENT_CHECKBOX = By.ID, 'Contact_Agreement'
    SUBMIT_BUTTON = By.TAG_NAME, 'button'

