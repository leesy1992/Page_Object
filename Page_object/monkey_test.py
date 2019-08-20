#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/8/16
"""猴子吃桃问题。猴子第一天摘下若干个桃子，当即吃了一半，又多吃了一个。
以后每天都吃了前一天剩下的一半多一个。到第10天想再吃时，只剩1个桃子了。求第一天共摘了多少个桃子。
"""
peach=0
end=True
while  end:
    peach+=1
    _peach=peach
    for i in range(9):
        if _peach%2!=0:
            break
        _peach /=2
        _peach-=1

    else:
        if _peach==1:
            print(peach)
            end=False
"""题目：找出斐波那契数列中包含0~9的连续10个数字。
斐波那契数列大家都很熟悉，1, 1, 2, 3, 5, 8, 13, 21, 34, 55......
如果把这些数量组成一个字符串就成为：'11235813213455'，这里面'2134'是包含1234这四个数字的，继续下去可以找到第一个含有0~9这10个数字的地方（10个数字的次序随意），
可能处于一个斐波那契数，有可能跨越2个或多个斐波那契数，现在要求你找到它，并打印出这十个数字，例如：9034621587
"""
a1 = 1
a2 = 1
nums = ''
end=True
while end:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    nums += str(a3)
    for i in range(len(nums)):
        temp = nums[i:i+10]
        if len(set(temp)) == 10:
            print(temp)
            nums = nums[i+1:]
            end=False
"""           
建立一个函数mysum，参数为不确定个数的正整数、负整数或零，返回一个字符串为各个数字加法的算式和结果，例如：
print(mysum(-7, 12,83, -99, 22, 0, 1))
输出：
-7+12+83-99+22+0+1=12
注意：-99前不要加号，如果实在不会写，也可以先写成+-99

提示，函数的参数数量不确定，可以使用收集参数。
"""

def mysum(*args):
    result=str(args[0])
    print(args[1:])
    for i in args[1:]:
        if i >=0:
            result +="+" + str(i)
        else:
            result += str(i)
    result += "=" + str(sum(args))
    return result

print(mysum(-7))

"""编写一个函数，参数为一个整数n。利用递归获取斐波那契数列中的第n个数并且返回。"""

# def fib(n=3):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# n = int(input("请输入你想要的数字:  "))
# while True:
#     if n>=50:
#          n=int(input("你输入的过大，请重新输入你想要的数字:  "))
#
#     else:
#         print(fib(n))
#         break

"""
   我们知道1的阶乘是1，2的阶乘是2，3的阶乘是6，4的阶乘是24，将前4个数字的阶乘排在一起是12624，
   现在要求将1~50的阶乘排在一起打印出来，要求，每40个数字1行，当本行超过40个时换行到下一行，
   另外在每行的开头打印行号。
"""
# i=50
s=1
num = ''
for i in range(1,51):
    s *=i
    num+=str(s)
i=0

while len(num)>0:
    i+=1
    print("(%2d)" %i ,end='  ')
    print(num[:40])
    num=num[40:]
# for n in range(len(num)//40+1):
    # i+=1
    # print(num[(i-1)*40:i*40])


"""小球从最高处逐层落下，每个节点都有可能向左下或右下方向下落，且几率相同，各占50%，
共有10万个小球依次落下，当都从第0层落至第9层时图中0~9的10个位置各有多少个小球
（这里为了与python一致，都是从0开始的）。
"""
import random as r
counts = [0] * 10
for i in range(10000):
    position = 0
    for j in range(9):
        move = r.choice((0, 1))
        position += move
    counts[position] += 1
print(counts)

"""古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？"""

def rabbit(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return rabbit(n-1)+rabbit(n-2)

rabbit=rabbit(3)
print(rabbit)


"""一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"""


def hight(n,h):
    s = h / 2
    for i in range(n):
        h +=2*s
        s=s/2
    return s,h

hight=hight(2,100)
print(hight)

"""打印中文乘法口诀表"""

for i in range(1,10):
    for j in range(1,i+1):

        print(j, "*", i, "=", i * j, "\t", end='')     #如果不想换行可以用 print(xxx,end='');    print函数默认换行，是end='\n'在起作用
    print("")

def character(i, j):
    characters = ",一,二,三,四,五,六,七,八,九,十"
    characters = characters.split(',')
    string = characters[i] +  characters[j]
    result = i * j
    if result < 10:
        string += '得'
        string += characters[result]
    else:
        string += characters[result // 10] + '十' + characters[result % 10]
    return(string)

for i in range(1, 10):
    for j in range(1, i+1):
        temp = character(j, i)
        print(temp ,"\t",end=' ')
    print()















