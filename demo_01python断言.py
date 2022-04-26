# coding = utf-8
# Author: kemi
# Date: 2022/4/22

'''断言'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
# 隐式等待：只要声明一次，然后在整个python文件中都可以用，在你去定位元素/页面跳转的时候，会自动去执行这个
# 隐式等待的时间，最大的等待时间是10秒，
driver.implicitly_wait(10)
driver.get('http://erp.lemfix.com/login.html')

driver.find_element_by_id('username').send_keys('test123')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btnSubmit').click()
time.sleep(2)

# 断言：通过url来判断登录是否成功
tz_page_url = driver.current_url
print(tz_page_url)

# if tz_page_url == 'http://erp.lemfix.com/index.html':
#     print('登录成功')
# else:
#     print('登录失败')

# assert断言：如果两者相等，则不会返回任何信息；如果两者不相等，则会AssertionError报错
# assert tz_page_url == 'http://erp.lemfix.com/index.html'

# 断言：判断昵称是否为测试用例
# 1-先去定位到测试昵称这个元素
ele = driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/div[1]/div[2]/p')
# 2-获取这个元素的文本值
sj_nick_name = ele.text
# 3-判断这个文本值是否与预期结果一致
if sj_nick_name == '测试用户':
    print('登录成功，昵称正确',sj_nick_name)
else:
    print('登录失败',sj_nick_name)

time.sleep(2)
driver.quit()
