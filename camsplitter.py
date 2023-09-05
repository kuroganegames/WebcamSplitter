#coding:utf-8

import cv2  # OpenCVライブラリ
import pyvirtualcam  # 仮想カメラライブラリ
import subprocess  # サブプロセス管理ライブラリ
import tkinter as tk  # GUIライブラリ
from tkinter import ttk  # ttkウィジェット
import configparser  # INIファイル操作ライブラリ
import os  # OS操作ライブラリ

# カメラデバイスのリストを取得する関数
def get_device_list():
    # ffmpegコマンドでデバイスリストを取得
    cmd = "ffmpeg -list_devices true -f dshow -i dummy"
    result = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, shell=True)
    data_log = result.stderr
    # デバイス情報の行を抽出
    device_lines = [line for line in data_log.split('\n') if 'dshow @' in line and '\"' in line if 'Alternative name' not in line]
    extracted_device_info = []
    # デバイス情報を抽出
    for device in device_lines:
        device_id = device.split(' ')[2]
        device_name = device.split('"')[1]
        device_type = device.split('(')[1].split(')')[0]
        extracted_device_info.append({"id": device_id, "name": device_name, "type": device_type})
    return extracted_device_info

# カメラを分岐させる関数
def start_cam_split():
    button_ok.config(text="Running")  # ボタンのテキストを"Running"に変更
    root.update_idletasks()  # GUIを更新
    
    # 選択されたデバイス情報を取得
    selected_device_index = combo1.current()
    selected_device1 = combo2.get()
    selected_device2 = combo3.get()
    
    # 選択されたデバイスをINIファイルに保存
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'InputDevice': str(selected_device_index),
                          'OutputDevice1': selected_device1,
                          'OutputDevice2': selected_device2}
    with open('device_settings.ini', 'w') as configfile:
        config.write(configfile)
    
    # OpenCVでカメラを開く
    cap = cv2.VideoCapture(selected_device_index)
    
    # 仮想カメラを開く
    with pyvirtualcam.Camera(width=640, height=480, fps=30, device=selected_device1) as cam1:
        with pyvirtualcam.Camera(width=640, height=480, fps=30, device=selected_device2) as cam2:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cam1.send(frame_rgb)
                cam2.send(frame_rgb)
                cam1.sleep_until_next_frame()
                cam2.sleep_until_next_frame()
    cap.release()  # カメラリソースを解放

# INIファイルから前回の設定を読み込む
config = configparser.ConfigParser()
if os.path.exists('device_settings.ini'):
    # INIファイルが存在する場合は設定を読み込む
    config.read('device_settings.ini')
    prev_input_device = config.getint('DEFAULT', 'InputDevice', fallback=None)
    prev_output_device1 = config.get('DEFAULT', 'OutputDevice1', fallback=None)
    prev_output_device2 = config.get('DEFAULT', 'OutputDevice2', fallback=None)
else:
    # INIファイルが存在しない場合はNoneを設定
    prev_input_device = None
    prev_output_device1 = None
    prev_output_device2 = None

# カメラデバイスリストを取得
devices = get_device_list()
device_names = [device["name"] for device in devices if device["type"] == "video"]

# GUI設定
root = tk.Tk()
root.title("Webcam Splitter by @Kurogane_8_Gk")
iconfile = r"M:\devs\python\webcam\webcamplitter.ico"
root.iconbitmap(default=iconfile)

# GUIのフレームの設定
frame = ttk.Frame(root, padding="10")
frame.grid()

# プルダウンメニューとラベルの設定
ttk.Label(frame, text="Input Device:").grid(row=0, column=0)
combo1 = ttk.Combobox(frame, values=device_names, width=30)
combo1.grid(row=0, column=1)
if prev_input_device is not None:
    combo1.current(prev_input_device)
else:
    combo1.set("Select Input Device")

ttk.Label(frame, text="Output Device 1:").grid(row=1, column=0)
combo2 = ttk.Combobox(frame, values=device_names, width=30)
combo2.grid(row=1, column=1)
combo2.set(prev_output_device1 if prev_output_device1 else "Select Output Device 1")

ttk.Label(frame, text="Output Device 2:").grid(row=2, column=0)
combo3 = ttk.Combobox(frame, values=device_names, width=30)
combo3.grid(row=2, column=1)
combo3.set(prev_output_device2 if prev_output_device2 else "Select Output Device 2")

# OKボタンの設定
button_ok = ttk.Button(frame, text="OK", command=start_cam_split)
button_ok.grid(row=3, columnspan=2)

root.mainloop()  # GUIループを開始
