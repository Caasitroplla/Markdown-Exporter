import markdown

def markdown_to_html(text: str) -> str:
    return markdown.markdown(text)

