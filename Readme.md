# Scibids Test

This is a monorepo for Scibids test app. It contains both the front and backend

## Backend

### Flask

Backend is using Flask. In the api.py file there are 4 endpoints :

- `/documents` returns a list of all documents
- `/document/<id>` returns a list of a document by id
- `/tagsfromdoc/<id>`returns the tags associated with a document
- `/fulldocs` returns a list of all documents each with its asociated tags

## Frontend

### React

Frontend is a simple React application that fetches data from the api and displays it accordingly.

#### Dependencies

- `Tailwindcss` to make css styling faster.

## Quickstart

To run the project locally, clone the project and then follow the steps below.

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

## Code

The tricky part of this project was to display documents with their associated tags.  
To do that, I decided to do all the work on the backend and create an endpoint that returns  
the desired format which is full document (document + associated tags).  
And this is to avoid making a lot of api calls in the front.
The frontend will then call this endpoint `/fulldocs` once and then take only `document.name === "Scibids"` and now we have all the documents that we need with the desired fileds.  
Finally we will pass version 1 and version 2 in constants and use those to create the desired display through the FormatObject function.
