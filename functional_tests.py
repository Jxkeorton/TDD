from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):

    """
    Tests are organised into classes, which inherit from unittest.TestCase.
    Any method whose name starts with test is a test method,
    SetUp and tearDown are special methods to start/stop browser,
    Use self.assertIn instead of just assert to make our test assertions.

    The if __name__ == '__main__' clause (that’s how a Python script checks if it’s been executed
    from the command line, rather than imported by another script). We call unittest.main(), 
    which launches the unittest test runner, which will automatically find test classes 
    and methods in the file and run them.
    """

    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\jakeo\Desktop\coding\Projects\TDD\geckodriver.exe', options=options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # she is invited to enter a to-do item straight away 

if __name__ == '__main__':  
    unittest.main()
