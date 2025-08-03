''' listmp4.py
@version 0.3のテストプログラム
mp4ファイルのリストを作成する
'''

from mp42mp3.read_config import read_config
from mp42mp3.globmp4 import globmp4
from pprint import pprint

if __name__ == '__main__':
    cfdict = read_config()

    mp4list = globmp4(cfdict)
    pprint(mp4list)
