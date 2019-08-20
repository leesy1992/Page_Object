#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/7/25
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pytest

# #登录模块


def getUrl():
    # url="https://test.jinhui120.com/incall/#/home/index"  #测试环境地址
    url="https://ent.jinhui120.com/incall/#/home/index"    #生产环境地址
    driver=webdriver.Chrome()
    driver.maximize_window()  #最大化页面
    driver.get(url)
    sleep(20)
    #打开综合信息管理的签约医院管理页面
    driver.find_element_by_xpath("//*[@id='app']//ul/li[6]").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='app']//div/ul/li[6]/ul/li[3]").click()
    sleep(2)
    return driver

def writeFile(content,filename):
    fo=open(filename,'a+')
    fo.write(content)
    fo.close()

def getHospital():
    driver=getUrl()
    for j in range(28,124):
        for i in range(1,11):
            try:
                #输入页码跳转
                d="//*[@id='app']/div/div[2]/div[2]/div/div[2]/form/div/div/ul/li[11]/div/input"
                driver.find_element_by_xpath(d).send_keys(j)
                sleep(1)
                driver.find_element_by_xpath(d).send_keys(Keys.ENTER)
                sleep(2)
                x="//*[@id='app']//div/div/table/tbody/tr["+ str(i)+"]/td[1]"
                hospitalname = driver.find_element_by_xpath(x).text                  #获取列表的医院名称
                aa="//*[@id='app']//div/div/table/tbody/tr["+ str(i)+"]/td[6]/a[2]"
                target = driver.find_element_by_xpath(aa)
                # 利用js将定位到的元素拖动到可见区域；参数为true：调用该函数，页面发送滚动，使element的顶部与视图(容器)顶部对齐；参数为false：使element的底部与视图(容器)底部对齐
                driver.execute_script("arguments[0].scrollIntoView(false);", target)
                sleep(2)
                target.click()
                sleep(2)
                hospitalName=driver.find_element_by_id("hospitalName")
                value = driver.execute_script("return arguments[0].value", hospitalName)  #利用JS获取输入框的值
                driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div/button[1]").click()
                sleep(2)
                #页面外面的医院名称与详情页面的医院名称对比，并把结果写入到对应的文件中
                if hospitalname==value:
                    right="===============第" + str(j)+"页第" + str(i)+"行：" + hospitalname+ "一致===================="+"\n"
                    writeFile(right,"right.txt")
                else:
                    wrong="===============第"+ str(j)+"页第"+ str(i)+"行失败："+ hospitalname+ "与" + value+"不一致============="+"\n"
                    writeFile(wrong,"wrong.txt")

            except:
                wrong ="有错误出现，请注意,===============第"+ str(j)+"页第"+ str(i)+"行执行出错"+"\n"
                writeFile(wrong, "wrong.txt")
                #出错了，重新刷新页面重新进入到我们要求的页面
                driver.refresh()
                sleep(1)
                ee = driver.find_element_by_xpath("//*[@id='app']//div/ul/li[6]/ul/li[3]")
                ee.click()
                sleep(1)


if __name__ == "__main__":
    hospital=getHospital()
    # wirth=writeFile("sdsd156465"+"\n","right.txt")
    # wirt2h = writeFile("sdsd156465" + "\n", "right.txt")







