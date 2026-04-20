from pydantic import BaseModel

# -------- PRODUCT --------
class ProductCreate(BaseModel):
    name: str
    quantity: int
    price: int

class ProductUpdate(BaseModel):
    name: str
    quantity: int
    price: int

class Product(BaseModel):
    id: int
    name: str
    quantity: int
    price: int

    class Config:
        from_attributes = True


# -------- USER --------
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str