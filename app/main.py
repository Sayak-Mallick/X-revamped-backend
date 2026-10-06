from fastapi import FastAPI

app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author": "Sayak Mallick",
        "title": "Post 1",
        "content": "This is the content of post 1",
        "created_at": "2025-05-22",
    },
    {
        "id": 2,
        "author": "Shubhajit Mallick",
        "title": "Post 2",
        "content": "This is the content of post 2",
        "created_at": "2025-05-22",
    },
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/posts")
async def get_posts():
    return posts
   