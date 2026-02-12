
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("https://training-support.net/webelements/keyboard-events")

# print("Page title is:", driver.title)

# input_field = driver.find_element(By.ID, "inputField")
# input_field.send_keys("Hello Selenium")

# message = driver.find_element(By.ID, "input-result").text
# print("Message on page:", message)

# driver.close()



from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


with webdriver.Firefox() as driver:
  
    actions = ActionChains(driver)
 
    driver.get("https://training-support.net/webelements/keyboard-events")

  
    print("Page title is: ", driver.title)

 
    actions.send_keys("This is coming from Selenium").send_keys(Keys.RETURN).perform()
  
    pageText = driver.find_element(By.XPATH, "/html/body/div/main/div/div/div/div/div[2]/h1").text
    print(pageText)
