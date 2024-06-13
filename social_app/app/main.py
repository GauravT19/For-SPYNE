from fastapi import FastAPI
from app.routers import users, discussions, comments, likes, hashtags, auth
from app.utils.database import Base, engine

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(discussions.router)
app.include_router(comments.router)
app.include_router(likes.router)
app.include_router(hashtags.router)

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
