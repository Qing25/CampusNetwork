
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, time, sys


def login(usernumber,password):
	driver = webdriver.PhantomJS()
	driver.get("https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&")
	try:
		username_elm = driver.find_element_by_name("username")
		password_elm = driver.find_element_by_name("password")
		username_elm.send_keys(usernumber)
		password_elm.send_keys(password)
	except Exception as e:
		print(e, "please retry!")
		driver.close()
	else:
		password_elm.send_keys(Keys.ENTER)
		print("------------login success!-----------")
		driver.close()


def test_net():
	url = "https://login.ecnu.edu.cn/include/auth_action.php"
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Accept": "*/*",
		"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		"Accept-Encoding": "gzip, deflate, br",
	}
	try:
		response = requests.get("https://www.baidu.com", timeout=2)
	except Exception as e:
		print(e)
		return False
	return True

if __name__ == '__main__':
	if 1 == len(sys.argv):
		usernumber = input("input your usernumber:")
		password   = input("  input your password:")
	else:
		usernumber, password = sys.argv[1], sys.argv[2]
	if test_net() is True:
		print("The campus network is connected, there's nothing you need to do!")
	else:
		login(usernumber,password)
