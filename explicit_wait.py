from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_install as cdi
from selenium.webdriver.common.by import By

path = cdi.install(file_directory='./lib/', verbose=False,
                   chmod=True, overwrite=False, version=None)

driver = webdriver.Chrome(path)

driver.get("http://google.com")
delay = 3  # seconds
try:
    WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, 'hplogo')))
    print("Page is ready!")
finally:
    print("Loading took too much time!")
