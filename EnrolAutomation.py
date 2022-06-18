from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service(r'C:\Users\ahmed\Downloads\chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.uocampus.uottawa.ca/psp/csprpr9www/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?languageCd=ENG")
name_box=driver.find_element(By.NAME,"loginfmt")
name_box.send_keys("oabde073@uottawa.ca")
first_next_button=driver.find_element(By.XPATH,"/html/body")
first_next_button.click()