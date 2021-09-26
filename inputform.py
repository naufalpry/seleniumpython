from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
# browser = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")




time.sleep(3)
# driver.find_element_by_xpath("//input[@name='firstname']").send_keys("NAUFAL")
# driver.find_element_by_xpath("//input[@name='lastname']").send_keys("PRAYOGO")
# driver.find_element_by_id('sex-0').click()
# driver.find_element_by_id('exp-3').click()
# driver.find_element_by_id('datepicker').send_keys("26/09/2021")
# driver.find_element_by_id('profession-1').click()
# driver.find_element_by_id('tool-2').click()
scrol =  driver.find_element_by_id('continents')
driver.execute_script("arguments[0].scrollIntoView();",scrol)
time.sleep(2)
# driver.find_element_by_id('continents').click()
# select(driver.find_element_by_id('continents'))
# select.select_by_visible_text('Asia').click()
# driver.find_element_by_link_text("WebElement Commands").click()
# queues = Select(driver.find_element_by_id('selenium_commands'))
# queues.select_by_visible_text("WebElement Commands")
driver.find_element_by_id("photo").send_keys("naufalpry/Automation/selenium-python/1.png")
driver.find_element_by_xpath("//a[@href='https://github.com/stanfy/behave-rest/blob/master/features/conf.yaml']").click()
driver.find_element_by_id('submit').click()



