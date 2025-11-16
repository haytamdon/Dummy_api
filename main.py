from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.get_info import router as get_info
from router.upload import router as upload
app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"message": "FastAPI is working!"}

app.include_router(get_info, prefix="")
app.include_router(upload)