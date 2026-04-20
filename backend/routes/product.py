from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database
from auth.auth_bearer import JWTBearer

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/", dependencies=[Depends(JWTBearer())])
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

# READ ALL
@router.get("/", dependencies=[Depends(JWTBearer())])
def read_all(db: Session = Depends(get_db)):
    return crud.get_products(db)

# READ ONE
@router.get("/{product_id}", dependencies=[Depends(JWTBearer())])
def read_one(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# UPDATE
@router.put("/{product_id}", dependencies=[Depends(JWTBearer())])
def update(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated = crud.update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

# DELETE
@router.delete("/{product_id}", dependencies=[Depends(JWTBearer())])
def delete(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Deleted successfully"}