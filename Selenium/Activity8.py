# from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Firefox() as driver:
#     actions = ActionChains(driver)
#     driver.get("https://training-support.net/webelements/mouse-events")
#     print("Page title is: ", driver.title)
#     button = driver.find_element(By.XPATH, "//button[@id='button']")
#     actions.double_click(button).perform()
#     print("Button text after double click: ", button.text)
#     actions.context_click(button).perform()
#     print("Button text after right click: ", button.text)



# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# with webdriver.Firefox() as driver:
#     actions = ActionChains(driver)
#     driver.get("https://training-support.net/webelements/mouse-events")
#     print("Page title is: ", driver.title)
#     cargoLock = driver.find_element(By.XPATH, "//h1[text()='Cargo.lock']")
#     cargoToml = driver.find_element(By.XPATH, "//h1[text()='Cargo.toml']")
#     srcButton = driver.find_element(By.XPATH, "//h1[text()='src']")
#     targetButton = driver.find_element(By.XPATH, "//h1[text()='target']")
#     actions.click(cargoLock).pause(1).move_to_element(cargoToml).pause(5).click(cargoToml).perform()
#     actionMessage = driver.find_element(By.ID, "result").text
#     print(actionMessage)
#     actions.double_click(srcButton).pause(3).pause(5).context_click(targetButton).pause(3).perform()
#     actions.click(driver.find_element(By.XPATH, ("//div[@id='menu']/div/ul/li[1]"))).pause(5).perform()
#     actionMessage = driver.find_element(By.ID, "result").text
#     print(actionMessage)

               
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:
    actions = ActionChains(driver)

    driver.get("https://training-support.net/webelements/mouse-events")
    print("Page title is: ", driver.title)

    cargoLock = driver.find_element(By.XPATH, "//h1[text()='Cargo.lock']")
    cargoToml = driver.find_element(By.XPATH, "//h1[text()='Cargo.toml']")
    srcButton = driver.find_element(By.XPATH, "//h1[text()='src']")
    targetButton = driver.find_element(By.XPATH, "//h1[text()='target']")

    actions.click(cargoLock).pause(1)\
           .move_to_element(cargoToml).pause(1)\
           .click(cargoToml).perform()

    actionMessage = driver.find_element(By.ID, "result").text
    print(actionMessage)

    actions.double_click(srcButton).perform()
    actions.context_click(targetButton).perform()

    wait = WebDriverWait(driver, 10)
    menu_item = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='menu']//li[1]"))
    )

    menu_item.click()

    actionMessage = driver.find_element(By.ID, "result").text
    print(actionMessage)
