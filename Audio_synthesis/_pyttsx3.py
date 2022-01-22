# -*- coding:utf-8 -*-
# pip install pyttsx3
# author: Interweave
# date: 2022.1.22 21:53
# email: interweave@qq.com
# 效果还行

import pyttsx3


def pyttsx(text, speed, volume, language, filename):
    print("ready")
    # 实例化对象
    engine = pyttsx3.init()
    # 语音速率
    engine.setProperty('rate', speed)
    # 语音音量，音量最小为 0，最大为 1
    engine.setProperty('volume', volume)
    # 语音模式,0为中文,1为英文
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[language].id)
    # 输出音频
    engine.save_to_file(text, f"{filename}.mp3")
    engine.runAndWait()
    engine.stop()


if __name__ == '__main__':
    pyttsx("124343", 130, 1, 0, "test")
