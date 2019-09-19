###太原理工大学新版教务系统登入拉取成绩信息，需要连接校园网
from selenium import webdriver
import requests,time,bs4
driver = webdriver.Firefox()
driver.get('http://jxgl.tyut.edu.cn:999/')
user = driver.find_element_by_class_name("form-username")
user.send_keys("用户名")
pwd = driver.find_element_by_class_name("form-password")
pwd.send_keys("密码")
driver.find_element_by_id("btn_login").click()
driver.switch_to.frame("iframe0")
driver.find_element_by_id("Kccj").click()

driver.switch_to.default_content()   #回到上一级找内容，并列框架需要该步骤
driver.switch_to.frame("iframe125102")

cookies = driver.get_cookies()   #获取浏览器cookies
cookie = [item["name"] + "=" + item["value"] for item in cookies ]
cookiestr = ';'.join(item for item in cookie)
headers_cookie ={
           "Cookie": cookiestr         # 通过接口请求时需要cookies等信息,这样post方法就会带上浏览器的访问信息
}
data = {"order": "zxjxjhh desc,kch"}
b = requests.post("http://jxgl.tyut.edu.cn:999/Tschedule/C6Cjgl/GetKccjResult",data=data,headers=headers_cookie)
print(b.text)

