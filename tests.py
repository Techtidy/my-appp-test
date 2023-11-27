from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import WebDriverException

try:
    with webdriver.Chrome() as driver:
        driver.get("https://techtidy.github.io/my-app-dev/")
        button = driver.find_element(By.ID, "myButton")
        button.click()
        wait = WebDriverWait(driver, 10)
        wait.until(presence_of_element_located((By.XPATH, '//div[@id="myElementId"]')))
        links = driver.find_elements(By.TAG_NAME, 'a')
        for i, link in enumerate(links):
            print(f'#{i + 1} Text: {link.text}, Href: {link.get_attribute("href")}')

except WebDriverException as e:
    print(f"WebDriverException: {e}")
