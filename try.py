from fastapi import FastAPI
import pymongo
sort=[]
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['PinCodeDB']
col = db["IndianPin"]
app =FastAPI()
@app.get("/", tags=['Root'])
async def root():
    return ("data","welcome page")

@app.get('/Get_Lat&Lng')
def getlatlng(pincode:int):
    pin=str(pincode)
    for PinCode in col.find({"postal code":pin},{'_id':0}):
        sort.append(PinCode)
    return {'data':sort}
