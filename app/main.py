# System imports
# Libs imports
from fastapi import FastAPI, status
# Local imports
from routers import user, entreprise, activite
from auth import auth

app = FastAPI()

custom_responses = {
    200: {"description": "OK"},
    201: {"description": "Created"},
    204: {"description": "No content"},
    400: {"description": "Bad request"},
    401: {"description": "Unauthorized"},
    403: {"description": "Forbidden"},
    404: {"description": "Not found"},
}

app.include_router(user.router, tags=["users"], responses=custom_responses)
app.include_router(entreprise.router, tags=["entreprises"], responses=custom_responses)
app.include_router(activite.router, tags=["activites"], responses=custom_responses)
app.include_router(auth.router, tags=["authentication"], responses=custom_responses)