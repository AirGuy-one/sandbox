from selenium import webdriver
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome()

try:
    driver.get("https://ya.ru/")
    logo = driver.find_element("tag name", "img")
    assert logo.is_displayed()
    print("Logo is displayed on the page.")
except WebDriverException as e:
    print("Error while running WebDriver:", e)
except AssertionError:
    print("Logo is not displayed on the page.")
finally:
    driver.quit()
