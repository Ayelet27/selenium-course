from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Get welcome message after successful login
    def get_welcome_text(self):
        welcome = self.wait.until(
            EC.visibility_of_element_located((By.ID, "WelcomeContent"))
        )
        return welcome.text

    def sign_out(self):
        sign_out_link = self.driver.find_element(By.LINK_TEXT, "Sign Out")
        sign_out_link.click()