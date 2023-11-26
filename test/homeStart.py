from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver (or choose another browser)
driver = webdriver.Chrome()

# Navigate to the local URL where the web application is running
driver.get(r"C:\Users\dell\Desktop\TechTidy final\TechTidy\home.html")

try:
    # Find the "Get Started" link using its text
    get_started_link = driver.find_element(By.LINK_TEXT, "Get Started")

    # Click on the link
    get_started_link.click()
    # back to home page
    home_link = driver.find_element(By.XPATH, "//a[contains(., 'Home')]")
    home_link.click()

    # Scroll to the "Read More" button
    read_more_button = driver.find_element(By.XPATH, "//a[contains(text(), 'read more')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", read_more_button)

    # Wait for the page to settle after scrolling
    time.sleep(2)

    # Wait for the "Read More" button to be clickable
    wait = WebDriverWait(driver, 10)
    read_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'read more')]")))

    # Click on the "Read More" button
    read_more_button.click()
    time.sleep(3)
    # Scroll down to the "Recycle Now" button using JavaScript
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for a moment to allow the page to settle after scrolling
    time.sleep(2)

    # Locate the "Recycle Now" button and click on it
    recycle_now_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Recycle Now')]")
    recycle_now_button.click()

    # Find the pincode input field and enter '560076'
    pincode_input = driver.find_element(By.ID, "pincode")
    pincode_input.send_keys("560076")

    # Wait for a moment to allow the input to be processed
    time.sleep(2)

    # Find and click the search button
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()
    time.sleep(2)

    driver.back()

    profile_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Profile"]'))
    )

    # Click the profile link
    profile_link.click()
    time.sleep(5)

    element = driver.find_element(By.XPATH, '//a[text()="Learn More"]')
    driver.execute_script("arguments[0].click();", element)

    print("Test passed")


except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Ensure the browser is closed even if an exception occurs
    driver.quit()

