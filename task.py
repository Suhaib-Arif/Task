from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

def select_options(district: str,  mandal: str, village: str):
    district_selected = False
    mandal_selected = False
    village_selected = False
    
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 100)

    driver.get("https://dharani.telangana.gov.in/knowLandStatus")
    wait.until(EC.element_to_be_selected, (By.NAME, "districtID"))

    time.sleep(10)
    district_selector = Select(wait.until(EC.presence_of_element_located((By.NAME, "districtID"))))
    for option in district_selector.options:
        if district in option.text:
            print(option.text)
            district_selected = True
            option.click()
            break

    if not district_selected:
        print("Not Found")
        return None
    
    time.sleep(10)
    mandal_selector = Select(wait.until(EC.presence_of_element_located((By.NAME, "mandalID"))))
    for option in mandal_selector.options:
        if mandal in option.text:
            mandal_selected = True
            print(option.text)
            option.click()
            break

    if not mandal_selected:
        return
    
    time.sleep(10)
    village_selector = Select(wait.until(EC.presence_of_element_located((By.NAME, "villageId"))))

    for option in village_selector.options:
        if village in option.text:
            village_selected = True
            print(option.text)
            option.click()
            break
    
    if not village_selected:
        return
    
    time.sleep(10)
    survey_selector = Select(wait.until(EC.presence_of_element_located((By.NAME, "surveyIdselect"))))

    return [option.text for option in survey_selector.options[1:]]


   

if __name__ == "__main__":
    
    district = input("Enter the district: ")
    mandal = input("Enter the mandal: ")
    village = input("Enter the village: ")
    
    survey_no = select_options(district, mandal, village)

    if survey_no is not None:
        for no in survey_no:
            print(no)