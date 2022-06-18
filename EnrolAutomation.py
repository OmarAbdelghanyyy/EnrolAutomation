from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
s=Service(r'C:\Users\ahmed\Downloads\chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.uocampus.uottawa.ca/psp/csprpr9www/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?languageCd=ENG")
name_box=driver.find_element(By.NAME,"loginfmt")
name_box.send_keys(UNIVERSITY-EMAIL)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input"))).click()
password_box=driver.find_element(By.NAME,"passwd")
password_box.send_keys(PASSWORD)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input"))).click()
