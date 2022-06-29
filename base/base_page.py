from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib  # 负责发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容模块
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart
import os

smtpserver = 'smtp.qq.com'  # 发件服务器
user = '1051166333@qq.com'  # 发件人邮箱
password = 'grayzafkndembbad'  # 授权码

sender = '1051166333@qq.com'  # 定义发件人
receive = '1051166333@qq.com'  # 定义收件人

subject = 'WBE selenium 自动化测试报告'  # 定义标题

content = "<html><h1 style='color:red'>切</h1></html>"  # 正文

report_dir = 'D:\\py_project\\chicv\\test_report'


class BasePage:
    def __init__(self):
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.get("http://localhost/e/admin/index.php")

    #  封装定位元素并返回， 注意参数loc解包
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    #  封装需要输入值的数据
    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 封装点击
    def click(self, loc):
        self.locator_element(loc).click()

    # 封装进入frame框架
    def goto_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 封装退出frame框架
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 封装下拉框关键字
    def choice_select(self, loc, value):
        sel = Select(driver.find_element(*loc))
        sel.select_by_value(value)

    # 封装获取定位元素的值
    def get_value(self, loc):
        return self.locator_element(loc).text

    # 获取最新的测试报告文件
    def route(self):
        lists = os.listdir(report_dir)
        lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
        return report_dir+"\\"+lists[-1]

    # 封装发送邮件
    def send_emails(self):
        send_file = open(self.route(), 'rb').read()  # 获取到文件 并打开
        att = MIMEText(send_file, "base64", "utf-8")  # 添加文件到附件    后面跟两个参数 编码 和传输格式
        att["Content-Type"] = "application/octet-stream"  # 传输格式
        att["Content-Disposition"] = 'attachment;filename="login_data.html"'  # 附件的文件名

        msgRoot = MIMEMultipart()
        msgRoot.attach(MIMEText(content, "html", "utf-8"))  # 邮件正文内容
        msgRoot["Subject"] = subject  # 邮件标题
        msgRoot["From"] = sender  # 邮件发件人
        msgRoot["To"] = receive  # 邮件收件人
        msgRoot.attach(att)  # 上传附件

        smtp = smtplib.SMTP_SSL(smtpserver, 465)  # 邮件服务器和端口
        smtp.helo(smtpserver)  # 账号密码发给服务器认证
        smtp.ehlo(smtpserver)  # 返回认证结果
        smtp.login(user, password)  # 发送邮件账号密码

        print("开始发送邮件")
        smtp.sendmail(sender, receive, msgRoot.as_string())  # 发件人  收件人  标题内容转化
        smtp.quit()
        print("发送完成")


if __name__ == '__main__':
    BasePage().send_emails()
