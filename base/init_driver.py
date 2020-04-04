from appium import webdriver

"""
初始化driver对象
"""
def get_driver(package, activity):
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = '4b1bd9d2'
    #支持Toast
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity
    #支持中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # desired_caps['automationName'] = 'Uiautomator2'
    # 声明driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
