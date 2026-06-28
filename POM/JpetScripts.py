from LoginPage import LoginPage
from MainPage import MainPage


class JpetScripts:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)

# Run invalid login scenario
    def invalid_login(self, username, password, expected_result):
        print("Running Invalid Login Test")
        print("Username:", username)
        print("Expected Result:", expected_result)

        self.login_page.nav_to()
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()

        actual_result = self.login_page.get_actual_result_text()
        print("Actual Result:", actual_result)

        assert expected_result in actual_result, \
            f"FAIL: Expected '{expected_result}' but got '{actual_result}'"

        print("Status: PASS")
        print("-----------------------------------")
        
# Run valid login scenario
    def valid_login(self, username, password, expected_result):
        print("Running Valid Login Test")
        print("Username:", username)
        print("Expected Result:", expected_result)

        self.login_page.nav_to()
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()

        actual_result = self.main_page.get_welcome_text()
        print("Actual Result:", actual_result)

        assert expected_result in actual_result, \
            f"FAIL: Expected '{expected_result}' but got '{actual_result}'"

        print("Status: PASS")
        print("-----------------------------------")

        self.main_page.sign_out()