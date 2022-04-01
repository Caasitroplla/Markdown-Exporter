import unittest

from src.convertors import markdown_to_html


class test_markdown_to_html(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(markdown_to_html('# heading'), '<h1>heading</h1>')
        self.assertEqual(markdown_to_html('## heading 2'), '<h2>heading 2</h2>')
        self.assertEqual(markdown_to_html('### heading 3'), '<h3>heading 3</h3>')

    def test_bold(self):
        self.assertEqual(markdown_to_html('**bold**'), '<p><strong>bold</strong></p>')

    
