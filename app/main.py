from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from app.user import router

app = FastAPI(
    title="Project 1",
    description="Sample Fast API project"
)

app.include_router(router.user_router,prefix='/api')

@app.get('/')
def get_root():
    return {"index":"homepage"}



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.patch("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}