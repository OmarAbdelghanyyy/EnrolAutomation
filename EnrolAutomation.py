from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def success():
    driver.implicitly_wait(10)
    driver.get("https://www.uocampus.uottawa.ca/psc/csprpr9www/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL"
               "?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=300268565&ENRL_REQUEST_ID=&INSTITUTION=UOTTA"
               "&STRM=2229")  # Fall 2022 shopping cart
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[10]/td["
                                  "2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/a/span/input").click()  # proceed button
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT").click()  # finish button
    driver.implicitly_wait(30)
    driver.get("https://www.uocampus.uottawa.ca/psc/csprpr9www/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL"
               "?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=300268565&ENRL_REQUEST_ID=&INSTITUTION=UOTTA"
               "&STRM=2229")  # Redirects to Add page Page
    time.sleep(0.5)
    driver.find_element(By.ID, "DERIVED_SSS_SCT_SSS_TERM_LINK").click()  # Change term
    time.sleep(0.5)
    driver.find_element(By.ID, "SSR_DUMMY_RECV1$sels$2$$0").click()  # Clicks winter 2023
    driver.find_element(By.ID, "DERIVED_SSS_SCT_SSR_PB_GO").click()  # Clicks continue
    time.sleep(0.5)
    driver.find_element(By.ID, "DERIVED_REGFRM1_LINK_ADD_ENRL$82$").click()  # Proceed to step 2 out of 3
    driver.find_element(By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT").click()  # Finish enrolling


def no_longer_waiting():
    return mat_1720w_status == fra_status == mat_1720a_status


s = Service(r'C:/Users/ahmed/Downloads/chromedriver_win32 (2)/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(
    "https://www.uocampus.uottawa.ca/psp/csprpr9www/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?languageCd=ENG")  # Enrol URL
driver.implicitly_wait(20)
name_box = driver.find_element(By.ID, "i0116")  # finds login text box
name_box.send_keys("oabde073@uottawa.ca")  # inputs login
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div["
                                                                      "1]/div/div/div/div/div[1]/div["
                                                                      "3]/div/div/div/div["
                                                                      "4]/div/div/div/div/input"))).click()  # First Next Button to proceed to password input page
password_box = driver.find_element(By.NAME, "passwd")  # finds password text box
password_box.send_keys("Om@1409003")  # inputs Password

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div["
                                                                      "1]/div/div/div/div/div/div[3]/div/div["
                                                                      "2]/div/div[4]/div["
                                                                      "2]/div/div/div/div/input"))).click()  # Second Next Button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/div/div/div[2]/div["
                                                                      "1]/div/div/div/div/div/div[3]/div/div["
                                                                      "2]/div/div[3]/div[2]/div/div/div["
                                                                      "2]/input"))).click()  # YES button after MFA authorization
driver.get("https://www.uocampus.uottawa.ca/psc/csprpr9www/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_LIST.GBL?Page"
           "=SSR_SSENRL_LIST&Action=A&ACAD_CAREER=CAR&EMPLID=300268565&ENRL_REQUEST_ID=&INSTITUTION=INST&STRM=TERM")  # Redirects to My Class Schedule Page

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div["
                                                                      "5]/table/tbody/tr/td/div/table/tbody/tr[4]/td["
                                                                      "2]/div/table/tbody/tr[2]/td/table/tbody/tr["
                                                                      "3]/td[1]/div/input"))).click()  # Fall 2022 Button

WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.NAME, "DERIVED_SSS_SCT_SSR_PB_GO"))).click()  # Continue Button
time.sleep(0.5)
fra_status = driver.find_element(By.ID, "STATUS$0").text
mat_1720a_status = driver.find_element(By.ID, "STATUS$1").text  # Sana Keita section
mat_1720w_status = driver.find_element(By.ID, "STATUS$2").text  # Joseph Khoury section

if (no_longer_waiting()==True):  # to be changed to if not (content.find("Waiting")) after getting of the waitlist of one of the classes
   success()
