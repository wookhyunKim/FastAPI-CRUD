from fastapi import FastAPI

from typing import List
from starlette.middleware.cors import CORSMiddleware

# web
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
from fastapi import APIRouter, Request, Form



# .py 
from model import UserTable, User
from model import FruitTable, Fruit
from db import session


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)




@app.get('/')
def hi():
    return 'Hello World !'


# 단순 웹띄우기
@app.get("/show")
async def show_web(request: Request):
    context = {}
    names = ["Jane", "Happy", "Siri"]
    context = {"request": request, "names": names}  # currentIndex 추가
    return templates.TemplateResponse("index.html", context)


# @app.post("/insert")
# async def insert_web(request: Request):
#     context = {}
#     names = ["Jane", "Happy", "Siri"]
#     context = {"request": request, "names": names}  # currentIndex 추가
#     return templates.TemplateResponse("index.html", context)


# 단순 웹띄우기
@app.get("/show2")
def show_web(request : Request):

    return templates.TemplateResponse('test.html',{"request": request})

# 단순 웹띄우기
@app.get("/show3")
def show_web(request : Request):

    return templates.TemplateResponse('tf.html',{"request": request,'id':3})



# select all 
@app.get('/users')
def read_users():

    users = session.query(UserTable).all()

    return users

# select one
@app.get('/users/{user_id}')
def read_user(user_id : int):

    user = session.query(UserTable).filter(UserTable.id == user_id).first()

    return user

# insert
@app.post('/user')
def create_user(name:str, age: int):

    user = UserTable()
    user.name = name
    user.age = age

    session.add(user)
    session.commit()

    return f'{name} created....'


# update
@app.put('/users')
def update_users(users : List[User]):

    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.name = i.name
        user.age = i.age
        session.commit()

    return f'{users[0].name} created....'

# delete
@app.delete('/user')
def read_users(user_id : int):

    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()

    return read_users


# =================================
# select all 
@app.get('/fruits')
async def read_fruits(request:Request):

    fruits = session.query(FruitTable).all()

    return templates.TemplateResponse('table.html',{"request": request,'fruits':fruits})



# insert
@app.post('/fruit')
async def create_fruit(request: Request, name: str = Form(...), price: int = Form(...)):
        fruit = FruitTable()
        fruit.fname = name  
        fruit.fprice = price

        session.add(fruit)
        session.commit()
        return RedirectResponse(url='/fruits',status_code=302)

        # return f'{name} created....'




# update swagger
@app.put('/fruits')
async def update_fruits(fruits : List[Fruit]):

    for i in fruits:
        fruit = session.query(FruitTable).filter(FruitTable.fid == i.fid).first()
        fruit.fname = i.fname
        fruit.fprice = i.fprice
        session.commit()

    return f'{fruits[0].name} created....'

# update in web
@app.post('/update_fruit')
async def update_fruits(request: Request, id: int = Form(...),name: str = Form(...), price: int = Form(...)):

    
    fruit = session.query(FruitTable).filter(FruitTable.fid == id).first()
    fruit.fname = name
    fruit.fprice = price
    session.commit()

    return RedirectResponse(url='/fruits',status_code=302)

# delete in web
@app.post('/delete_fruit')
async def update_fruits(request: Request, id: int = Form(...)):

    
    fruit = session.query(FruitTable).filter(FruitTable.fid == id).delete()
    session.commit()

    return RedirectResponse(url='/fruits',status_code=302)
