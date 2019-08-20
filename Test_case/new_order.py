# coding=utf-8
'''
Created on 2018-10-28
@author: Lee
Project:使用unittest框架编写测试用例。使用pytest执行
'''
import unittest,pytest,allure
import ddt
from selenium import webdriver
from time import sleep
from Page_object.loginpage import Logintest
from Page_object.read_excle import  ExcelTest
from Page_object.case_list import Case_mangage
from Page_object.case_edit import Case_edit
from Page_object.case_add import Case_add
from Page_object.before import New_Before
from Page_object.incall import in_Call
from Page_object.doctor import Doctors
from Logs.logs import Logger
import Obejct_config.config as cfg
from Page_object.base_processed import Base_proce
from Test_case.dc_reject import Case_state

# 测试数据
data = ExcelTest(cfg.ExcelTest.filePath, cfg.ExcelTest.sheetName)
testData = data.dict_data()
# 实例化log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

@ddt.ddt
class Casejinhui120(unittest.TestCase):
    """
          登录金汇120的case
    """
    @classmethod
    def setUpClass(cls):
        #初始化浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(0)
        cls.url = cfg.HOME_URL
        cls.base=Base_proce(cls.driver, cls.url, u"金汇")
        cls.login_page = Logintest(cls.driver, cls.url, u"金汇")
        cls.case_page = Case_mangage(cls.driver, cls.url, u"金汇")
        cls.case_add = Case_add(cls.driver, cls.url, u"金汇")
        cls.case_edit = Case_edit(cls.driver, cls.url, u"金汇")
        cls.before = New_Before(cls.driver, cls.url, u"金汇")
        cls.call = in_Call(cls.driver, cls.url, u"金汇")
        cls.base=Base_proce(cls.driver, cls.url, u"金汇")
        cls.doctor=Doctors(cls.driver, cls.url, u"金汇")
        cls.Case = Case_state(cls.driver, cls.url, u"金汇")
        # 登录
        cls.login_page.open()
        cls.login_page.input_username("lishaoyang")
        cls.login_page.input_password(123456)
        cls.login_page.input_passcode(6666)
        cls.login_page.button_submit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 用例执行体
    # @allure.feature  # 用于定义被测试的功能，被测产品的需求点
    # @allure.story  # 用于定义被测功能的用户场景，即子功能点
    # with allure.step  # 用于将一个测试用例，分成几个步骤在报告中输出
    # allure.attach  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
    # @pytest.allure.step  # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤


    @ddt.data(*testData)
    @allure.feature("工单流程")
    @allure.story("新建院前工单")
    def test_sale_AA(self,data):     #新建院前工单
        with allure.step("进入案件新建院前"):
            #进入案件
            sleep(2)
            self.driver.refresh()
            sleep(0.5)
            self.call.case_mages()
            sleep(1)
            self.case_page.do_cases()
            sleep(1)
            self.case_edit.add_Before()
        with allure.step("填写院前工单信息"):
            #填写院前工单信息
            self.before.patient_Name(data["patient"])
            self.before.patient_Age(data["age"])
            sleep(2)
            self.before.Source()
            # self.before.Upload()
            self.before.disease_Desc(data["Dis_decribe"])
            self.before.palce_Name(data["accident"])
            self.before.palce_Jd("E121","34","3.86")
            self.before.palce_Wd("N31","14","44.74")
            self.before.hospital_Info(data["Out_hospital"],data["Out_adress"],"E121","31","26.80","N31","16","44.76")
            sleep(2)
            self.before.local_Info("上海测试基地")
            self.before.Doctor()
            sleep(1)


    @ddt.data(*testData)
    @allure.feature("工单流程")
    @allure.story("医务官处理工单")
    def test_sale_BB(self,data):     #医务官处理工单
        with allure.step("进入到医务官处理页面"):
            #医务官处理信息
            sleep(2)
            self.driver.refresh()
            self.call.processed_Order()
            sleep(2)
            self.Case.Refer_State(num=1)
            self.call.first_Order()
            sleep(2)
        with allure.step("医务官处理接单拒单操作"):
            if data["idea"]:
                self.doctor.Order_reject()
                sleep(2)
                self.doctor.Order_take()
                self.doctor.Dc_ideas(data["Dc_idea"])
                self.doctor.Next_step()
                sleep(1)
                self.call.processed_Order()
                self.call.first_Order()
                sleep(1)
                self.driver.get_screenshot_as_file("D:/Page_Object/Test_reports/image/baidu_img.png")
                sleep(2)
            else:
                self.doctor.Order_reject()
                sleep(2)
                self.doctor.Dc_ideas(data["Dc_idea"])
                self.doctor.Next_step()
                sleep(1)
                self.call.processed_Order()
                self.call.first_Order()
                sleep(1)
                self.driver.get_screenshot_as_file("D:/Page_Object/Test_reports/image/baidu_img.png")
                sleep(2)

if __name__ == "__main__":
    pytest.main("--html=test_report.html")









