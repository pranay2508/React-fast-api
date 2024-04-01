from fastapi import FastAPI 
from tortoise.contrib.fastapi import register_tortoise
from models import (supplier_pydantic,supplier_pydanticIn , Supplier)

app = FastAPI()
@app.get('/')
def index():
    return {"Msg":"Hello you can go to /docs for api documnentation hello "}

@app.post('/supplier')
async def add_supplier(supplier_info:supplier_pydanticIn): # type: ignore
    supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset = True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status":"ok" , "data":response}


@app.get('/supplier')
async def get_all_suppliers():
    response = await supplier_pydantic.from_queryset(Supplier.all())
    return {"status":"ok" , "data":response}

register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)