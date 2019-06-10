import re, urllib.request, threading, time
import matplotlib.pyplot as plt
import numpy as np
now_net_value = input('当前净值：')
response = urllib.request.urlopen('http://fund.eastmoney.com/000656.html')
content = response.read().decode('utf-8')
last_10_days_percent = re.findall('<td class="alignLeft">[0-9][0-9]-[0-9][0-9]</td>  <td class="alignRight bold">(.+?)</td>', content)
print(last_10_days_percent)
mean_data = []
for i in last_10_days_percent:
    mean_data.append(float(i))
print(np.mean(mean_data))
print((float(now_net_value) - np.mean(mean_data))/np.mean(mean_data)*100)