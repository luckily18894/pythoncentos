
import datetime


fivedaysago = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d_%H-%M-%S")
file = 'save_fivedaysago_time_'+fivedaysago+'.txt'
print(fivedaysago)
act = open(file, 'w')
act.write(fivedaysago)
act.close()

