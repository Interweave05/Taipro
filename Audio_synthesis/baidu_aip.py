# -*- coding:utf-8 -*-
# pip install pyttsx3
# author: Interweave
# date: 2022.1.20 19:57
# email: interweave@qq.com
# 效果一般般
from aip import AipSpeech

APP_ID = '25517271'
API_KEY = 'DvbjZrHv7eKDYiRnvjYUZajX'
SECRET_KEY = 'eZWXWqDdMBwWIPxBU7g5mvi2sis2isBo'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
for i in range(1):
    if i == 0:
        content = '模型加载成功'
        result = client.synthesis(content, 'zh', 1, {'spd': 6, 'vol': 5, 'per': 3})
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    filename = str(i)
    if not isinstance(result, dict):
        with open(filename + '.mp3', 'wb') as f:
            f.write(result)
