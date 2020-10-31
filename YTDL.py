"""

Youtube Downloader 1.0 2020 10 30 JJH

1.1 Fixed a problem that the path of YTDL.py requires specific path. Now always initializes by [C://User/Username], hence works well anywhere on the computer. (Personal folder, background, etc)

"""

import os
import youtube_dl
import getpass

print('CURRENT WORKING DIRECTORY: ', os.getcwd())


def downloader(external_path, videos_list):
    download_path = os.path.join(external_path, '%(upload_date)s-%(title)s.%(ext)s')
    # read http://manpages.ubuntu.com/manpages/hirsute/en/man1/youtube-dl.1.html  -> Output template
    print(download_path)
    for urls in videos_list:
        download_options = {
            # Note that this option part is still under researching.
            'format': 'best/best',  # see options.py for more infos
            'outtmpl': download_path,
            'writesubtitles': 'best',
            'writethumbnail': 'best',# If there is no thumbnail, then YTDL will automatically choose *.webp extension.
            'nooverwrites': True,
            # prevents duplicated download if the video already exists at the same path. does not work if the save path is different.
            'geo_bypass': False
            # Use when you're restricted by legion lock. However, basically VTuber streams are globally open.
            # 'skip_download': True  # Test code. Skips download.
        }
        try:
            with youtube_dl.YoutubeDL(download_options) as YDL:
                YDL.download([urls])
            print(f'{len(videos_list)} Video(s) Download Complete')
        except Exception as E:
            print('An error occured', E)  # this code is referred at https://tech.dslab.kr/2019/09/10/python-youtube_dl/


if __name__ == "__main__":

    UID = getpass.getuser()
    
    YTDL_ABS_PATH = os.path.abspath('..').replace('\\', '/')
    # This path initializes to C:\Users\USERNAME. and add paths by Subcategory list below
    # 

    Subcategory = ['Videos', 'YTDL', 'VTubers', 'にじさんじ KR']  # Note that 'Videos' is Windows default path.
    # In order to stores videos at different path, open CMD and check what your directory is.
    # Hint : type 'dir' shows you what directory you have, 'cd' [Directory] moves your current working path

    for t in Subcategory:
        YTDL_ABS_PATH += '/' + t
        if os.path.exists(YTDL_ABS_PATH):
            print(f'the path {YTDL_ABS_PATH} already exists')
        else:
            os.mkdir(YTDL_ABS_PATH)
            print(f'Created a path {YTDL_ABS_PATH}')
    # this FOR statement helps you create the path whether it does really exist or not
    # if the path already exists

    # Now, ignite sequences
    URLS = [
        'https://youtu.be/ntbaT9_YM2I',
        'https://youtu.be/n5anMdABRK0'
    ]  # This link is a sample. Ryu Hari's Weird DJ Party, Suha and Boni(Nijisanji ID)'s APEX Legends Collaboration.
    # Since URLS is list, you can add links as many as you want. But you can't distribute links individually.
    # Note that PLAYLIST also works. YoutubeDL code will automatically analyze and start download.
    downloader(external_path=YTDL_ABS_PATH, videos_list=URLS)
