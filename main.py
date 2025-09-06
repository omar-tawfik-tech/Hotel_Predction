from fastapi import FastAPI ,Query
from pydantic import BaseModel,Field
from typing import Union
from typing_extensions import Annotated
app = FastAPI()

products_dp =[
 {"id":1, "name":"Laptop",'price':10000},
 {"id":2, "name":"Phone",'price':5000}
]
@app.get("/")
async def root(): # End Point

 return {"message":"Welcome To The E-Commerce API!"}

@app.get("/products")
async def Get_products(): # End Point

 return {"Products":products_dp}

class Product(BaseModel):

 name : str = Field(title="The Name Of Product",max_length=20,min_length=3)
 price : float 
 description: Union[str,None] = None

@app.post("/products")
async def Add_Product(product:Product):
 id = len(products_dp) +1
 name = product.name
 price = product.price
 descirption = product.description

 products_dp.append({"id":id,"Name":name,"Price":price,'descirption':descirption})
 return{"Message":"Product Added Succsesfully","product: ":product}


def find_product_id(product_id):
 for product in products_dp:
     if product["id" ]== product_id:
         return product
     else:
         return None
@app.get("/products/{product_id}")
async def Get_Product(product_id:int):
 product = find_product_id(product_id)
 if product is not None:
     return {"Message":"Product Retrived Succesfully","product":product}
 else:
     {"Message":"Product Not Found"}


@app.get("/Search")
async def Search_Product(search_query:Annotated[Union[str,None],Query(min_length=3)]=None, min_price:Annotated[Union[float,None],Query(ge=0)]=None):
   if search_query:
     search_result =[product for product in products_dp if search_query.lower() in product['name'].lower()]
   else:
     search_result = products_dp

   if min_price:
     search_result =[product for product in search_result if min_price in product['price']>=min_price]
 

   return{"Search Results: ": search_result}

