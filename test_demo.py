from selenium import webdriver
import yaml
import time


def output_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id('menu_contacts').click()
    print(driver.get_cookies())


def add_cookie():
    """
    添加cookie
    :return:
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    cookies = [{'domain': '.qq.com', 'expiry': 1608306294, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'uH9e1iB-jooL0OYZuWZjIhmxusqxbovEy_B0PgItFL-SXL8gVPAKhlxyjiz56cUSPLt51Eao2xPdsa6W00l2JMVQ6TEVjuZf4Lc1tregFD8zfp5hraAbMKrhqb7T9ygRa7OAzKdBPUYQzQJZhDvB6kuPGD6yA-qfoC5uGH_ZXV6aAn5vTcC_lQciQWqRf5J_Lr8RehlylYdaT0Vr0hY_MRTEwRQBFbQjJXVSza5gjk2q1BFoCuCxbaho8bCmpDobtyvn0M4osKl-W0KJhVrz3g'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1608300101'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688854011475388'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688854011475388'}, {'domain': '.work.weixin.qq.com', 'expiry': 1608329757, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': '8ccdihh'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '6517060533'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1923575772, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': True, 'value': '5a7e0741335423ff'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608329757, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8ccdihh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'LBB0_phvAtPmV_x3T34cHWuQs81CLyXlOmNoUzIEJ9w91Zjnd7YiUxoAdUy0vB3h'}, {'domain': '.qq.com', 'expiry': 1608392454, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1375443505.1608131759'}, {'domain': '.qq.com', 'expiry': 1610633648, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': True, 'value': 'o0474463104'}, {'domain': '.qq.com', 'expiry': 1610633648, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': True, 'value': '00010000a33152968a2617db237f813879693ca9d9877d365a3975472c4783ad2df7c0b2a299672f90809675'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325009213174'}, {'domain': '.qq.com', 'expiry': 1921504781, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True, 'value': '1_474463104'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639388950, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1671378054, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1282484941.1607852952'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610898154, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': '6VZNmtxDGv'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '4872695808'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639836100, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1608210953,1608212536,1608225894,1608300101'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True, 'value': '6478445703447733'}, {'domain': '.qq.com', 'expiry': 1610705717, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': True, 'value': '474463104'}, {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '64781281613aa01ab19817b537bde5556cad5896748931d2165b13e117dbb333'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6656990'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': True, 'value': '474463104'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id('menu_contacts').click()
    driver.implicitly_wait(5)
    driver.quit()


def test_get_cookie():
    """
    获取cookie，序列化后存入yaml文件内
    :return:
    """
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookie = driver.get_cookies()
    print(cookie)
    with open("data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)


def test_login():
    """
    使用序列化cookie的方法进行登录
    :return:
    """
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            if 'expiry' in yaml_data:
                yaml_data.pop('expiry')
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    time.sleep(3)
    driver.find_element_by_link_text("添加成员").click()
    driver.find_element_by_id("username").send_keys("XXX")
    driver.find_element_by_id("memberAdd_english_name").send_keys("XXXX")
    driver.find_element_by_id("memberAdd_acctid").send_keys("XXXXXX")
    driver.find_element_by_id("memberAdd_phone").send_keys("XXXXXXX")
    driver.find_element_by_id("memberAdd_mail").send_keys("XXXXXXX@163.com")
    driver.find_element_by_link_text("保存").click()
    ast = driver.find_element_by_xpath('//*[@id="member_list"]/tr[3]/td[2]')
    # print(ast.text)
    assert (ast.text == 'XXX')
    time.sleep(3)


if __name__ == '__main__':
    # output_cookie()
    # add_cookie()
    # test_get_cookie()
    test_login()
