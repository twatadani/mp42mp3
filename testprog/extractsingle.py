''' extractsingle.py
@version 0.2のテストプログラム
config.jsonを読み込み、単一のmp4ファイルをmp3に変換する
'''

from mp42mp3.read_config import read_config
from mp42mp3.extractmp3 import extractmp3

if __name__ == '__main__':
    
    cfdict = read_config()

    ffmpeg = cfdict['ffmpegpath']

    extractmp3(ffmpeg, 'test.mp4', '.')


