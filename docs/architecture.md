# Architecture

## Struture

Angular (UI)
    |
REST/GraphQL API via HTTPS
    |
Python Backend (FastAPI / Django / Flask)


## Frontend

Reasons to use Angular:
- It is a full-fledged framework and richer in its capabilities than, e.g., React
- Bidirectional data binding
- MVC model
  - HTTP files
  - Components
  - Services


## Backend

Reasons to use Python:
- Python has a lot of data processing libraries
- spectrum_utils is a Python package: https://github.com/bittremieuxlab/spectrum_utils?tab=readme-ov-file

Python django:
- TODO

Versions:
- Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux 
- pip 23.3.2 from /usr/local/lib/python3.11/dist-packages/pip (python 3.11)


## API

The frontend calls the apis from the backend server.

APIs:
- notes: http://127.0.0.1:8000/api/notes/


