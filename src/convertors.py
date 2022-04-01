import markdown
import pdfkit
import sys

def markdown_to_html(text: str) -> str:
    return markdown.markdown(text)

def html_to_pdf(html: str):
    # change the directory where th pdf will be saved
    # sys.path.insert('') -- needs changing
    pdfkit.from_string(html, 'out.pdf')
    