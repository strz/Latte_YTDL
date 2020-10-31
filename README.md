# Latte_YTDL

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

Warnings :

1. Make sure that this file is placed at C Drive(Since the code supposes that itself is placed on C Drive).
If other Drives like D, then the code will create D://Videos/VTubers... and save videos at that path.
2. There are few reported bugs to youtube-dl official that are currently working Like "JS player error", which I can't make trouble-shooting them.
Several same error reports are found. In this case, please consider using another tools.


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

주의사항 :
이 파일이 항상 C드라이브에 놓이도록 해주세요. 코드가 C드라이브에 놓여있을 것이라고 암묵적으로 가정하고 있기때문입니다.
만약 다른 D드라이브같은 곳에 놓여서 실행되면, 코드는 D://Videos/VTubers...와 같이 새롭게 카테고리를 만들고 비디오를 해당 경로에 다운로드할 것입니다.
youtube-dl 패키지에는 현재 몇 가지 보고되는 JS Player error같은 오류가 있습니다. 제가 대응하기 어려운 문제입니다.
같은 오류보고가 보고되고 있으며, 이럴 경우 다른 툴의 사용을 고려해주세요.



日本語案内

このPythonコードは、貴方のお好きなユーチューブ動画をダウンロード出来る様にお手伝いします。Pythonをどう使えばいいか分からなくても
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

注意事項：
このファイルがCドライブに置かれるようにしてください。コードがCドライブに置かれていると暗黙的に仮定しているためです。

もしほかのドライブ、Dなどで置かれ実行するとコードはD://Videos/VTubersのように新しく経路を作り、動画をそこで保存します。

現在youtube-dlパッケージには幾つか報告されてるJS Player errorなどのエラーがあります。私から対応しがたい問題です。

同じエラー報告が今も報告されており、たまにダウンロードできない場合があります。もしそうなったら、ほかのツールのご使用をどうかお考えになってください。
