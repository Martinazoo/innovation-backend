from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from models.user import UserDB
from uuid import UUID
from security import get_current_user
from schemas.user import *
from security import hash_password
users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/me")
def read_current_user(user_id: UUID = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": str(db_user.id),
        "name": db_user.name,
        "surname": db_user.surname,
        "email": db_user.email,
        "bachelor_degree": db_user.bachelor_degree,
        "posX": db_user.posX,
        "posY": db_user.posY
    }

@users_router.put("/update")
def update_user(u_user: UserUpdate, user_id: UUID = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if u_user.name is not None:
        db_user.name = u_user.name
    if u_user.surname is not None:
        db_user.surname = u_user.surname
    if u_user.email is not None:
        db_user.email = u_user.email
    if u_user.password is not None:
        db_user.password = hash_password(u_user.password)
    if u_user.bachelor_degree is not None:
        db_user.bachelor_degree = u_user.bachelor_degree

    db.commit()
    db.refresh(db_user)

    return {
        "message": "User updated successfully",
        "user": {
            "id": str(db_user.id),
            "name": db_user.name,
            "surname": db_user.surname,
            "email": db_user.email,
            "bachelor_degree": db_user.bachelor_degree,
        }
    }

@users_router.put("/update_position")
def update_user_position(pos: UserUpdatePosition, user_id: UUID = Depends(get_current_user), db: Session = Depends(get_db)):

    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.posX = pos.posX
    db_user.posY = pos.posY

    db.commit()
    db.refresh(db_user)

    return {
        "message": "User position updated successfully",
        "user": {
            "id": str(db_user.id),
            "posX": db_user.posX,
            "posY": db_user.posY
        }
    }

@users_router.get("/position")
def get_user_position(user_id: UUID = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": str(db_user.id),
        "posX": db_user.posX,
        "posY": db_user.posY
    }

@users_router.delete("/delete")
def delete_user(user_id: UUID = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully"}                                                 