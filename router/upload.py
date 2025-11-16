from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter()

class createUser(BaseModel):
    name: str
    email: str
    age: int

users = []
@router.post("/update_info")
def create_user(user: createUser):
    new_user = {
        "name" : user.name,
        "email" : user.email,
        "age" : user.age
    }
    
    users.append(new_user)
    if new_user not in users:
        raise HTTPException(status_code=500, detail="Error in storing new user details")
    
    return {"message": "Succesfully stored new user information"}