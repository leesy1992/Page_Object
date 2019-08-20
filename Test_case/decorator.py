#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/4/24
from functools import reduce

# def f(x):
#     return x*2
import time
class te():
    def log(f):
        def fn(x):
            print("call"+f.__name__+"()")
            return f(x)
        return fn
@te.log
def f(x):
    return x*2

#python中编写无参数decorator
import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        print(t1, t2, t1 - t2)
        return r

    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(10))

#python中编写带参数decorator
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if unit=="ms":
                t=(t2-t1)*1000
            else:
                t=t2-t1
            # t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print ('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print (factorial(10))