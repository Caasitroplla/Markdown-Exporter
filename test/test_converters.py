import unittest
try:
    from convertors import markdown_to_html
except ModuleNotFoundError:
    from src.convertors import markdown_to_html


class test_markdown_to_html(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(markdown_to_html('# heading'), '<h1> heading </h1>')