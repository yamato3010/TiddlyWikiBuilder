import os
import urllib.parse
import re

def decode_percent_encoded_in_html(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".html"):
            file_path = os.path.join(directory_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()

            # パーセントエンコーディングをデコード
            decoded_content = urllib.parse.unquote(html_content)

            # 特定のエンコーディングをデコードするための正規表現パターン
            # 例: %20 を スペース にデコードする
            decoded_content = re.sub(r'%20', ' ', decoded_content)

            # 他のエンコーディングも必要に応じて正規表現パターンを追加してください

            # デコードされた内容をファイルに書き込む
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(decoded_content)

            print(f"Decoded HTML file: {file_path}")

if __name__ == "__main__":
    target_directory = "./myfirstwiki/output/static"
    decode_percent_encoded_in_html(target_directory)
