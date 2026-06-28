from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from LoginData import LoginData
from JpetScripts import JpetScripts

# Browser configuration
options = Options()
options.binary_location = "/home/codespace/.cache/selenium/chrome/linux64/149.0.7827.115/chrome"
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(
    "/home/codespace/.cache/selenium/chromedriver/linux64/149.0.7827.115/chromedriver"
)

driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)

scripts = JpetScripts(driver)

expected_error = "Invalid username or password"
expected_welcome = "Welcome"

# Run login test scenarios
scripts.invalid_login("wrong_user1", LoginData.valid_password1, expected_error)
scripts.invalid_login("wrong_user2", LoginData.valid_password2, expected_error)

scripts.invalid_login(LoginData.valid_username1, "wrong_password1", expected_error)
scripts.invalid_login(LoginData.valid_username2, "wrong_password2", expected_error)

scripts.invalid_login("wrong_user1", "wrong_password1", expected_error)
scripts.invalid_login("wrong_user2", "wrong_password2", expected_error)

scripts.valid_login(LoginData.valid_username1, LoginData.valid_password1, expected_welcome)
scripts.valid_login(LoginData.valid_username2, LoginData.valid_password2, expected_welcome)

driver.quit()