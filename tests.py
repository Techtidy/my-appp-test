from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import WebDriverException

try:
    # Use Chrome instead of Firefox
    with webdriver.Chrome() as driver:
        # Update the URL to your site
        driver.get("https://techtidy.github.io/my-app-dev/")
        
        # Locate the search input field and send the search query
        search_input = driver.find_element(By.NAME, "q")
        search_input.send_keys("cheese" + Keys.RETURN)
        
        # Use WebDriverWait for waiting for the presence of the search results container
        wait = WebDriverWait(driver, 10)
        wait.until(presence_of_element_located((By.XPATH, '//div[@id="rcnt"]')))
        
        # Find all the search result links using a more specific XPath
        results = driver.find_elements(By.XPATH, '//div[@class="tF2Cxc"]/div/a[@href]')
        
        # Print the search results
        for i, elem in enumerate(results):
            print(f'#{i + 1} {elem.text} ({elem.get_attribute("href")})')

except WebDriverException as e:
    print(f"WebDriverException: {e}")
