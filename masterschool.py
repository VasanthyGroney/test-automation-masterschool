import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate a WebDriver Object
driver = webdriver.Chrome()

# Navigate to the Masterschool homepage
driver.get("https://masterschool.com")

# Request browser title
title = driver.title
print("Browser Title:", title)

# Use explicit wait to wait for the text box to be visible
text_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "my-text"))
)

# Take action after waiting for 2 seconds
text_box.send_keys("Selenium")

# Wait for 2 seconds before clicking the submit button
time.sleep(2)

# Find the submit button and click it
submit_button = driver.find_element(By.TAG_NAME, "button")
submit_button.click()

# Wait for the message to appear after the form is submitted
message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "message"))
)

# Print the message text
print("Message after submission:", message.text)

# End the session
driver.quit()