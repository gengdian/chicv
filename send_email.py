import smtplib  # 负责发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容模块
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart  #


def send_email():
    smtpserver = 'smtp.qq.com'
    user = '1051166333@qq.com'
    password = 'grayzafkndembbad'

    sender = '1051166333@qq.com'
    receive = '1051166333@qq.com'

    subject = 'WBE selenium 自动化测试报告'

    content = "<html><h1 style='color:red'>我爱自学网，自学成才</h1></html>"

    send_file = open(r'D:\\xuexi\\data\\login_data.xlsx', 'rb').read()
    att = MIMEText(send_file, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="login_data.xlsx"'

    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(content, "html", "utf-8"))
    msgRoot["Subject"] = subject
    msgRoot["From"] = sender
    msgRoot["To"] = receive
    msgRoot.attach(att)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("开始发送邮件")
    smtp.sendmail(sender, receive, msgRoot.as_string())
    smtp.quit()
    print("发送完成")
