''' read_config.py
config.jsonの読み込みを行うread_config関数を記述する
'''

import os.path
import json

def read_config(filename: str = 'config.json') -> dict:
    ''' config.jsonを読み込み、dictの形式で返す '''

    cdir = os.path.split(__file__)[0]
    with open(os.path.join(cdir, filename), mode='r', encoding="utf-8") as fp:
        cfdict = json.load(fp)
    
    return cfdict
