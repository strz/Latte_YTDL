"""

Youtube Downloader 1.0 2020 10 30 JJH

This Python code helps you download Youtube video files that you like, no matter you don't know how to handle Pyhton,
you can easily operate this code just by changing Save path and URLs. Please install Python, and get your favorite videos!

https://www.python.org/downloads/

###

IMPORTANT : When you install Python, Must check "Add Python 3.9 to PATH". You need to download "youtube_dl" package to initiate the code.

After Python installed, type Windows + R to open Execute. And type 'cmd', then a black command line will appear. Now type like this : pip install youtube_dl
If there is no problem, installation will be successful. This sequence is necessary.

###

If you want to read document, create another python file
and import inspect, youtube_dl, and call print(inspect.getdoc(youtube_dl.YoutubeDL())).
Although this document does not show all the information of it, at least you can modify download options.

##########
IF you are new at Python, and just want to download videos or playlist, modify "Subcategory" and "URLS"
each means "Store path", "Download URL".

Download Sequence
1. Run IDLE(Python 3.9 32 or 64-bit)
2. Open this python file
3. modify Subcategory and URLS as you want.
4. Press F5 to start download
##########


한국어 안내

이 파이썬 코드는 당신이 좋아하는 유튜브 비디오를 다운로드할 수 있도록 도와줍니다. 파이썬을 어떻게 다루는지 몰라도
저장경로와 URL을 변경하는 것만으로도 쉽게 이 코드를 작동시킬 수 있습니다. 파이썬을 설치하고 좋아하는 비디오를 다운받으세요!

https://www.python.org/downloads/

###

중요한 알림 : 파이썬을 설치할 때, 반드시 "Add Python 3.9 to PATH"를 체크하세요. 또한 "youtube_dl" 패키지를 설치해야 이 코드를 실행시킬 수 있습니다.
파이썬을 설치하고난 뒤에, 윈도우 키 + R을 눌러서 "실행"창을 연 다음 "cmd"를 입력하세요. 그러면 검은 명령창이 뜰 텐데, 이제 "pip install youtube_dl"이라고 입력하세요. 별다른 문제가 없다면 설치는 성공적일 것입니다. 이 절차는 반드시 수행되어야만 합니다.

###

youtube_dl에 관한 문서를 읽고 싶으시다면 또다른 파이썬 파일을 생성하고 inspect, youtube_dl 모듈을 가져온 다음 print(inspect.getdoc(youtube_dl.YoutubeDL()))으로 기본적인 사항을 확인할 수 있습니다. 모든 정보를 다 알 수 있는 건 아니나, 다운로드 옵션을 조정할 수는 있습니다.

##########
파이썬이 처음이고, 그저 동영상이나 재생목록을 받고 싶다면 "Subcategory"와 "URLS"를 수정하세요. 각각 "저장경로", "다운로드 URL"을 의미합니다.

다운로드 절차.
1. IDLE(Python 3.9 32 또는 64-bit)을 실행하세요.
2. 이 파이썬 파일을 여세요
3. Subcategory와 URLS를 원하시는대로 수정하세요.
4. F5를 눌러서 다운로드를 시작하세요.
##########


日本語案内

このPythonコードは、貴方のお好きなユーチューブ動画をダウンロード出来る様にお手伝いします。Pythonをどう使えばいいか知らなくても
ダウンロード経路とURLを変更するだけで手間をかけずに容易くこのコードを作動させることができます。Pythonを設置して好きな動画をダウンロードしましょ！

https://www.python.org/downloads/

###
お知らせ：Pythonを設置するとき、必ずや「Add Python 3.9 to PATH」をチェックしてください。なお、「youtube_dl」パッケージを設置してこそこのコードを実行することができます。
Pythonの設置が完了した後、Windows＋Rを押し「実行」欄を開けて「cmd」を入力してください。そうしたら黒い命令窓が登場するはずで、そこで「pip install youtube_dl」とご入力ください。問題なければ成功的に設置されるはずです。このシークエンスは必要不可欠です。
###

youtube_dlに関しての文書はもう一つのPythonファイルを作りinspect, youtube_dlモジュールを持ってきて、print(inspect.getdoc(youtube_dl.YoutubeDL()))で基本的な情報を確認することができます。全てまではないんですけど、ダウンロードオプションを調整するには役に立ちます。

##########
Pythonが初めてで、ただ動画や再生リストをダウンロードするだけなら"Subcategory"と"URLS"を修正してください。それぞれ「ダウンロード経路」と「ダウンロードURL」を示しています。

ダウンロードシークエンス
1.IDLE(Python 3.9 32または64-bit)を実行してください。
2.このファイルを開けてください。
3.SubcategoryとURLSをお好きに修正してください。
4.F5を押してダウンロードを始めてください。
##########

1.1 Fixed a problem that the path of YTDL.py requires specific path. Now always initializes by [C://User/Username], hence works well anywhere on the computer. (Personal folder, background, etc)




"""

import os
import youtube_dl

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

    YTDL_ABS_PATH = os.path.abspath('..').replace('\\', '/')
    # This path initializes to C:\Users\USERNAME. and add paths by Subcategory list below

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
