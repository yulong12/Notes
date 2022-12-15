

import pytube
import os
import string

Base_PATH = "/opt/software/ansible/pythonDemo/video"
listUrl="https://www.youtube.com/playlist?list=PLEkRYDcpWohzyea73KQzskcV8q3KrRu6N"

# 所有的英文标点符号替换为_： !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
def stringClean(str):
    punctuation_string = string.punctuation
    for i in punctuation_string:
        str = str.replace(i, '_')
    return str

# base url download video
def downloadYouTube(url,output):
    yt = pytube.YouTube(url)
    stream =yt.streams.get_highest_resolution()
    title=stringClean(yt.title)
    titleStr=title.replace(' ','_')+".mp4"
    try:
        print(f'    Downloading: {title}')
        stream.download(output,titleStr)
        print("Download"+title+" is completed successfully")
    except:
        print("Download"+title+"An error has occurred")
    

# base listurl get urls
def geturl(listurl):
    p=pytube.Playlist(listurl)
    print(f'Downloading: {p.title}')
    return p.video_urls,p.title.replace(' ','_')

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        '''
        os.mkdir(path)与os.makedirs(path)的区别是,当父目录不存在的时候os.mkdir(path)不会创建,os.makedirs(path)则会创建父目录
        '''
        os.makedirs(path) 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False


# base txt get a list
def readUrls(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines

# download Pamela
playlistUrls=readUrls("Pamela.txt")
for playListurl in playlistUrls:
    urls,listTitle=geturl(playListurl)
    downloadPath=Base_PATH+"/"+listTitle
    mkdir(downloadPath)
    for url in urls:
        downloadYouTube(url,downloadPath)

