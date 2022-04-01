import unittest
from selenium import webdriver

PATH = "../geckodriver.exe"


class TestTextCrudApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=PATH)
        self.driver.get('https://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Text Crud', self.driver.title)


if __name__ == '__main__':
    unittest.main()
