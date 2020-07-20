from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import Chrome


def before_scenario(context,scenario):
    context.driver=webdriver.Chrome(executable_path="..//deivers//chromedriver.exe")

def afeter_scenario(context,scenario):
    context.driver.quit()
