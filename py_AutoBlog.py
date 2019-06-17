from selenium import webdriver
import time,os,random,shutil
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Firefox()
browser.set_page_load_timeout(20)
browser.set_script_timeout(20)

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

def moveFile(fileDir,tarDir):
        pathDir = os.listdir(fileDir)    #取图片的原始路径
        filenumber=len(pathDir)
        # rate=0.1    #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
        picknumber=9 #按照rate比例从文件夹中取一定数量图片
        sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片
        str_arrary = '#搞笑# #搞笑动图# #幽默# #笑话#\n'
        index = 0
        for i in sample:
            file_name, extension = os.path.splitext(i)
            index = index + 1
            str_arrary = str_arrary + str(index) + '. ' + file_name + '\n'
        print(str_arrary)
        for name in sample:
                try:
                    shutil.move(fileDir+name, tarDir+name)
                except Exception:
                    pass
        return str_arrary

def isVerifyCodeExist():
    try:  # 如果成功找到验证码输入框返回true
        browser.find_element_by_css_selector('input[name="verifycode"]')
        return True
    except:  # 如果异常返回false
        return False

def manualVerifyCode():
    while isVerifyCodeExist():
        if browser.current_url.split('/')[-1] == 'home':
            print(u'登录成功')
            break

try: #get到页面
    browser.get("https://weibo.com")
except:
    browser.execute_script("window.stop()")
time.sleep(30)
try:
    WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="loginname"]')).send_keys('darboy@foxmail.com')
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[2]/div/input').send_keys('3.14159265758')
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]/a').click()
    time.sleep(5)
except:
    pass
if isVerifyCodeExist():
    manualVerifyCode()
time.sleep(15)
while True:
    del_file('D:\\uploadImage')
    make_folder('D:\\uploadImage')
    text = moveFile('D:\\爬虫下载\\image\\','D:\\uploadImage\\')
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').send_keys(text)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[2]/a[2]').click()    #图片
    os.system("E:\\code\\python\\py-FundOnline\\upload.exe")
    time.sleep(20)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a').click()       #发布
    time.sleep(300)
    # time.sleep(5)

