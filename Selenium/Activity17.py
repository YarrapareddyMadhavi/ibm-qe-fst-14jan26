# Open a new browser to https://training-support.net/webelements/selects
# Get the title of the page and print it to the console.
# On the Multi Select:
# Select the "HTML" option using the visible text.
# Select the 4th, 5th and 6th options using the index.
# Select the "Node" option using the value.
# Deselect the 5th option using index.
# Close the browser.


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# with webdriver.Firefox() as driver:
  
#     driver.get("https://training-support.net/webelements/selects")
   
#     print("Page title is: ", driver.title)
#     dropdown = driver.find_element(By.CSS_SELECTOR, "select.h-10:nth-child(4)")
#     multiSelect = Select(dropdown)
#     multiSelect.select_by_visible_text("HTML")
#     print("Selected option: " + multiSelect.first_selected_option.text)
#     multiSelect.select_by_index(3)
#     print("Selected option: " + multiSelect.first_selected_option.text)
#     multiSelect.select_by_index(4)
#     print("Selected option: " + multiSelect.first_selected_option.text)
#     multiSelect.select_by_index(5)
#     print("Selected option: " + multiSelect.first_selected_option.text)
#     multiSelect.select_by_value("node")
#     print("Selected option: " + multiSelect.first_selected_option.text)
#     multiSelect.deselect_by_index(4)
#     print("Deselected option at index 4")


# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Start the Driver
with webdriver.Firefox() as driver:
    # Navigate to the URL
    driver.get("https://training-support.net/webelements/selects")
    # Print the title of the page
    print("Page title is: ", driver.title)

    # Find the dropdown
    selectElement = driver.find_element(By.CSS_SELECTOR, "select.h-80")
    # Pass the WebElement to the Select object
    multiSelect = Select(selectElement)

    # Select "HTML" using visible text
    multiSelect.select_by_visible_text("HTML")
    # Select 4th, 5th, and 6th index options
    for i in range(3, 5):
        multiSelect.select_by_index(i)
    # Select "Node" using value attribute
    multiSelect.select_by_value("nodejs")
    # Print the selected options
    selectedOptions = multiSelect.all_selected_options
    print("Selected options are: ")
    for option in selectedOptions:
        print(option.text)

    # Deselect the 5th index option
    multiSelect.deselect_by_index(4)
    # Print the selected options
    selectedOptions = multiSelect.all_selected_options
    print("Selected options are: ")
    for option in selectedOptions:
        print(option.text)