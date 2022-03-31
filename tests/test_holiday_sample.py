from pyparsing import common_html_entity
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)



driver.get('https://loan-holidays-landing-test.kube.aebank.lan/')
driver.maximize_window()

searchBox = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-card/mat-card-content/div/app-phone/form/fieldset/div/mat-form-field[1]/div/div[1]/div[3]/input")
searchBox.send_keys('9963176826')

getSmsCodeButton = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-card/mat-card-content/div/app-phone/form/fieldset/div/button").click()

#driver.quit()

