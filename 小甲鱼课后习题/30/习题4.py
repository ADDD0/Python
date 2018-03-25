# 输入开始搜索的路径,查找该路径下(包含子文件夹内)所有的视频格式文件(如mp4,rmvb,avi等)
# 在当前路径下创建一个文件(VideoList.txt)存放文件路径
import os

search_type = ['.mp4', '.rmvb', '.avi']
video_path = []


def search_video(catalog):
    os.chdir(catalog)
    for each in os.listdir(os.curdir):
        if os.path.splitext(each)[1] in search_type:  # 扩展名匹配成功
            video_path.append(os.getcwd()+os.sep+each+os.linesep)  # os.linesep为当前平台所使用的行终止符
        if os.path.isdir(each):
            search_video(catalog+os.sep+each)
            os.chdir(os.pardir)


search_video(input('Please enter the initial directory to search:'))
file = open('VideoList.txt', 'w')
file.writelines(video_path)
file.close()
