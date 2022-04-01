import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "../geckodriver.exe"


class TestTextCrudAppHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=PATH)
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Text Crud', self.driver.title)

    def test_page_heading_is_words(self):
        heading = self._find('heading').text
        self.assertEqual(heading, 'Words')

    def test_if_add_page_has_input_form(self):
        form = self._find('form')
        self.assertIsNotNone(form)

    def test_if_has_list_of_words(self):
        word_list = self._find('word-list')
        self.assertIsNotNone(word_list)
    
    def test_if_has_list_item(self):
        word = self._find('word')
        self.assertIsNotNone(word)

    def _find(self, val):
        return self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{val}"]')


if __name__ == '__main__':
    unittest.main()
