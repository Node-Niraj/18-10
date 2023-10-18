from fastapi import FastAPI
from models import Employee
from mongoengine import connect
import json

app =FastAPI()
connect(db="derbe",host="localhost",port=27017)
@app.get("/", tags=["Index"])
async def root():
    return ( "welcome page")

@app.get("/list_of_all_items")
async def get_list():
    emp =json.loads(Employee.objects().to_json())
    return {"data":emp}

@app.get("/list_b_y")
async def get_list(name:str):
    emp1 =json.loads(Employee.find({"name":name}).to_json())
    return {"data":emp1}

# @app.post('/add_items')
# async def add_data(model:dict)->dict:
#     models.append(model)
#     return {"data":"your data is added"}
#
# @app.put("/update_item/{id}")
# async def update_item(id:int,body:dict)->dict:
#     for model in models:
#         if int((model['id']))==id:
#           model["name"]=body["name"]
#         return {"data": f"id {id} is updated"}
#     return {"data": f"this id {id}is not in model"}
# @app.delete("/delet_item/{id}")
# async def delet_item(id:int):
#     for model in models:
#         if (model['id']==id):
#             models.remove(model)
#             return {'data': " item {id} is remove now"}
#         return {'data': "id {id} is not found in list"}
