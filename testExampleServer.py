import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonCovidSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_corona_virus(self):
        driver = self.driver
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("Coronavirus")
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
       self.driver.refresh()

if __name__ == "__name__":
    unittest.main()
