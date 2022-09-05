from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

# Create an instance of FastAPI
app = FastAPI()

### CRUD: Create (POST), Read (GET), Update (PUT or PATCH), Delete

# Schema: Creating a 'Post' pydantic model
class Post(BaseModel): # Post inherits 'BaseModel', which will grab the body from your HTTP request
    title: str # This will only accept 'title' and 'content', and only if they are strings
    content: str # It will reject all other data
    published: bool = True # Default value (if the user doesn't provide a value, it'll default to True)
    rating: Optional[int] = None # Optional field, default value of None

# For now, in lieu of using a database, we're gonna save the data in memory.
# 'my_posts' list:
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "food", "content": "pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


### GET operations ###
# Path Operation (aka Route)
@app.get("/") # The decorator allows you to use FastAPI with HTTP Methods,
def root():     # the Path in the "get" method is whats appended to the URL
    return {"message": "Welcome to Seba's API!"} 

# Path Operation for GETting posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts} # FastAPI automatically turns an array (my_posts) into JSON

# Get the latest post
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

# using a Path Parameter
@app.get("/posts/{id}") # Warning: because this is similar to "/posts/latests", if you put this before 'latests' it will think 'latests' is an input for 'id'
def get_post(id: int, response: Response): # error validation! if an integer is not passed in, FastAPI will throw an error
    post = find_post(id)
    if not post: # if the post doesn't exist, throw a 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: '{id}' was not found.")
    return {"post_detail": post}


### POST operations ###
# Path Operation for Creating posts
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_post: Post): # Set 'new_post' equal to the data validated by the 'Post' pydantic model
    print(new_post.title) # access only the 'title' property
    print(new_post)
    post_dict = new_post.dict() # turn the array into a dictionary; this way we can alter it
    post_dict['id'] = randrange(0, 1000) # add a new item to the dict: 'id': '<randInt>'
    my_posts.append(post_dict)

    return {"data": post_dict} 


### DELETE operations ###

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id '{id}' does not exist.")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT) #returning this because when you delete something you DONT want to send data back


### UPDATE operations (PUT, PATCH) ###

# Update an entire post (must have all required fields)
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id '{id}' does not exist.")
   
    post_dict = post.dict()
    post_dict['id'] = id # this is necessary
    my_posts[index] = post_dict # replace the post at index __ with the new post
    return {'data': post_dict}

