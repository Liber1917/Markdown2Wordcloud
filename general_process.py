import sys
import subprocess

def call_convert_md_to_txt(md_file_path):
    subprocess.run(['python', 'convert_md_to_txt.py', md_file_path])

def call_WordFrequencyCount(arg1=None):
    cmd = ['python', 'WordFrequencyCount.py']
    if arg1 is not None:
        cmd.append(arg1)
    subprocess.run(cmd)

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Usage: python general_process.py <input_file.md> [arg1]')
        sys.exit(1)

    md_file_path = sys.argv[1]
    if len(sys.argv) == 3:
        arg1 = str(sys.argv[2])
    else:
        arg1 = None

    # 调用第一个脚本
    call_convert_md_to_txt(md_file_path)

    # 调用第二个脚本，可选参数为arg1
    call_WordFrequencyCount(arg1)
