# Activity 18
# Alerts #1
# Using Selenium:

# Open a new browser to https://training-support.net/webelements/alerts
# Get the title of the page and print it to the console.
# Find the button to open a SIMPLE alert and click it.
# Switch the focus from the main window to the Alert box and get the text in it and print it.
# Close the alert once with OK.
# Close the browser.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, timeout=10)
    driver.get("https://training-support.net/webelements/alerts")
    print("Page title is: ", driver.title)
    driver.find_element(By.ID, "simple").click()
    simpleAlert = wait.until(EC.alert_is_present())
    alertText = simpleAlert.text
    print("Text in alert: " + alertText)
    simpleAlert.accept()
    print(driver.find_element(By.ID, "result").text)