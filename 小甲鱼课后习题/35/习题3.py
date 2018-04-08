# 提供一个文件夹浏览框,让用户选择需要打开的文本文件,打开并显示文件内容
import easygui as g
import os

file_path = g.fileopenbox(default='*.txt')

with open(file_path, encoding='utf-8') as f:
    title = os.path.basename(file_path)
    msg = 'The contents of file %s are as follows' % title
    text = f.read()
    g.textbox(msg, title, text)
