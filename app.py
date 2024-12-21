from fastapi import FastAPI, Query
from requests import get
from bs4 import BeautifulSoup

app=FastAPI()

list=[]

@app.get("/data/")
async def get_data(url:str = Query(...)):
    response = get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    print(type(list))
    for a in soup.find_all("a"):
        list.append(str(a))
        print(a)
    return {"result":list}