import time
import unittest
import ddt

import openpyxl as openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By


def read_excel():
    data1 = openpyxl.load_workbook(r'D:\fuxi\common\login_data.xlsx')
    table = data1['login']

    a = []
    for rows in range(2, table.max_row + 1):
        b = []
        for cols in range(2, table.max_column + 1):
            b.append(table.cell(rows, cols).value)
        a.append(b)
    return a


@ddt.ddt
class TestCase(unittest.TestCase):
    @ddt.data(*read_excel())
    @ddt.unpack
    def test_login_01(self, a, b, c

                      ):
        driver = webdriver.Chrome()
        driver.get('http://localhost/')
        driver.find_element(By.NAME, "username").send_keys(a)
        driver.find_element(By.NAME, "password").send_keys(b)
        driver.find_element(By.NAME, "Submit").click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
