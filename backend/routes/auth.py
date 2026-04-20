from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, database
from auth.auth_handler import signJWT

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(db, user)

    if not new_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    return new_user

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, user)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = signJWT(db_user.username)
    return {"access_token": token}