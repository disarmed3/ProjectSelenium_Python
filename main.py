from telnetlib import EC

import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://ekmechanes.com/")
    driver.maximize_window()
    yield driver
    # driver.quit()

def test_careers_link(driver):

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='We are hiring']"))).click()
    title = driver.title
    assert "Careers" in title, "Expected 'Careers' in page title"

def test_qa_engineer_link(driver):

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Junior/Mid-Level QA Engineer']"))).click()
    text = driver.page_source
    assert "Junior/Mid-Level QA Engineer" in text, "Expected 'Junior/Mid-Level QA Engineer' in page source"

def test_application_link(driver):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'fab-Card fab-Card--sizeFull fab-Card--withoutBottomGradient')]//span[contains(@class,'jss-f76')][normalize-space()='Apply for This Job']"))).click()
    text = driver.page_source
    assert "Apply for this Position" in text, "Expected 'Apply for this Position' in page source"

def test_fill_info(driver):
    name = "Anastasios"
    surname = "Athanasiadis"
    email = "t.athanasiadis.test@gmail.com"
    phone = "693*******"
    linkedin = "https://www.linkedin.com/in/aathanasiadis/"
    github = "https://github.com/disarmed3"

    driver.find_element(By.ID, "firstName").send_keys(name)
    driver.find_element(By.ID, "lastName").send_keys(surname)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "phone").send_keys(phone)
    driver.find_element(By.ID, "websiteUrl").send_keys(github)
    driver.find_element(By.ID, "linkedinUrl").send_keys(linkedin)

    driver.find_element(By.CLASS_NAME, "CandidateField__checkboxRequiredIndicator").click()