import datetime

times=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
pro = "--html=../Test_reports/" + times + "test_report.html"
print(pro)