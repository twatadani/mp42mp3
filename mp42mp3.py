''' mp42mp3.py
mp4ファイルを一括でmp3ファイルに変換するメインプログラム
'''

from read_config import read_config
from globmp4 import globmp4
from batchextract import batchextract
import os.path
import os

if __name__ == '__main__':

    cfdict = read_config()
    print('コンフィグを読み込みました。以下の設定でmp4を一括変換します。')
    print('mp4ファイル探索ディレクトリ:', cfdict['mp4path'])
    mp3path = cfdict['mp3path']
    print('mp3ファイル出力ディレクトリ:', mp3path)

    if not os.path.exists(mp3path):
        print(mp3path, 'が存在しないため作成します。')
        os.makedirs(mp3path)

    mp4list = globmp4(cfdict)
    print(len(mp4list), '件のmp4ファイルが検出されました。')

    print('mp3抽出を実行します。')
    batchextract(cfdict, mp4list)

    print('抽出が終了しました。')