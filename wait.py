from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_install as cdi
from selenium.common.exceptions import TimeoutException


path = cdi.install(file_directory='./lib/', verbose=False,
                   chmod=True, overwrite=False, version=None)

driver = webdriver.Chrome(path)

driver.get("http://www.yahoo.com")


try:
    # tells WebDriver to poll the DOM for a certain amount
    driver.implicitly_wait(10)  # seconds
    myDynamicElement = driver.find_element_by_id("myDynamicElement")

    # WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully.
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(
    #    EC.presence_of_element_located((By.ID, "myDynamicElement"))
    # )
except TimeoutException as error:
    print(error)
    print('The TimeoutException() function was executed')
finally:
    driver.quit()
