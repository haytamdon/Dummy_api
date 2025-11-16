from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

users = {
    "user1": {
        "name" : "John",
        "email": "john@gmail.com",
        "age": 21
    },
    "user2": {
        "name" : "Victor",
        "email": "victor@gmail.com",
        "age": 35
    }
}
@router.get("/get_info")
async def get_user_info():
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return {"message": "Fetched user details successfully", "users": users}