from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_path = '/path/to/chromedriver'

driver = webdriver.Chrome()
driver.get('https://automationintesting.online/')

name = (driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[5]/div[2]/form/div[1]/input')
        .send_keys("Zaid Javed"))
driver.implicitly_wait(10)


email = (driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[5]/div[2]/form/div[2]/input').
         send_keys("memuzdak@gmail.com"))

driver.implicitly_wait(10)

phone = ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[5]/div[2]/form/div[3]/input")).
         send_keys("+923211234567"))
subject = ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[5]/div[2]/form/div[4]/input")).
           send_keys("Sending dummy data"))
message = ((driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[5]/div[2]/form/div[5]/textarea")).
           send_keys("I am testing the positive case in which I am writing more than 20 characters "))
(driver.find_element(By.ID, "submitContact")).click()

driver.implicitly_wait(10)

success_message = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[5]/div[2]/div/h2')
time.sleep(3)

if "Zaid Javed" in success_message.text:
    print("Test Case Pass")
else:
    print("Test Case Failed")

driver.quit()