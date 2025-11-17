# Architecture

The architural structure of the web-application:
- Angular (Frontend)
- REST API via HTTPS
- Python Backend


## Frontend: Angular

Reasons to use Angular:
- It is a full-fledged framework and rich in its capabilities
- Bidirectional data binding

Frontend elements: 
- Components define views.
- Services are called by components. They provide the background functionality, such as fetching data from the backend.
- Router services provides navigation among views.

Details on frontend see in `frontend.md`.


## Backend: Django

Reasons to use Django:

- Many built-in features, such as: ORM, admin panel, and authentication system. Therefore, for creating a new web-application for the sake of a coding task, it suits well.
- Free and open source.
- Very fast, and scalable.
- It is a Python framework. See reasons to use python below.

Reasons to use Python:
- Python has a lot of data processing and machine learning libraries
- The recommended `spectrum_utils` package is a Python package: https://github.com/bittremieuxlab/spectrum_utils?tab=readme-ov-file

Python and pip versions:
- Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux 
- pip 24.0

Details on backend see in `backend.md`.


## REST API

The connection between the frontend and the backend happens via REST API calls.

API definition: See `api.md`.


