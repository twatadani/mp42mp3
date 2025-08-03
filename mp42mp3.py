''' mp42mp3.py
mp4ファイルを一括でmp3ファイルに変換するメインプログラム
'''

from mp42mp3.batchextract import batchextract
from mp42mp3.read_config import read_config
from mp42mp3.globmp4 import globmp4

if __name__ == '__main__':

    cfdict = read_config()
    print('コンフィグを読み込みました。以下の設定でmp4を一括変換します。')
    print('mp4ファイル探索ディレクトリ:', cfdict['mp4path'])
    print('mp3ファイル出力ディレクトリ:', cfdict['mp3path'])

    mp4list = globmp4(cfdict)

    print('mp3抽出を実行します。')
    batchextract(cfdict, mp4list)

    print('抽出が終了しました。')