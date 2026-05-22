# Personal Library API

## A simple CRUD API for managing a collection of books

### Docs to Code Series - Project 1

At this day and age of AI, why am I building a CRUD app?

This project was a recomendation from Claude when I asked it for project ideas that I can build by myself using just documentations and not AI, the intention is to learn backend engineering by implementation.
This is first of many projects it recommended, future projects increases in complexity.
I had asked it to come up with the projects so that by the end of this series I would become an expert software engineer(hopefully, if i ever complete them). Projects were decided based on backend engineering concepts and each project will build on top of concepts from previous ones.
This is purely an attempt at learning software development so I wouldnt have to switch to plan mode when someone asks me to build something usefull, rather I can start writing code like the legends of the past did.

## Scope of version 0.1.0

Basic CRUD operations - implemented.

**Advancing to version 0.2.0**

### What is implemented so far?

- now the app has the following routes:
  -> post: /book
  -> get: /book/{book_id}
  -> put: /book/{book_id}
  -> delete: /book/{book_id}

- user can create, update, fetch and delete one book at a time from the Library
- I decided to use a JSON file to store the book data -> (The Library): this is because i had to split the main.py into a structured app as the file grew big so i thought I will store the data in a `db` folder.
- the app is well structured in this version compared to the prev commit.
- I added some basic HTTP exception handling in this version, will look into more advanced later on
- I also defined response models this time.
- Added example data for the post method.
- Since i decided to use a JSON file to store the data I was able to look into file handling and JSON methods - not deep but the stuff that I needed here

[
note: i realised that the whole codebase was a mess and the logic werent right, i did a full rewrite of the app, I felt like starting fresh because the code looked messy but more than that it ws because i wanted to challenge myself if i can rebuild it again, this time not refering the docs unless i dont remember at all - because the prev version was mostly built at the same time i was reading the docs. and i am happy with the results!!
]

### Next what?

- I am planning to re-introduce the use of query params in a new route - with more appropriate usecase rather than what I had done before
- I will bring in more advanced search methods and other operations

### Documentations refered:

- https://fastapi.tiangolo.com/tutorial/query-params-str-validations
- https://fastapi.tiangolo.com/tutorial/body/#request-body-path-query-parameters
- https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
- https://www.w3schools.com/python/python_regex.asp
- https://fastapi.tiangolo.com/tutorial/query-param-models/
- https://fastapi.tiangolo.com/tutorial/body-multiple-params/
- https://docs.python.org/3/tutorial/datastructures.html
- https://fastapi.tiangolo.com/tutorial/response-status-code/
- https://fastapi.tiangolo.com/tutorial/schema-extra-example/
- https://fastapi.tiangolo.com/tutorial/response-model/
- https://fastapi.tiangolo.com/tutorial/handling-errors/
- https://www.geeksforgeeks.org/python/python-map-function/
- https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
- https://www.geeksforgeeks.org/python/file-handling-python/
- https://fastapi.tiangolo.com/tutorial/bigger-applications/

### Project description from Claude:

**Project 1 — Personal Library API**
A simple CRUD API for managing a collection of books. No database yet — use in-memory storage (a Python dict or list).

Concepts covered:

- FastAPI project setup and structure
- Path operations (GET, POST, PUT, DELETE)
- Path parameters and query parameters
- Pydantic models for request and response validation
- Status codes and what they mean
- HTTP request/response cycle in practice
- Basic REST principles
- Python type hints (you'll be forced into them)
- Uvicorn and running a development server
- Auto-generated docs (Swagger UI / ReDoc — FastAPI gives you this for free)

Why this project: It strips away every distraction. No database, no auth, no complexity. Just you, FastAPI, and HTTP. You will discover exactly how routing, validation, and data modeling work.
