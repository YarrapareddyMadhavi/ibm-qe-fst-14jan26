# Using Selenium:

# Open a new browser to https://training-support.net/webelements/dynamic-controls
# Get the title of the page and print it to the console.
# On the page, perform:
# Find the checkbox on the page.
# Click the "Toggle Checkbox" button to remove the checkbox.
# Wait for the checkbox to disappear.
# Toggle the checkbox again.
# Wait for it appear and then select it.
# Close the browser.

# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, timeout=10)
    driver.get("https://training-support.net/webelements/dynamic-controls")
    print("Page title is: ", driver.title)
    checkbox = driver.find_element(By.ID, "checkbox")
    print("Checkbox is visible? ", checkbox.is_displayed())
    driver.find_element(By.XPATH, "//button[text()='Toggle Checkbox']").click()
    wait.until(EC.invisibility_of_element(checkbox))
    print("Checkbox is visible? ", checkbox.is_displayed())
    driver.find_element(By.XPATH, "//button[text()='Toggle Checkbox']").click()
    wait.until(EC.element_to_be_clickable(checkbox)).click()
    print("Checkbox is selected? ", checkbox.is_selected())
