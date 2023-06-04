import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def upload():
    driver = uc.Chrome()

    driver.get("https://images.google.com/")

    driver.implicitly_wait(5)

    driver.find_element(By.ID, "L2AGLb").click()

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[aria-label="Zoeken op afbeelding"]').click()
    driver.implicitly_wait(5)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
        r"C:\Users\j\PycharmProjects\vinylrecognition\albums\Queen.jpg")
    driver.implicitly_wait(5)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "wNPKTe").click()
    time.sleep(5)

    # Switch to the new tab
    new_tab_handle = driver.window_handles[-1]
    driver.switch_to.window(new_tab_handle)

    # Perform actions in the new tab
    record = driver.find_element(By.CLASS_NAME, 'SDkEP').text
    print(record)

    # Close the previous tab
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    time.sleep(20)
    driver.get("https://www.discogs.com/")
    time.sleep(50)

    driver.quit()

upload()