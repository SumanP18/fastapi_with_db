from fastapi import APIRouter

router = APIRouter()

@router.get("/signup   ")
def signup():
    return {"message": "user signed up successfully"}

@router.get("/login")
def login():
    return {"message": "user logged in successfully"}
    
