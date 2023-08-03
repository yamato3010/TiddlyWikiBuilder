import os
import re

def add_text_after_body(html_file, text_to_add):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # bodyタグの直後にテキストを追加
    modified_content = re.sub(r'(<body.*?>)', r'\1\n<p>{}</p>'.format(text_to_add), content)

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)

def process_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                base_name = os.path.basename(file_path)
                filename, _ = os.path.splitext(base_name)
                text_to_add = '<p style="margin-left: 10px;">このページは<a href="https://yamato3010.github.io/wiki">大和ノ求聞史Wiki</a>の静的バージョンです。記事の内容が最新でない可能性があります。動的版は<a href="https://yamato3010.github.io/wiki#' + filename + '">こちら</a></p>'
                add_text_after_body(file_path, text_to_add)
                

if __name__ == "__main__":
    directory_path = "./myfirstwiki/output/static"  # ディレクトリのパスを指定してください
    text_to_add = '<p style="margin-left: 10px;">このページは<a href="https://yamato3010.github.io/wiki">大和ノ求聞史Wiki</a>の静的バージョンです。記事の内容が最新でない可能性があります。</p>'

    process_html_files(directory_path)
