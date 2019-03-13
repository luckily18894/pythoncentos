import datetime
from datetime import date
import pickle
import os

# 第一步
today = date.today()
db = {}
db['today'] = today

dbfile = open((str(today)+'.pl'), 'wb')
pickle.dump(db, dbfile)
dbfile.close()

# 第二步
fivedaysearlier = today - datetime.timedelta(days=5)
fivedayslater = today + datetime.timedelta(days=5)

dbfile = open((str(today)+'.pl'), 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['today'] = fivedayslater

dbfile = open((str(today)+'.pl'), 'wb')
pickle.dump(db, dbfile)
dbfile.close()

os.rename((str(today)+'.pl'), (str(fivedaysearlier)+'.pl'))

# 第三步
dbfile = open((str(fivedaysearlier)+'.pl'), 'rb')
db = pickle.load(dbfile)
dbfile.close()

print(db['today'])

