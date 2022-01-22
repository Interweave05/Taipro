# -*- coding:utf-8 -*-
# pip install pyttsx3
# author: Interweave
# date: 2022.1.20 22:20
# email: interweave@qq.com
# 效果还行

import pyttsx3

# 创建对象
engine = pyttsx3.init()
# 获取当前语音速率
rate = engine.getProperty('rate')
print(f'语音速率：{rate}')
# 设置新的语音速率
engine.setProperty('rate', 130)
# 获取当前语音音量
volume = engine.getProperty('volume')
print(f'语音音量：{volume}')
# 设置新的语音音量，音量最小为 0，最大为 1
engine.setProperty('volume', 1)
# 获取当前语音声音的详细信息
voices = engine.getProperty('voices')
print(f'语音声音详细信息：{voices}')
# 设置当前语音声音为女性，当前声音不能读中文
# engine.setProperty('voice', voices[1].id)
# 设置当前语音声音为男性，当前声音可以读中文
engine.setProperty('voice', voices[0].id)
# 获取当前语音声音
voice = engine.getProperty('voice')
print(f'语音声音：{voice}')
# 语音文本输出
# 自动循环输出多个文件
i = 0
for i in range(0, 4):
    engine.save_to_file('123', f'{i}.mp3')
    i += i
engine.runAndWait()
engine.stop()
