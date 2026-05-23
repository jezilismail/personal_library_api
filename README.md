# Personal Library API

## A simple CRUD API for managing a collection of books

[Checkout Project] project deployed on fastapi cloud: https://personal-library-api.fastapicloud.dev/docs

### Docs to Code Series - Project 1

At this day and age of AI, why am I building a CRUD app?

The idea is to only rely on documentations for learning SWE by building projects and not using AI to build projects.

I have decided to suffer this way because AI in coding has made the concept of "building projects to land jobs" totally obsolete because anyone can spin up 10 projects in a night with a base plan from Claude Code. So I feel interviewers and employers dont trust projects anymore. Attempting to build these projects by only reading docs is what I feel how I can show someone that I actually put in the effort and learned it.

_So how do I prove that I am doing this on my own?_ - well, if you really want to validate, just look at all my commits and the evolution of my code in them. Because I am only starting to learn backend engineering, I am making the most "precious" stupid mistakes and as I learn more I am correcting them in later commits. this pattern will be seen in this project - which will be nearly impossible for an AI to mimic.

I have tried to learn SWE by watching YT videos in the past but that has kept me in a comfort zone and havent learned much.

This is purely an attempt at learning software development so I wouldnt have to switch to plan mode when someone asks me to build something usefull, rather I can start writing code like the legends of the past did.

## Scope of project

Basic CRUD operations API: build routes and endpoints, handle path and query params and body in requests, handle exceptions and use status codes, use proper request-response models for validation and documentation, structure the app like a pro.

### What is implemented so far?

- now the app has the following routes:

  -> post: /book

  -> get: /book/{book_id}

  -> put: /book/{book_id}
  
  -> delete: /book/{book_id}

  -> get: /library query params for filtering books and pagination

- user can create, update, fetch and delete one book at a time from the Library
- I decided to use a JSON file to store the book data -> (The Library): this is because i had to split the main.py into a structured app as the file grew big so i thought I will store the data in a `db` folder.
- the app is well structured in this version compared to the prev commit.
- I added some basic HTTP exception handling in this version, will look into more advanced later on
- I also defined response models this time.
- Added example data for the post method.
- Since i decided to use a JSON file to store the data I was able to look into file handling and JSON methods - not deep but the stuff that I needed here.
- new /library route enables user to get books in a list with pagination and let the user filter by price and genre.

### Next what?

- I wish to include text search, i dont know yet how it should be done because what I have in mind is return the results as user is typing - I am not sure if this is done using normal requests - will look into it.

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
