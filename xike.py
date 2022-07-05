import time

from selenium import webdriver
from selenium.webdriver.common.by import By



a = webdriver.Chrome()
a.get("https://noracora.com/")
a.find_element(By.XPATH, '//div[@class="relative group flex items-center"]').click()
a.find_element(By.XPATH, '//div[@class="inp-item"]//input[@name="email"]').send_keys("gengdian@chicv.com")
a.find_element(By.XPATH, '//div[@class="inp-item inp-password"]//input[@name="password"]').send_keys("111111")
a.find_element(By.XPATH, '//li[@class="login-item item"]//button[@type="submit"]').click()
time.sleep(3)
print(a.title)
