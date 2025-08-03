''' globmp4.py
mp4ファイルをリストアップするglobmp4関数を記述する
'''

from glob import glob
import os.path

def globmp4(cfdict: dict) -> list[str]:
    ''' mp4ファイルをリストアップする '''
    mp4path = cfdict['mp4path']
    pathpattern = os.path.join(mp4path, '**/*.mp4')

    globbed = glob(pathpattern, recursive=True)
    return globbed
