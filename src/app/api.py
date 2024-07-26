from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from main import data_values
from predict_price import predicted_price_original_scale


app = FastAPI() # <- создаем экземпляр класса
#app.mount('/static', StaticFiles(directory="static"), name="static")


route = APIRouter()
templates = Jinja2Templates(directory='templates')

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@route.get('/get_price')
def get_price(request:Request) -> dict:
   return data_values

"""@route.get('/predict_price')
def predict_price(request:Request):
   return predicted_price_original_scale"""
   
app.include_router(route)

if __name__=='__main__':
  uvicorn.run('api:app', port=8000, reload=True)