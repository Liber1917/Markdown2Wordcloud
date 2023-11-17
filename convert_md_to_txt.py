import sys
import mistune
import re

def convert_md_to_txt(md_file_path, txt_file_path):
    print('md_file_path:', md_file_path)
    print('txt_file_path:', txt_file_path)
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
        html_content = mistune.markdown(md_content)
        txt_content = re.sub('<p>|</p>', '', html_content)  # 去除<p>标签
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(txt_content)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python convert_md_to_txt.py <input_file.md>')
        sys.exit(1)

    md_file_path = sys.argv[1]
    txt_file_path = 'output.txt'
    convert_md_to_txt(md_file_path, txt_file_path)
