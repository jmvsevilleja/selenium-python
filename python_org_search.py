from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_install as cdi

#from webdriverdownloader import ChromeDriverDownloader
#from webdriverdownloader import GeckoDriverDownloader

#cdd = ChromeDriverDownloader()
#cdd = GeckoDriverDownloader()
# cdd.download_and_install()

path = cdi.install(file_directory='./lib/', verbose=True,
                   chmod=True, overwrite=False, version=None)

driver = webdriver.Chrome(path)
#driver = webdriver.Firefox()

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
