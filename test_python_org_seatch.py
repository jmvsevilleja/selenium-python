import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_install as cdi


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        path = cdi.install(file_directory='./lib/', verbose=True,
                           chmod=True, overwrite=False, version=None)
        self.driver = webdriver.Chrome(path)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
