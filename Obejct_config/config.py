#-*-coding=utf-8

# HOME_URL="https://dev.jinhui120.com/incall"  #测试地址dev环境
HOME_URL="https://test.jinhui120.com/incall"#测试地址test环境
# HOME_URL="https://ent.jinhui120.com/incall"#测试地址test环境
class Logger(object):
    path="../Logs/"   #日志生成的的地址
    filename="UI_logs.log"  #日志生成的名称

class ExcelTest(object):
    filePath = "../Parm_data/test.xlsx"  #表格的地址
    sheetName = "Sheet1"  #分页名称

class Handledoc(object):
    GET_FILES_PATH = "D:\Page_Object\Test_reports\\report\html"  # 需要压缩的文件夹
    SET_FILES_PATH = "D:\Page_Object\Test_reports\\report\html456.zip"  # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样)