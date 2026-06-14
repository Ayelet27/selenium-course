from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def test_random_number():
    options = Options()
    options.binary_location = "/home/codespace/.cache/selenium/chrome/linux64/149.0.7827.115/chrome"

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(
        "/home/codespace/.cache/selenium/chromedriver/linux64/149.0.7827.115/chromedriver"
    )

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.calculator.net/random-number-generator.html")

    lower_limit = driver.find_element(By.NAME, "slower")
    lower_limit.send_keys("100")

    upper_limit = driver.find_element(By.NAME, "supper")
    upper_limit.send_keys("500")

    generate_button = driver.find_element(By.NAME, "x")
    generate_button.click()