import re, urllib.request, threading, time
import matplotlib.pyplot as plt
import numpy as np

lock = threading.Lock()
global_web_content_000656 = ''
global_web_content_519697 = ''
def getStrContentOfWebPage(url_address):
    while True:
        response = urllib.request.urlopen(url_address)
        content = response.read().decode('utf-8')
        time.sleep(1)
        lock.acquire()
        global global_web_content_000656
        global_web_content_000656 = content
        lock.release()

def getStrContentOfWebPage2(url_address):
    while True:
        response = urllib.request.urlopen(url_address)
        content = response.read().decode('utf-8')
        time.sleep(1)
        lock.acquire()
        global global_web_content_519697
        global_web_content_519697 = content
        lock.release()

def getListOfRTValuation(all_page_content):
    real_time_valuation = re.findall('id="gz_gsz">(.+?)</span>' ,all_page_content)
    # for i in real_time_valuation:
    #     print('基金实时估值为：')
    #     print(i)
    return real_time_valuation

def getListOfRTPercent(all_page_content):
    rt_percent = re.findall('id="gz_gszzl">(.+?)%</span>', all_page_content)
    for i in rt_percent:
        print('基金实时百分数：')
        print(i)
    return rt_percent

def getListOfLast10DaysPercent(all_page_content):
    last_10_days_percent = re.findall('<td class="alignLeft">.+?</td>  <td class="alignRight bold">(.+?)</td>', all_page_content)
    dd = []
    for i in last_10_days_percent:
        print(i)
        dd.append(float(i))
    return dd

thread_get_web_page_000656 = threading.Thread(target=getStrContentOfWebPage,args=('http://fund.eastmoney.com/000656.html',))
thread_get_web_page_000656.start()
# thread_get_web_page_000656.join()
thread_get_web_page_519697 = threading.Thread(target=getStrContentOfWebPage2,args=('http://fund.eastmoney.com/519697.html',))
thread_get_web_page_519697.start()
# thread_get_web_page_519697.join()

response = urllib.request.urlopen('http://fund.eastmoney.com/000656.html')
content = response.read().decode('utf-8')
last_10_days_percent = re.findall('<td class="alignLeft">[0-9][0-9]-[0-9][0-9]</td>  <td class="alignRight bold">(.+?)</td>', content)
print(last_10_days_percent)
mean_data = []
for i in last_10_days_percent:
    mean_data.append(float(i))
last_10_days_mean_000656 = np.mean(mean_data)

response = urllib.request.urlopen('http://fund.eastmoney.com/519697.html')
content = response.read().decode('utf-8')
last_10_days_percent = re.findall('<td class="alignLeft">[0-9][0-9]-[0-9][0-9]</td>  <td class="alignRight bold">(.+?)</td>', content)
print(last_10_days_percent)
mean_data = []
for i in last_10_days_percent:
    mean_data.append(float(i))
last_10_days_mean_519697 = np.mean(mean_data)

import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(2, 1)
plt.ion()
plt.figure(figsize=(2,4))
plt.subplots_adjust(left=0.3, wspace =0, hspace =0.5)#调整子图间距
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
y_000656 = []
y_519697 = []
while True:
    time.sleep(1)
    now_rtvaluation_000656 = getListOfRTValuation(global_web_content_000656)
    print(now_rtvaluation_000656)
    now_rtvaluation_519697 = getListOfRTValuation(global_web_content_519697)
    print(now_rtvaluation_519697)
    if (now_rtvaluation_000656 == []) or (now_rtvaluation_519697 == []):
        continue
    print(last_10_days_mean_000656)
    print(last_10_days_mean_519697)
    y_000656.append((float(now_rtvaluation_000656[0]) - last_10_days_mean_000656)/last_10_days_mean_000656*100)
    y_519697.append((float(now_rtvaluation_519697[0]) - last_10_days_mean_519697)/last_10_days_mean_519697*100)
    plt.clf()
    plt.subplot(gs[0, :])
    x1 = plt.plot(y_519697)
    plt.ylabel('RT-IOPV')
    plt.title('519697')
    plt.grid(True)
    plt.subplot(gs[1, 0])
    x2 = plt.plot(y_000656) 
    plt.ylabel('RT-IOPV')
    plt.title('000656')
    plt.grid(True)
    plt.pause(0.1)
    plt.ioff()
    




# print(getListOfLast10DaysPercent(content1))

# import matplotlib.pyplot as plt

# import numpy as np
# y_data = getListOfLast10DaysPercent(content1)        #param of plot should be list
# y = []
# plt.ion()
# for i in y_data:
#     y.append(i)
#     plt.clf()
#     plt.plot(y)
#     plt.grid(True)
#     plt.pause(1)
#     plt.ioff()
# print(np.mean(y_data))




# sf = open('record.txt','wb')
# sf.write(html)
# sf.close()
# print(type(str(html)))
# tt = str(html)
# #id="gz_gsz">1.2106</span>
# #id="gz_gszzl">-0.86%</span>
# #<td class="alignLeft">06-06</td>  <td class="alignRight bold">1.2110</td>  <td class="alignRight bold">1.4610</td>  <td class="RelatedInfo alignRight10 bold"><span class="ui-color-green">-0.82%</span>
