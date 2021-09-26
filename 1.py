from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.google.com") #This is a dummy website URL
elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "q")) #This is a dummy element