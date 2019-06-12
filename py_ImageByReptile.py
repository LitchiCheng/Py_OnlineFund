import requests
import urllib
import re
from bs4 import BeautifulSoup
import os
import shutil
import time
import random

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
    header_list = [
    #遨游
    {"user-agent" : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
    #火狐
    {"user-agent" : "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
    #谷歌
    {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}]
    header = random.choice(header_list)
    if page == 1:   
        res = requests.get('http://xiaohua.zol.com.cn/qutu/', headers = header)
    else:
        res = requests.get('http://xiaohua.zol.com.cn/qutu/'+str(page)+'.html', headers = header)
    soup = BeautifulSoup(res.text,'html.parser')
    print('\n' + res.text + '\n')
    list_of_soup = soup.select('img')
    for i in list_of_soup:
        img_src = i.get('src')
        img_title = i.get('alt')
        if img_src == None:
            img_src = i.get('loadsrc')
        if img_src[0:6] == "https:":
            if img_src[-3:] == "jpg" or img_src[-3:] == "gif":
                urllib.request.urlretrieve(img_src, download_to_address + '%s.%s'%(img_title, img_src[-3:]))
                print(img_title)
                print(img_src)
        time.sleep(0.1)
        

mkpath="\\image\\"        #填你想命名的文件夹名
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_address = pwd + mkpath
make_folder(out_address)        #创建当前目录下的文件夹

for i in range(1,936):
    print('当前页面:%d\n'%i)
    time.sleep(5)
    downloadImage(out_address,i)