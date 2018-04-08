# 在习题3的基础上增加功能,当用户点击'OK'按钮后,判断当前文件是否被修改过
# 若修改过,提示'覆盖保存','另存为'或'放弃保存'并实现相应的功能
import easygui as g
import os

file_path = g.fileopenbox(default='*.txt')

with open(file_path, encoding='utf-8') as old_file:
    title = os.path.basename(file_path)
    msg = 'The contents of file %s are as follows' % title
    text = old_file.read()
    text_after = g.textbox(msg, title, text)

if text != text_after[:-1]:  # textbox的返回值会追加一个换行符
    msg = 'Changes detected in the contents of the file, please select the following operation'
    choice = g.buttonbox(msg, 'Alert', ('Overwrite save', 'Save as', 'Give up saving'))
    if choice == 'Overwrite save':
        with open(file_path, 'w', encoding='utf-8') as old_file:
            old_file.write(text_after[:-1])
    if choice == 'Save as':
        another_path = g.filesavebox(default='.txt')
        if os.path.splitext(another_path)[1] != 'txt':
            another_path += '.txt'
        with open(another_path, 'w', encoding='utf-8') as new_file:
            new_file.write(text_after[:-1])
    if choice == 'Give up saving':
        pass
