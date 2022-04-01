from src.convertors import html_to_pdf, markdown_to_html

def main():
    text = '''
    # Programme
    Authors: Mrs Heskath, Mr Bridges
    '''
    html = markdown_to_html(text)
    html_to_pdf(html)

if __name__ == '__main__':
    main()

