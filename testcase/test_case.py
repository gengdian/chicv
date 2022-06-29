import time

from pageobject.login_page import LoginPage
import unittest


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("\n用例开始执行")

    def doCleanups(self) -> None:
        print("\n用例执行结束")

    def test_login_01(self):
        ip = LoginPage()
        ip.login_ecshop("admin", "admin", "admin")
        time.sleep(3)
        self.assertEqual(ip.get_except_result(), "退出")
