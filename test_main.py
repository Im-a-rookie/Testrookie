import pytest
import time
from selenium import webdriver
import yaml


class TestWechat(object):

    def setup(self):
        self.options = webdriver.ChromeOptions()
        self.options.debugger_address = "localhost:9222"  # 复用浏览器
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.implicitly_wait(2)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            if 'expiry' in yaml_data:
                yaml_data.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        # print(self.driver.get_cookies())

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_01(self):
        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element_by_id("username").send_keys("XXX")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("XXXX")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("XXXXXX")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("XXXXXXX")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("XXXXXXX@163.com")
        self.driver.find_element_by_link_text("保存").click()
        ast = self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[3]/td[2]')
        # print(ast.text)
        assert (ast.text == 'XXX')
        time.sleep(3)


if __name__ == '__main__':
    pytest.main(['-s'])
