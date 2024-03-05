from fastapi import FastAPI

from typing import List

# web
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, Form



# .py 
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
