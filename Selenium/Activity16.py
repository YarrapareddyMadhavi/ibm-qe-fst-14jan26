# Using Selenium:

# Open a new browser to https://training-support.net/webelements/selects
# Get the title of the page and print it to the console.
# On the Single Select:
# Select the second option using the visible text.
# Select the third option using the index.
# Select the fourth option using the value.
# Get all the options and print them to the console.
# Close the browse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


with webdriver.Firefox() as driver:
  
    driver.get("https://training-support.net/webelements/selects")
   
    print("Page title is: ", driver.title)
    dropdown = driver.find_element(By.CSS_SELECTOR, "select.h-10")
    singleSelect = Select(dropdown)
    singleSelect.select_by_visible_text("Two")
    print("Second option: " + singleSelect.first_selected_option.text)
    singleSelect.select_by_index(3)
 
    print("Third option: " + singleSelect.first_selected_option.text)
    singleSelect.select_by_value("four")
    print("Fourth option: " + singleSelect.first_selected_option.text)
    allOptions = singleSelect.options
    print("Options in the dropdown: ")
    for option in allOptions: 
        print(option.text)