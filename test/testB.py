import datetime

a ='2018-02-20'
b ='2018-03-20'
startTime = datetime.datetime.strptime(a, '%Y-%m-%d')
endTime = datetime.datetime.strptime(b, '%Y-%m-%d')
print(startTime-endTime)