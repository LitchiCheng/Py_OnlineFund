from py_SendEmail import Email,SMTPServe
from py_RecieveEmail import EMailConsole
import os

# 输入邮件地址, 口令和POP3服务器地址:
email = 'darmail@163.com'
password = '520521ch'
pop3_server = 'pop.163.com'
reciever = []

if __name__ == "__main__":
    import time
    
    while(1):
        time.sleep(5)
        tmp_content = ""
        tmp_reciever = ""
        mail_server = EMailConsole(email, password, pop3_server)
        if mail_server.getMailNum() > 0:
            tmp_content = mail_server.getMailContent(1)
            tmp_reciever = mail_server.getMailFrom(1)
            while mail_server.getMailNum() != 0:
                mail_server.delMail(1)
            mail_server.loginOut()
            if tmp_content != "None":
                if  tmp_content.find("帮助") != -1:
                    mail_send = Email(email, password, SMTPServe.dict['163'])
                    mail_send.setSender(email)
                    reciever.clear()
                    reciever.append(tmp_reciever)
                    mail_send.setReciever(reciever)
                    mail_send.setSubject("帮助")
                    mail_send.addPlainContent("1. 立即查询保存基金情况\n")
                    mail_send.addPlainContent("...发送相应序号即可调用功能...\n")
                    mail_send.sendEmail()
                elif tmp_content.find("1") != -1:
                    os.system("python E:\code\python\py-FundOnline\py_Email-fund.py")
                
        # elif tmp_content != None:
        #     mail_send = Email(email, password, SMTPServe.dict['163'])
        #     mail_send.setSender(email)
        #     reciever.clear()
        #     reciever.append(mail_server.getMailFrom(1))
        #     mail_send.setReciever(reciever)
        #     mail_send.setSubject("未知指令")
        #     mail_send.addPlainContent("未知指令")
        #     mail_send.sendEmail()
        #     mail_server.delMail(1)







