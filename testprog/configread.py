''' configread.py
@version 0.1のテストプログラム
config.jsonの読み込みが正しく行えるかをテストする
'''

from mp42mp3.read_config import read_config
from pprint import pprint

if __name__ == '__main__':
    cfdict = read_config()
    pprint(cfdict)

