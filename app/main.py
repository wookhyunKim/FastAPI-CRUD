from fastapi import FastAPI

from typing import List
# from starlette.middleware.cors import CORSMiddleware

# web
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
from fastapi import APIRouter, Request, Form



# .py 
# from model import UserTable, User
# from model import FruitTable, Fruit
# from db import Databases
from functions import CRUD


# 라이브러리
# ====================================================================================


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app= "main:app", # main.py 에서 app 객체 실행
        # host = "0,0,0,0",
        host = "127.0.0.1",
        port = 8000,
        reload = True, # 서버 실행 파일이 수정되면 서버를 자동 재시작    보통 개발 환경에서 사용
        # workers = 4 # 4개의 process를 미리 구동
        workers = -1
    )
    


router = APIRouter()
templates = Jinja2Templates(directory="static")



app = FastAPI()
db = CRUD()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )




@app.get('/')
def hi():
    return 'Hello World !'






@app.post('/insert')
async def insert_action(fname: str, fprice: int):
    rs = db.insertDB(table='fruit', column='fname, fprice', data=(fname, fprice))

    if rs:
        return {'message': 'Data inserted successfully'}
    else:
        return {'message': 'Failed to insert data'}
    

    
@app.get('/select/all')
async def select_all():
    rs,result = db.readDB_All(table='fruit',column='*')

    if rs:
        result
        return {'result': result ,'message': 'Data select successfully'}
    else:
        result
        return {'result': result ,'message': 'Failed to select data'}


@app.get('/select/one/{fid}')
async def select_one(fid:int):
    rs,result = db.readDB_One(table='fruit',column='*',fid =fid)

    if rs:
        result
        return {'result': result ,'message': 'Data select successfully'}
    else:
        result
        return {'result': result ,'message': 'Failed to select data'}
    


# update
@app.put('/update')
async def update_action(fid:int,fname:str,fprice:int):

    table = 'fruit'

    
    rs = db.updateDB(table,fname,fprice,fid)

    if rs:
        return {'message': 'Data update successfully'}
    else:
        return {'message': 'Failed to update data'}
    




# delete
@app.delete('/delete')
def delete_action(fid : int):

    rs = db.deleteDB(table='fruit',fid=fid)
    if rs:
        return {'message': 'Data delete successfully'}
    else:
        return {'message': 'Failed to delete data'}































# # 단순 웹띄우기
# @app.get("/show")
# async def show_web(request: Request):
#     context = {}
#     names = ["Jane", "Happy", "Siri"]
#     context = {"request": request, "names": names}  # currentIndex 추가
#     return templates.TemplateResponse("index.html", context)



# @app.post("/insert")
# async def insert_web(request: Request):
#     context = {}
#     names = ["Jane", "Happy", "Siri"]
#     context = {"request": request, "names": names}  # currentIndex 추가
#     return templates.TemplateResponse("index.html", context)


# # 단순 웹띄우기
# @app.get("/show2")
# def show_web(request : Request):

#     return templates.TemplateResponse('test.html',{"request": request})

# # 단순 웹띄우기
# @app.get("/show3")
# def show_web(request : Request):
#     context = {}
#     context = {"request": request,'id':3}
#     return templates.TemplateResponse('tf.html',context)



# # select all 
# @app.get('/users')
# def read_users():

#     users = session.query(UserTable).all()

#     return users

# # select one
# @app.get('/users/{user_id}')
# def read_user(user_id : int):

#     user = session.query(UserTable).filter(UserTable.id == user_id).first()

#     return user

# # insert
# @app.post('/user')
# def create_user(name:str, age: int):

#     user = UserTable()
#     user.name = name
#     user.age = age

#     session.add(user)
#     session.commit()

#     return f'{name} created....'


# # update
# @app.put('/users')
# def update_users(users : List[User]):

#     for i in users:
#         user = session.query(UserTable).filter(UserTable.id == i.id).first()
#         user.name = i.name
#         user.age = i.age
#         session.commit()

#     return f'{users[0].name} created....'

# # delete
# @app.delete('/user')
# def read_users(user_id : int):

#     user = session.query(UserTable).filter(UserTable.id == user_id).delete()
#     session.commit()

#     return read_users


# # =================================
# # select all 
# @app.get('/fruits')
# async def read_fruits(request:Request):

#     context = {}

#     fruits = session.query(FruitTable).all()

#     context = {"request": request,'fruits':fruits}
    
#     return templates.TemplateResponse('table.html',context)



# # insert
# @app.post('/fruit')
# async def create_fruit(request: Request, name: str = Form(...), price: int = Form(...)):
#         fruit = FruitTable()
#         fruit.fname = name  
#         fruit.fprice = price

#         session.add(fruit)
#         session.commit()
#         return RedirectResponse(url='/fruits',status_code=302)

#         # return f'{name} created....'




# # update swagger
# @app.put('/fruits')
# async def update_fruits(fruits : List[Fruit]):

#     for i in fruits:
#         fruit = session.query(FruitTable).filter(FruitTable.fid == i.fid).first()
#         fruit.fname = i.fname
#         fruit.fprice = i.fprice
#         session.commit()

#     return f'{fruits[0].name} created....'

# # update in web
# @app.post('/update_fruit')
# async def update_fruits(request: Request, id: int = Form(...),name: str = Form(...), price: int = Form(...)):

    
#     fruit = session.query(FruitTable).filter(FruitTable.fid == id).first()
#     fruit.fname = name
#     fruit.fprice = price
#     session.commit()

#     return RedirectResponse(url='/fruits',status_code=302)

# # delete in web
# @app.post('/delete_fruit')
# async def update_fruits(request: Request, id: int = Form(...)):

    
#     fruit = session.query(FruitTable).filter(FruitTable.fid == id).delete()
#     session.commit()

#     return RedirectResponse(url='/fruits',status_code=302)
