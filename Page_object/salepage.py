# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:金汇营销首页操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class saletest(BasePage):
    # 定位器，通过元素属性定位元素对象
    # 商品管理
    goodsmanage_aa=(By.XPATH,"//*[@id='app']//ul/li[1]/div[1]")
    # 商品列表
    goodslist_aa = (By.XPATH, "//*[@id='app']//div/ul/li[1]/ul/li/a")
    #输入商品名称
    goodsname_aa=(By.XPATH,"//*[@id='app']//div/span/input")
    #查询按钮
    checkbutton_aa=(By.XPATH,"//*[@id='app']//div/form/button[1]")
    #新建商品按钮
    newgoods_aa=(By.XPATH,"//*[@id='app']//div/form/button[2]")
    #新建商品页面的校验
    check_newgoods=(By.XPATH,"// *[ @ id = 'app']//div[2]/div/div[1]/h1")


    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 点击商品管理
    def check_goodsmanage(self):
        self.element_find(*self.goodsmanage_aa).click()
        log.logging.info("点击商品管理")

    # 点击商品列表
    def check_goodslist(self):
        self.element_find(*self.goodslist_aa).click()
        log.logging.info("点击商品列表")

    # 输入商品名称
    def goods_nanme(self,goodsname):
        self.element_find(*self.goodsname_aa).send_keys(goodsname)
        log.logging.info("输入商品名称")

    # 查询商品名称结果
    def check_goodsname(self):
        self.element_find(*self.checkbutton_aa).click()
        log.logging.info("查询商品名称结果")


    # 新建商品跳转
    def new_goods(self):
        self.element_find(*self.newgoods_aa).click()
        text=self.element_find(*self.check_newgoods).text
        try:
            assert u'添加商品管理'in text
            log.logging.info("新建页面打开成功")
        except :
            log.logging.error("页面打开错误")