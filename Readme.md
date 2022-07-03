# Scibids Test

This is a monorepo for Scibids test app. It contains both the front and backend

## Backend

### Flask

Backend is in the backend folder, in the api.py file there are 4 endpoints :

- `/documents` returns a list of all documents
- `/document/<id>` returns a list of document by id
- `/tagsfromdoc/<id>`returns the tags associated with a document
- `/fulldocs` returns a list of all documents each with its asociated tags

## Frontend

### React

Frontend is a simple React application that fetches data from the api and displays accordingly.

#### Dependencies

- `Tailwindcss` is used to write css easily

## Quickstart

To run the project locally, clone the project.

### Requirements

- npm or yarn

### Backend installation and usage

- create python venv
- run `pip install -r requirement.txt` to install reqs
- run `python api.py` to start the backend on the specified port

### Frontend installation and usage

- `cd` in the `frontend` dir
- run `npm install`
- run `npm start`
  You can now view frontend in the browser in your localhost port 3000.
