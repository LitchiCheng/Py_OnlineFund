from selenium import webdriver
import time,os,random,shutil
from selenium.webdriver.support.ui import WebDriverWait

class TimeOut:
    def __init__(self, max_count, index):
        self.__count = 0
        self.__maxcount = max_count
        self.__index = index
    def trigger(self):
        self.__count = self.__count+1
        if self.__count >= self.__maxcount:
            print(str(self.__index) + ' time out!')
            self.__count = 0
            return True
        else:
            return False

trigger1 = TimeOut(10, 1)
trigger2 = TimeOut(10, 2)
trigger3 = TimeOut(10, 3)
trigger4 = TimeOut(10, 4)

def make_folder(path):
    # path=path.strip()
    # path=path.rstrip("\\")
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
    # if trigger1.trigger():
    #     break
    pathDir = os.listdir(fileDir)    #取图片的原始路径
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
            shutil.move(fileDir+'\\'+name, tarDir+'\\'+name)
        except Exception as e:
            print(e)
        # else:
        #     if len(os.listdir(tarDir)) == 9:
    return str_arrary

def checkFileExist(path):           #判断该路径下是否有文件存在
    if(len(os.listdir(path)) > 0):
        return True
    else:
        return False
    

class AutoBlog:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.set_page_load_timeout(20)
        self.browser.set_script_timeout(20)

    def __isVerifyCodeExist(self):
        try:  # 如果成功找到验证码输入框返回true
            self.browser.find_element_by_css_selector('input[name="verifycode"]')
            return True
        except:  # 如果异常返回false
            return False

    def __manualVerifyCode(self):
        while self.__isVerifyCodeExist():
            print('验证中。。。')
            if self.browser.current_url.split('/')[-1] == 'home':
                print('登录成功')
                break

    def openTheBlog(self, blog_url, wait_time):
        try: #get到页面
            self.browser.get(blog_url)       #"https://weibo.com"
        except:
            self.browser.execute_script("window.stop()")
        time.sleep(wait_time)#30

    def inputUserAndPassword(self,user_name,user_password,wait_time,log_in_time):
        try:
            WebDriverWait(self.browser, wait_time).until(lambda x: x.find_element_by_xpath('//*[@id="loginname"]')).send_keys(user_name)#'darboy@foxmail.com'
            WebDriverWait(self.browser, wait_time).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[2]/div/input')).send_keys(user_password)#'3.14159265758'
            time.sleep(1)
            WebDriverWait(self.browser, wait_time).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]/a')).click()
            time.sleep(5)
        except:
            pass
        if self.__isVerifyCodeExist():
            self.__manualVerifyCode()
        time.sleep(log_in_time) #15

    def sendBlog(self,pic_source,pic_target,script_path,upload_time):
        if(os.path.exists(pic_target)):
            if not checkFileExist(pic_target):
                text = moveFile(pic_source,pic_target)   #'D:\\爬虫下载\\image\\','D:\\uploadImage\\'
                time.sleep(1)
            else:
                del_file(pic_target)
                make_folder(pic_target)
                text = 'NOTHING'
                text = moveFile(pic_source,pic_target)   #'D:\\爬虫下载\\image\\','D:\\uploadImage\\'
                time.sleep(1)
        else:
            # del_file(pic_target)#'D:\\uploadImage'
            make_folder(pic_target)   #'D:\\uploadImage'
            text = 'NOTHING'
            text = moveFile(pic_source,pic_target)   #'D:\\爬虫下载\\image\\','D:\\uploadImage\\'
            time.sleep(1)
                
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').send_keys(text)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[2]/a[2]').click()    #图片
        time.sleep(2)
        os.system(script_path)#"E:\\code\\python\\py-FundOnline\\upload.exe"
        time.sleep(upload_time)#20
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a').click()       #发布
        try:
            error = self.browser.find_elements_by_class_name('S_txt1')
        except:
            error = 0
            print('没找到')
        if error:
            try:
                self.browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/a').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').clear()
                self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').send_keys('#搞笑# #搞笑动图# #幽默# #笑话#')
                self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a').click()       #发布
            except:
                print('有问题')


blog=AutoBlog()
blog.openTheBlog("https://weibo.com",10)
blog.inputUserAndPassword('darboy@foxmail.com', '3.14159265357', 10, 10)
while True:
    blog.sendBlog('D:\\爬虫下载\\image','D:\\uploadImage',"E:\\code\\python\\py-FundOnline\\upload.exe",20)
    time.sleep(300) 
