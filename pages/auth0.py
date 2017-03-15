from selenium.webdriver.common.by import By

from pages.base import Base


class Auth0(Base):
    _login_with_ldap_button_locator = (By.CSS_SELECTOR, '.auth0-lock-ldap-button.auth0-lock-ldap-big-button')
    _ldap_email_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-email .auth0-lock-input')
    _ldap_password_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-password .auth0-lock-input')
    _login_button_locator = (By.CSS_SELECTOR, '.auth0-lock-submit')
    _login_with_email_button_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-button')
    _passwordless_email_field_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-pane .auth0-lock-input')
    _send_email_button_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-submit')

    def login_with_ldap(self, ldap_email, ldap_password):
        self.selenium.find_element(*self._login_with_ldap_button_locator).click()
        self.selenium.find_element(*self._ldap_email_field_locator).send_keys(ldap_email)
        self.selenium.find_element(*self._ldap_password_field_locator).send_keys(ldap_password)
        self.selenium.find_element(*self._login_button_locator).click()

    def login_with_email(self, email):
        self.wait_for_element_visible(*self._login_with_email_button_locator)
        self.selenium.find_element(*self._login_with_email_button_locator).click()
        self.selenium.find_element(*self._passwordless_email_field_locator).send_keys(email)
        self.selenium.find_element(*self._send_email_button_locator).click()
