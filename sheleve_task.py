import datetime
from datetime import date
import shelve

# 第一步
today = date.today()
db = shelve.open('date_shelve')
db['savetime'] = today
db.close()

# 第二步
db = shelve.open('date_shelve')
db['savetime'] = datetime.datetime.now()
db.close()

# 第三步
db = shelve.open('date_shelve')
t = db['savetime']
print(t.strftime("%Y-%m-%d %H::%M::%S"))

