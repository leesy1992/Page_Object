# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:案件类表页面的元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class Case_mangage(BasePage):
    # 定位器，通过元素属性定位元素对象
    # 新建案件
    new_case=(By.XPATH,"// *[ @ id = 'app']//div[2]/div/button")
    # 案件编号
    case_id = (By.ID, "id")
    #案件名称
    case_name = (By.ID, "caseName")
    #点击创建人控件
    create_id = (By.XPATH, "//*[@id='createAcId']/div/div/div")
    #选择创建人
    create_ids = (By.XPATH, "/html/body/div[2]/div/div/div/ul/li")
    # 点击案件状态
    case_state = (By.XPATH, "//*[@id='caseState']/div/div/div")
    #选择案件状态
    case_states = (By.XPATH, "/html/body/div[3]/div/div/div/ul/li")
    #查询按钮
    check_button=(By.XPATH, "//*[@id='app']//div/span/button[1]")
    #重置按钮
    res_button = (By.XPATH, "//*[@id='app']//div/span/button[2]")
    #第一个处理按钮
    do_button=(By.XPATH, "//*[@id='app']//table/tbody/tr[1]/td[10]/span/span")



    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 输入案件编号
    def case_ids(self,caseId):
        self.element_find(*self.case_id).send_keys(caseId)
        log.logging.info("输入案件编号")

    # 输入案件名称
    def case_names(self,caseName):
        self.element_find(*self.case_name).send_keys(caseName)
        log.logging.info("输入案件名称")

    # 选择创建人
    def select_person(self,num):
        self.element_find(*self.create_id,).click()
        self.elements_find(*self.create_ids,num=num).click()
        log.logging.info("选择创建人")

    # 选择案件状态
    def select_state(self,num):
        self.element_find(*self.case_state).click()
        self.elements_find(*self.case_states,num=num).click()
        log.logging.info("选择案件状态")

    # 点击查询
    def check_cases(self):
        self.element_find(*self.check_button).click()
        log.logging.info("点击查询")

    # 点击重置
    def res_cases(self):
        self.element_find(*self.res_button).click()
        log.logging.info("点击重置")

    # 点击新建按钮按钮
    def new_cases(self):
        self.element_find(*self.new_case).click()
        log.logging.info("点击新建按钮按钮")

    # 点击处理按钮
    def do_cases(self):
        self.element_find(*self.do_button).click()
        log.logging.info("点击处理按钮")




