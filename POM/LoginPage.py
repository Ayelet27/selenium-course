from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def nav_to(self):
        self.driver.get("http://petstore.octoperf.com/actions/Account.action?signonForm=")

    def enter_username(self, username):
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.NAME, "signon")
        login_button.click()

        # Get error message after failed login
    def get_actual_result_text(self):
        error_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid username or password')]"))
        )
        return error_message.text