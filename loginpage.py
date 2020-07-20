from behave import *
from selenium.webdriver import chrome
from selenium import webdriver

@given('User enter the url')
def user_enter_url(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://thetestingworld.com/testings/")

@when('User enter the username "{user}" and password "{passw}"')
def step_impl(context,user,passw):
    context.driver.find_element_by_xpath("//li[2]//label[1]").click()
    context.driver.find_element_by_name("_txtUserName").send_keys(user)
    context.driver.find_element_by_name("_txtPassword").send_keys(passw)

@when('User  lick on the login button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Login']").click()

@then('User verify the My Profile page should display')
def step_impl(context):
   button= context.driver.find_element_by_xpath("//button[contains(text(),'View Me')]").text
   assert button=="View Me"


