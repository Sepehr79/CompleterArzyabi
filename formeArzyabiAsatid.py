"""
@author: kia
@edited for kashanu ac: mrunderline
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

userName = os.getenv("USER")
password = os.getenv("PASSWORD")
salary = os.getenv("SALARY")

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

def get_teachers():
	driver.get('https://pooya.kashanu.ac.ir/nazar/stu_portal/SelectLessons.php')
	return driver.find_elements_by_tag_name("tr")

def login():
	url = 'https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php'
	driver.get(url)
	driver.find_element_by_id('UserID').send_keys(userName)
	driver.find_element_by_id('DummyVar').send_keys(password)
	driver.find_element_by_xpath(".//input[@type='submit']").click()
	print("loged in")

login()
teachers_count = len(get_teachers())
verify = 2

while verify < teachers_count:
	teachers = get_teachers()
	teachers[verify].click()

	for select in driver.find_elements_by_tag_name('select'):
		select = Select(select)
		select.select_by_value(salary)
	driver.find_element_by_id("FSubmit").click()
	driver.switch_to_alert().accept()
	print 'teacher {} verified!'.format(verify)
	verify += 1

print 'finished! all teachers verified!'
print '>>> by: @mrunderline <<<'