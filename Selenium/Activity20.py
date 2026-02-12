# Open a new browser to https://training-support.net/webelements/alerts
# Get the title of the page and print it to the console.
# Find the button to open a PROMPT alert and click it.
# Switch the focus from the main window to the Alert box and get the text in it and print it.
# Type "Awesome!" into the prompt.
# Close the alert by clicking Ok.
# Close the browser.



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, timeout=10)
    driver.get("https://training-support.net/webelements/alerts")
    print("Page title is: ", driver.title)
    driver.find_element(By.ID, "prompt").click()
    promptAlert = wait.until(EC.alert_is_present())
    alertText = promptAlert.text
    print("Text in alert: " + alertText)
    promptAlert.send_keys("Awesome!")
    promptAlert.accept()
    print(driver.find_element(By.ID, "result").text)