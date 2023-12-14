from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_path = '/path/to/chromedriver'
driver = webdriver.Chrome()
driver.get('https://automationintesting.online/')
def test_case_001_Welcome_to_Restful_Booker_Platform(name, email, phone, subject, message):
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[5]/div[2]/form/div[1]/input'))
     .send_keys(name))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[5]/div[2]/form/div[2]/input'))
     .send_keys(email))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[5]/div[2]/form/div[3]/input"))
     .send_keys(phone))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[5]/div[2]/form/div[4]/input"))
     .send_keys(subject))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[5]/div[2]/form/div[5]/textarea"))
     .send_keys(message))
    (driver.find_element(By.ID, "submitContact")).click()
    driver.implicitly_wait(2)
    success_message = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[5]/div[2]/div/h2')
    driver.implicitly_wait(2)
    if "Zaid Javed" in success_message.text:
        print("Test Case 001: Passed")
    else:
        print("Test Case 001: Failed - Go to form.py [function: test_case_001_Welcome_to_Restful_Booker_Platform]")

def test_case_002_room_reservation(first_name, last_name, email, phone):
    driver.implicitly_wait(2)
    (driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[4]/div/div/div[3]/button')).click()
    driver.implicitly_wait(2)
    date = driver.find_element(By.XPATH,
                               '/html/body/div/div[2]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/button')
    start_date = driver.find_element(By.XPATH,
                                     '/html/body/div/div[2]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[4]/button')
    end_date = driver.find_element(By.XPATH,
                                   '/html/body/div/div[2]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[5]')
    driver.implicitly_wait(2)
    # time.sleep(2)
    actions = ActionChains(driver)
    actions.click_and_hold(date).move_to_element(start_date).perform()
    actions.move_to_element(end_date).perform()
    driver.implicitly_wait(2)
    time.sleep(2)
    ((driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[4]/div/div[2]/div[3]/div[1]/input')).send_keys(first_name))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[4]/div/div[2]/div[3]/div[2]/input')).send_keys(last_name))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[4]/div/div[2]/div[3]/div[3]/input")).send_keys(email))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[4]/div/div[2]/div[3]/div[4]/input")).send_keys(phone))
    driver.implicitly_wait(2)
    ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[4]/div/div[2]/div[3]/button[2]"))).click()
    driver.implicitly_wait(2)
    # time.sleep(1)
    try:
        success_message = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[1]/div[2]/h3')
        if "Booking Successful!" in success_message.text:
            driver.implicitly_wait(2)
            print("Test Case 002: Passed")
        else:
            print(
                "Test Case 002: Failed - Rooms did get reserved, Go to form.py [function: test_case_002_room_reservation]")
    except:
        print('Test Case 002: Failed - Rooms did not get reserved, Go to form.py [function: test_case_002_room_reservation]")')
