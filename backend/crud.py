from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    
    if existing_user:
        return None

    hashed = hash_password(user.password)
    db_user = models.User(username=user.username, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user: schemas.UserLogin):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user:
        return None
    if not verify_password(user.password, db_user.password):
        return None
    return db_user

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    
    db_product.name = product.name
    db_product.quantity = product.quantity
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    
    db.delete(db_product)
    db.commit()
    return db_product