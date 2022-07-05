import os
import sys
# 获取当前目录
basedir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(basedir)[0]
sys.path.append(rootPath)

import time  # 导入时间模块 方便创建文件时创建不同文件
import unittest
import HTMLTestRunner  # 生成HTML文件模块
from base.SendEmail import Send_Email



def zhix():
    dir = "D:\\py_project\\chicv\\testcase"  # 获取当前文件路径
    print(dir)
    suite = unittest.defaultTestLoader.discover(start_dir=dir, pattern="test_case.py")  # 获取要运行的测试用例文件
    report_dir = "D:\\py_project\\chicv\\test_report"  # 获取存放测试用例文件路径
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
    report_name = report_dir + '/' + now + "result.html"  # 拼接时间跟result生成html文件，并放在report_dir目录下
    with open(report_name, "wb") as f:  # 已二进制方式打开report_name 并把生成的数据写入创建好的HTML文件
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="test teport",
                                               description='test case result')  # 生成HTML文件  stream 调用文件   title：浏览器打开名称  description：HTML文件正文描述

        runner.run(suite)  # 运行
    f.close()

    Send_Email().send_emails()


if __name__ == '__main__':
    zhix()
