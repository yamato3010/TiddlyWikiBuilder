import os
import urllib.parse

def decode_percent_encoded_filenames(directory_path):
    for filename in os.listdir(directory_path):
        encoded_filename = urllib.parse.unquote(filename)
        decoded_filename = encoded_filename.replace('%20', ' ')  # スペースの復元
        decoded_filename = decoded_filename.replace('%2F', '/')  # スラッシュの復元
        # 他のエンコーディングも必要に応じて追加してください
        new_filepath = os.path.join(directory_path, decoded_filename)

        # ファイル名が変更されている場合はリネームする
        if filename != decoded_filename:
            os.rename(os.path.join(directory_path, filename), new_filepath)

        print(f"Decoded: {filename} -> {decoded_filename}")

if __name__ == "__main__":
    target_directory = "./myfirstwiki/output/static"
    decode_percent_encoded_filenames(target_directory)
