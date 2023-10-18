import pymongo
p= str(829104)
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['PinCodeDB']
col = db["IndianPin"]

#x=col.find({'postal code': p})
x=col.find({},{'_id':0})
for i in x:
  print(i)
