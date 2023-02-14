from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        """
        1 send_keys, which is Selenium’s way of typing into input elements
        2 The Keys class (don’t forget to import it) lets us send special keys like Enter
        3 The time.sleep is there to make sure the browser has finished loading before we make any assertions about the new page

        """

        # she is invited to enter a to-do item straight away 
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # The page updates again, and now shows both items on her list
        self.fail('Finish the test!')

