''' batchextract.py
extractmp4をマルチスレッドで並列に実行するbatchextract関数を記述する
'''

from mp42mp3.extractmp3 import extractmp3
import concurrent.futures
import os

def batchextract(cfdict: dict, mp4list: list[str]):
    ''' extractmp4を並列に実行する '''

    ffmpeg = cfdict['ffmpegpath']

    nthreads = os.cpu_count()-1
    nthreads = max(1, nthreads)
    ex = concurrent.futures.ThreadPoolExecutor(max_workers=nthreads)

    futures = [ ex.submit(extractmp3(ffmpeg, mp4, cfdict['mp3path'])) for mp4 in mp4list ]

    concurrent.futures.wait(futures)

    return
   