from Models.models import ItemsModel
from CRUD.Items import get_items,create_items,delete_items,get_categories_total
from fastapi import APIRouter

Items_router = APIRouter()

x = 1 # replace with token value in the future
##############################################
@Items_router.get("/api/items/")
async def get_items_t():
    if x == 1:
        return await get_items()
    return {'message':'Invalid token'}
####################################################
@Items_router.post("/api/items/")
async def create_items_t(items: ItemsModel):
    if x == 1:
        return await create_items(items)
    return {'message':'Invalid token'}
####################################################
@Items_router.delete("/api/items/{item_id}")
async def delete_items_t(item_id: int):
    if x == 1:
        return await delete_items(item_id)
    return {'message':'Invalid token'}
####################################################
@Items_router.get("/api/items/categories/")
async def get_categories_total_t():
    if x == 1:
        return await get_categories_total()
    return {'message':'Invalid token'}
####################################################