''' extractmp3
外部コマンドffmpegを呼び出してmp3を抽出する関数extractmp3を記述する
'''

import os.path
import subprocess

def extractmp3(ffmpegpath: str, mp4path: str, mp3path: str):
    ''' ffmpegコマンドを呼び出してmp3を抽出する
     mp4pathはファイル名、mp3pathはディレクトリ名を指定する '''
    
    mp4path = os.path.expandvars(os.path.expanduser(mp4path))
    mp4filename = os.path.basename(mp4path)
    mp4prefix = os.path.splitext(mp4filename)[0]

    mp3filename = mp4prefix + '.mp3'
    mp3fullname = os.path.join(mp3path, mp3filename)
    ffmpegpath = os.path.expandvars(os.path.expanduser(ffmpegpath))

    # ffmpegを実行
    result = subprocess.run( [ffmpegpath, '-i', mp4path, '-c:a', 'mp3', mp3fullname] )

    return result
    