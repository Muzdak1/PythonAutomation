from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from form import test_case_001_Welcome_to_Restful_Booker_Platform,test_case_002_room_reservation

if __name__ == "__main__":
    test_case_001_Welcome_to_Restful_Booker_Platform("Zaid Javed", "memuzdak@gmail.com",
                                                               "+923211234567", "Sending dummy data",
                                                               "I am testing the positive case in which I am writing "
                                                               "more than 20 characters ")
    time.sleep(2)
    test_case_002_room_reservation("Zaid", "Javed",
                                  "memuzdak@gmail.com", "+923211234567")