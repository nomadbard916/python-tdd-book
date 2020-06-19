from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEquals(found.func, home_page)  # func here means "view function"

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")

        self.assertIn("<title>To-Do lists</Title>", html)
        self.assertTrue(html.endsWith("</html>"))
