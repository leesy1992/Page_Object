#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/4/1
import  time as t

class MyTime():
    def __init__(self):
        self.unit=['年','月','日','时','分','秒']
        self.prompt="为开始计时！"
        self.lasted=[]
        self.begin=0
        self.end=0

    def __str__(self):
        return self.prompt

    __repr__=__str__

    def __add__(self, other):
        prompt="总共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+self.unit[index])
        return  prompt



    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.prompt="提示：请先使用stop（）停止计时！"
        print("计时开始！")

    def stop(self):
        if not self.begin:
            self.prompt = "提示：请先使用start（）停止计时！"
            print("提示：请先使用start（）停止计时！")

        else:
            self.end=t.localtime()

            print(self.end)
            self._calc()
            print("计时结束")


    def _calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt+=(str(self.lasted[index])+self.unit[index])
                print(self.prompt)



if __name__=="__main__":
    ss=MyTime()
    ss.stop()
    ss.start()
    t.sleep(3)

    ss.stop()
    print(ss)
