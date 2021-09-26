from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time
# browser = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

time.sleep(1)
driver.find_element_by_xpath("//input[@name='firstname']").send_keys("NAUFAL")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys("PRAYOGO")
driver.find_element_by_id('sex-0').click()
driver.find_element_by_id('exp-3').click()
driver.find_element_by_id('datepicker').send_keys("26/09/2021")
driver.find_element_by_id('profession-1').click()
driver.find_element_by_id('tool-2').click()
scrol =  driver.find_element_by_id('continents')
driver.execute_script("arguments[0].scrollIntoView();",scrol)
time.sleep(2)
contien=driver.find_element(By.ID,"continents")
contiens=Select(contien)
contiens.select_by_visible_text("Asia")
time.sleep(1)
driver.find_element_by_xpath("//select[@id='selenium_commands']//option[2]").click()
time.sleep(1)
driver.find_element_by_id("photo").send_keys("/Users/naufalpry/Automation/selenium-python/1.PNG")
driver.find_element_by_xpath("//a[@href='https://github.com/stanfy/behave-rest/blob/master/features/conf.yaml']").click()
# driver.find_element_by_id('submit').click()
driver.close();

