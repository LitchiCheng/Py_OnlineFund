import time,os,datetime,re, urllib.request
import numpy as np
from py_SendEmail import Email,SMTPServe

def convertContent(fund_code, email):
    url = "http://fund.eastmoney.com/"+str(fund_code)+".html"
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    last_10_days_percent = re.findall('<td class="alignLeft">[0-9][0-9]-[0-9][0-9]</td>  <td class="alignRight bold">(.+?)</td>', content)
    mean_data = []
    for i in last_10_days_percent:
        mean_data.append(float(i))
        last_10_days_mean = np.mean(mean_data)
    real_time_valuation = re.findall('id="gz_gsz">(.+?)</span>' ,content)
    rt_percent = re.findall('id="gz_gszzl">(.+?)%</span>', content)
    email.addPlainContent("基金代码: "+ str(fund_code) + "\n")
    email.addPlainContent("实时净值估值："+ str(real_time_valuation[0]) + "\n")
    email.addPlainContent("估计增长百分数："+str(rt_percent[0])+"%\n")
    email.addPlainContent("近十日净值平均值："+str(last_10_days_mean)[0:5]+"\n")
    email.addPlainContent("\n")

def addFundPic(fund_code, email):
    file_name = fund_code + ".png"
    urllib.request.urlretrieve("http://j4.dfcfw.com/charts/pic6/"+file_name, file_name)
    email.addAttachFile((file_name))

if __name__ == "__main__":
    sender = 'da***@163.com' 
    receivers = ['***@qq.com',] #, '1747883186@qq.com'
    pwd = "52***" 
    email = Email(sender, pwd, SMTPServe.dict['163'])
    email.setSender(sender)
    email.setReciever(receivers)
    date_str = (str(time.localtime()[0]) +"-"+ str(time.localtime()[1]) +"-"+ str(time.localtime()[2]) +" "\
        +str(time.localtime()[3]) +":"+ str(time.localtime()[4])+":"+ str(time.localtime()[5])+" "\
        +"周"+str(time.localtime()[6]+1))
    title = date_str + (" <基金信息>")
    email.setSubject(title)

    convertContent("000656", email)
    convertContent("519697", email)
    convertContent("260108", email)
    convertContent("100038", email)

    addFundPic("000656", email)
    addFundPic("519697", email)
    addFundPic("260108", email)
    addFundPic("100038", email)
    
    email.sendEmail()



