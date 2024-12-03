from selenium import webdriver
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome()

try:
    driver.get("https://yandex.ru/weather")
    temperature = driver.find_element("xpath", '//span[contains(@class, "temp__value")]')
    assert temperature.is_displayed()
    print("Current temperature is displayed on the page.")
except WebDriverException as e:
    print("Error while running WebDriver:", e)
except AssertionError:
    print("Current temperature is not displayed on the page.")
finally:
    driver.quit()
