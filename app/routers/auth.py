from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models.user import UserDB
from schemas.user import *
from security import *
from uuid import UUID

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/register")
async def register(user: UserRegistration, db: Session = Depends(get_db)):
    e_user = db.query(UserDB).filter(UserDB.email == user.email).first()
    if e_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)

    new_user = UserDB(
        name=user.name,
        surname=user.surname,
        email=user.email,
        password=hashed_password,
        bachelor_degree=user.bachelor_degree,
        posX=0.0,
        posY=0.0
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": str(new_user.id)
    }

@auth_router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": str(db_user.id)})

    return {"access_token": access_token, "token_type": "bearer"}

