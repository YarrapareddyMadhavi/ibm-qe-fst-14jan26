    # Using Selenium:

    # Open a new browser to https://training-support.net/webelements/drag-drop
    # Get the title of the page and print it to the console.
    # On the page, perform:
    # Find the ball and simulate a click and drag to move it into "Dropzone 1".
    # Verify that the ball has entered Dropzone 1.
    # Once verified, move the ball into "Dropzone 2".
    # Verify that the ball has entered Dropzone 2.
    # Close the browser.

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By

# with webdriver.Firefox() as driver:
#     actions = ActionChains(driver)

#     driver.get("https://training-support.net/webelements/drag-drop")
#     print("Page title is: ", driver.title)

#     ball = driver.find_element(By.ID, "draggable")
#     dropzone1 = driver.find_element(By.ID, "droppable")
#     dropzone2 = driver.find_element(By.ID, "droppable2")

#     actions.drag_and_drop(ball, dropzone1).perform()
#     dropzone1Text = dropzone1.find_element(By.TAG_NAME, "p").text
#     print("Dropzone 1 Text: ", dropzone1Text)

#     actions.drag_and_drop(ball, dropzone2).perform()
#     dropzone2Text = dropzone2.find_element(By.TAG_NAME, "p").text
#     print("Dropzone 2 Text: ", dropzone2Text)



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Firefox() as driver:
    actions = ActionChains(driver)
    driver.get("https://training-support.net/webelements/drag-drop")
    print("Page title is: ", driver.title)
    football = driver.find_element(By.ID, "ball")
    dropzone1 = driver.find_element(By.ID, "dropzone1")
    dropzone2 = driver.find_element(By.ID, "dropzone2")
    actions.click_and_hold(football).move_to_element(dropzone1).pause(3).release().perform()
    if(dropzone1.find_element(By.CLASS_NAME, "dropzone-text").text == "Dropped!"):
        print("Ball was dropped in Dropzone 1")
    actions.drag_and_drop(football, dropzone2).pause(3).perform()
    if(dropzone2.find_element(By.CLASS_NAME, "dropzone-text").text == "Dropped!"):
        print("Ball was dropped in Dropzone 2")