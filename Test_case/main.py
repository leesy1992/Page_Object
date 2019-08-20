#   coding=utf-8

import sys
import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
import pytest
from Test_case.doc import HandleDoc

def main():
    # pytest.main("-q base_test.py")
    print("测试开始")
    while True:
        pytest.main(['-s', '-q', "map_test.py", '--alluredir', '../Test_reports/report'])
        # 实例化HandleDoc()
        # sl = HandleDoc()
        # # sl.doc()
        # # sl.compress()
        # sl.sendemail()

    # print("测试完成")
    # pytest.main("-v -s Case_test.py")


if __name__ == "__main__":
    main()
    # pytest.main("-q new_order.py")
    # pytest.main("-q base_test.py")
    # pytest.main(['-s', '-q',"new_order.py","base_test.py",'--alluredir', '../Test_reports/report'])
    # #实例化HandleDoc()
    # sl = HandleDoc()
    # sl.doc()
    # sl.compress()
    # sl.sendemail()
    #'''allure generate【reprot目录】-0 【report目录下加上html目录】''