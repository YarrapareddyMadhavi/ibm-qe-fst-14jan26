
# Using Selenium:

# Open the training support site. (https://training-support.net)

# Print the title of the page

# Click the about us button

# Print the title of the new page

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Firefox() as driver:
 
    driver.get("https://training-support.net/")

  
    print("Page title is: ", driver.title)

    
    driver.find_element(By.LINK_TEXT, "About Us").click()

  
    print("New page title is: ", driver.title)