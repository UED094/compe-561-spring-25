from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body

app = FastAPI()


@app.get("/")
async def root():
    """Basic FastAPI endpoint

    Returns:
        _type_: none -- Returns a dictionary with a message key
    """

    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


BOOKS = [
    {
        "id": 0,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "genre": "Fantasy",
    },
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy",
    },
    {
        "id": 2,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "genre": "Fiction",
    },
]


@app.get("/books")
async def get_books():
    return BOOKS


@app.get("/book_names")
async def get_book_names():
    return {"book_names": [book["title"] for book in BOOKS]}


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return BOOKS[book_id]


@app.get("/sum/{a}/{b}")
async def sum(a: int, b: int):
    return {"sum": a + b}


# Add a query parameter to book endpoint
@app.get("/book")
async def get_book_by_id(book_id: int):
    return BOOKS[book_id]


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book/{book_id}")
async def update_book(book_id: int, updated_book=Body()):
    BOOKS[book_id] = updated_book


@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int):
    del BOOKS[book_id]


class Book(BaseModel):
    title: str
    name: str


class BookRequest(Book):
    author: str


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)
