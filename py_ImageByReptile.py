import requests
import urllib
from bs4 import BeautifulSoup
res = requests.get('http://xiaohua.zol.com.cn/qutu/')
soup = BeautifulSoup(res.text,'html.parser')
print(soup.select('img'))