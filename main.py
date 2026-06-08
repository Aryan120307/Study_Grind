from fastapi import FastAPI, Path,Query,HTTPException
# from sympy import Product
from service.products import get_all_products
from pydantic import BaseModel, Field
from typing import Annotated 
from uuid import UUID
from schema.product import Product

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}

# @app.get("/products")
# def get_product():
#     return get_all_products()
@app.get("/products")
def list_products(
    name : str = Query(
        default=None, 
        description="Search products by name (case insensitive)",
        min_length=1,
        max_length=50
    ),
    sort_by_price: bool = Query(
        default=False,
        description="Sort products by price in ascending or descending order (true for ascending and false for descending",
    ),
    order :str =Query(
        default="asc",
        description="Sort order for products (asc for ascending and desc for descending ",
        pattern="^(asc|desc)$"
    ),
    limit : int = Query(
        default=5,
        description="Maximum number of products to return",
        ge=1,
        le=10,   
    ),
    offset :int =Query(
        default=0,
        description="Number of products to skip before starting to collect the result set ",
        ge=0
    )
):
    # products = get_all_products()
    # if name:
    #     products = [product for product in products if name.lower() in product["name"].lower()]
    products = get_all_products()
    if name:
        needle=name.strip().lower()
        products=[products for products in products if needle in products.get("name", " " ).lower()]
    if not products:
        raise HTTPException(status_code=404, detail="No product found matching the search criteria")
    if sort_by_price:
        reverse= order=="desc"
        products = sorted(products,key=lambda p:p.get("price",0), reverse=reverse)    
    total=len(products)
    products=products[offset:offset+limit]
    return {"total":total,"limit":limit, "products":products}
@app.get("/products/{product_uuid}")
def get_product_by_uuid(product_uuid:str = Path(
        ...,
        description=" the id of the project to retrieve ",
        example="a1f3c9b2-9d12-4f2c-8c21-91a1c2d9f101",
        max_length=36,
        min_length=36
)):
    products=get_all_products()
    for product in products:
        if product.get("uuid")==product_uuid:
            return product
    raise HTTPException(status_code=404 , detail="product not found")

@app.post("/products")
def create_product(product: Product):
    print("FUNCTION EXECUTED")
    return product
# from fastapi import FastAPI, Path, Query, HTTPException
# from pydantic import BaseModel, Field
# from typing import Annotated
# from service.products import get_all_products

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "hello world"}


# @app.get("/products")
# def list_products(
#     name: str = Query(None, min_length=1, max_length=50),
#     sort_by_price: bool = Query(False),
#     order: str = Query("asc", pattern="^(asc|desc)$"),
#     limit: int = Query(5, ge=1, le=10),
#     offset: int = Query(0, ge=0)
# ):

#     products = get_all_products()

#     if name:
#         needle = name.strip().lower()
#         products = [p for p in products if needle in p.get("name", "").lower()]

#     if sort_by_price:
#         reverse = order == "desc"
#         products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

#     total = len(products)
#     products = products[offset:offset + limit]

#     return {"total": total, "products": products}


# @app.get("/products/{product_uuid}")
# def get_product_by_uuid(product_uuid: str):
#     products = get_all_products()

#     for product in products:
#         if product.get("id") == product_uuid:
#             return product

#     raise HTTPException(status_code=404, detail="Product not found")


# class Product(BaseModel):
#     id: str
#     uuid: Annotated[str, Field(description="Unique identifier")]
#     name: str
#     price: float
#     brand: str
#     category: str


# @app.post("/products", status_code=201)
# def create_product(product: Product):
#     return product