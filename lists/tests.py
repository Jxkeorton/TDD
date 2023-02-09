from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """
        1 create an HttpRequest object, which is what Django will see when a user’s browser asks for a page.
        2 pass it to our home_page view, which gives us a response.
        3 we extract the .content of the response....decode() to convert them into the string of HTML that’s being sent to the user.
        4 We want it to start with an <html> tag which gets closed at the end.
        5 <title> tag somewhere in the middle, with the words "To-Do lists" in it

        """
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

