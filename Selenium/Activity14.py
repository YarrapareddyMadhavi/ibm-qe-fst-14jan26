# Open a new browser to https://training-support.net/webelements/tables
# Get the title of the page and print it to the console.
# Using xpaths on the table:
# Find the number of rows and columns in the table and print them.
# Find and print the Book Name in the 5th row.
# Click the header of the Price column to sort it in ascending order.
# Find and print the Book Name in the 5th row again.
# Close the browser.


# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


with webdriver.Firefox() as driver:

    wait = WebDriverWait(driver, timeout=10)
    driver.get("https://training-support.net/webelements/tables")
    print("Page title is: ", driver.title)
    cols = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-auto')]/thead/tr/th")
    print("Number of columns: ", len(cols))
    rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr")
    print("Number of rows: ", len(rows))
    cellValue = driver.find_element(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr[5]/td[2]")
    print("Book name before sorting: ", cellValue.text)
    driver.find_element(By.XPATH, "//table[contains(@class, 'table-auto')]/thead/tr/th[5]").click()
    cellValue = driver.find_element(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr[5]/td[2]")
    print("Book Name after sorting: ", cellValue.text)