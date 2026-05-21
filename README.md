### Personal Library API

## A simple CRUD API for managing a collection of books

# Docs to Code Series - Project 1

At this day and age of AI, why am I building a CRUD app?

This project was a recomendation from Claude when I asked it for project ideas that I can build by myself using just documentations and not AI, the intention is to learn backend engineering by implementation.
This is first of many projects it recommended, future projects increases in complexity.
I had asked it to come up with the projects so that by the end of this series I would become an expert software engineer(hopefully, if i ever complete them). Projects were decided based on backend engineering concepts and each project will build on top of concepts from previous ones.
This is purely an attempt at learning software development so I wouldnt have to switch to plan mode when someone asks me to build something usefull, rather I can start writing code like the legends of the past did.

## Scope of version 1.0

I am not using database, auth, or any other complexity. rather, data will be stored in a list or dict

- the library will have books
- user can add books
- user can get book(s) - not decided if it is text search
- user can delete books

# Project description from Claude:

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
