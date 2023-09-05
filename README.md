# Webcam Splitter by @Kurogane_8_Gk

[日本語の説明もあります。](https://github.com/kuroganegames/WebcamSplitter/blob/main/README_JP.md)

Webcam Splitter is a Python program that splits a single physical webcam into multiple virtual cameras.

It comes with a GUI, making it easy to configure the settings.

## Features

- Captures video from a physical webcam
- Sends video to two virtual cameras
- Saves and loads previous settings in an INI file

## Dependencies
- ffmpeg
- [schellingb/UnityCapture](https://github.com/schellingb/UnityCapture)
- OBS Studio

### For Python Usage

You'll need opencv-python and pyvirtualcam.

Tested on Python 3.9.13

```
pip install opencv-python
pip install pyvirtualcam
```

## Installation
### EXE Version

You can download it from the [Release](https://github.com/kuroganegames/WebcamSplitter/releases) page.

~~Also available on booth.~~ Coming soon

### Python Version

After installing all the dependencies, clone or download this repository.

## Usage
- Launch the program.
- A GUI will appear, where you can select the input device (physical webcam) and output devices (virtual cameras).
- Click the "OK" button to start splitting the camera.
- The program runs on a single thread, so the window will freeze after execution, but the program is working correctly.
- To exit, press the 'X' on the black window.

## License
This project is released under the GPL license. For more details, please refer to the [LICENSE](https://github.com/kuroganegames/WebcamSplitter/blob/main/LICENSE).
