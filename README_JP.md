# Webcam Splitter by @Kurogane_8_Gk

Webcam Splitterは、1つの物理的なWebカメラを複数の仮想カメラに分岐させるPythonプログラムです。

GUIを備えており、簡単に設定を行うことができます。

## 機能

- 物理的なWebカメラから映像を取得
- 2つの仮想カメラに映像を送信
- 前回の設定をINIファイルに保存・読み込み

## 依存関係
- ffmpeg
- schellingb/UnityCapture
- OBS Studio

### Pythonで使用する場合

opencv-python、pyvirtualcamが必要です。

Python 3.9.13で動作確認済み

```
pip install opencv-python
pip install pyvirtualcam
```

## インストール
### exe版

[Release](https://github.com/kuroganegames/WebcamSplitter/releases)よりダウンロード可能です。

~~boothからも入手可能です。~~ 準備中

### Python版

依存関係をすべてインストールした後、このリポジトリをクローンまたはダウンロードしてください。



## 使い方
- プログラムを起動します。
- GUIが表示されるので、入力デバイス（物理的なWebカメラ）と出力デバイス（仮想カメラ）を選択します。
- "OK"ボタンをクリックして、カメラの分岐を開始します。
- シングルスレッドで動作するため、実行後、ウィンドウはフリーズしますが、プログラムは正常に動いています。
- 終了時は黒いウィンドウ側のXを押してください。

## ライセンス
このプロジェクトはGPLライセンスのもとで公開されています。詳細は[LICENSE](https://github.com/kuroganegames/WebcamSplitter/blob/main/LICENSE)を参照してください。
