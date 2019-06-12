import requests
import urllib
import re
from bs4 import BeautifulSoup
import os
import shutil

def make_folder(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return True
    else:
        return False

def del_file(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        return True
    else:
        shutil.rmtree(path)
        return False

def downloadImage(download_to_address, page):
    if page == 1:   
        res = requests.get('http://xiaohua.zol.com.cn/qutu/')
    else:
        res = requests.get('http://xiaohua.zol.com.cn/qutu/'+str(page)+'.html')
    soup = BeautifulSoup(res.text,'html.parser')
    list_of_soup = soup.select('img')
    for i in list_of_soup:
        img_src = i.get('src')
        img_title = i.get('alt')
        if img_src == None:
            img_src = i.get('loadsrc')
        if img_src[0:6] == "https:":
            urllib.request.urlretrieve(img_src, download_to_address + '%s.%s'%(img_title, img_src[-3:]))
        print(img_title)
        print(img_src)

mkpath="\\image\\"        #填你想命名的文件夹名
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_address = pwd + mkpath
make_folder(out_address)        #创建当前目录下的文件夹

for i in range(1,936):
    #print(i)
    downloadImage(out_address,i)