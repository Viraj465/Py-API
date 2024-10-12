# import the dependencies
from fastapi import FastAPI
from fastapi.params import Body #  To get data into Body of App.
from pydantic import BaseModel #  To validate data
from typing import Optional

'''
To run the server uvicorn <filename>:app *--reload* --reload is imp to auto reloading of page
'''
app = FastAPI()

# create a route
@app.get("/home") # decorator: gives path of function. modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
async def root():
    return {"message": "Hello Viraj"}

@app.get("/data")
async def retreive_data():
    return {"data": "This is the data"}

# @app.post("/posts")
# async def create_post(post:dict = Body(...)):
#     print(post)
#     return {"message": f"Post created successfully.","new_post":f"name {post['name']} App {post['App']}"}

# Person name->str, App name->str, Education->str, isStudent->bool

class Post(BaseModel):
    person_name: str
    app_name: str
    education: str
    is_student: bool = True
    rating: Optional[int] = None

@app.post("/createdata")
async def create_data(post: Post = Body(...)):
    print(post)
    print(post.__dict__)
    return {"message": f"Data created successfully.","new_data":f"Name {post.person_name}, {post.app_name}, {post.education}, {post.is_student}, {post.rating}"}

# CRUD

# To save all data.(miniature database)
my_posts = [
    {"id":1,
    "title": "title1",
    "content": "content1"},
    {"id":2,
    "title": "title2",
    "content": "content2"}
    ]

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts")
async def create_post(post:dict = Post):
    my_posts.append(post)
    print(my_posts)
    return {"data":my_posts}

def find_post(id):
    for i in my_posts:
        if i["id"]==id:
            return i
        
@app.get("/posts/{id}")
def get_post(id: int):
    posts = find_post(id)
    return posts