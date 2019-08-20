# -*-coding=utf-8
import logging
import time

class Logger(object):
    def __init__(self,path, filename):
        tlee = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.filenames=path+str(tlee)+filename
        self.logging=logging
        #设置log的格式和log打印等级
        logging.basicConfig(filename=self.filenames, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y/%m/%d %H:%M:%S %p")

if __name__ == "__main__":
     i=1
     log=Logger("../Logs/","Ulogs.log")
     log.logging.info("trsrsdfdvc dedas*---------1 %d" %i)
     log.logging.debug("trssadsa撒旦法 dedas---------2 ")
     log.logging.error("trssadsa撒旦法 dedas ---------3")
     log.logging.info("trsrsdfdvc dedas*---------7 ")
     log.logging.debug("trssadsa撒旦法 dedas---------8")
     log.logging.error("trssadsa撒旦法 dedas ---------9")




