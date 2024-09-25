import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()

    cleaned_text = re.sub(r'<[^>]+>', '', html_content)

    cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write("\n".join(cleaned_lines))

