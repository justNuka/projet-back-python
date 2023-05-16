# System imports
# Libs imports
from fastapi import FastAPI, status
# Local imports
from routers import user, entreprise, planning
from tables import users, entreprises, plannings
from auth import auth

app = FastAPI()


@app.get("/init_data", tags=["init"])
def init_data():
    user.init_data()
    entreprise.init_data()
    planning.init_data()
    return {"success": True}


custom_responses = {
    404: {"description": "Not found"},
    400: {"description": "Bad request"},
    204: {"description": "No content"}
}

app.include_router(user.router, tags=["users"], responses=custom_responses)
app.include_router(entreprise.router, tags=["entreprises"], responses=custom_responses)
app.include_router(planning.router, tags=["plannings"], responses=custom_responses)
app.include_router(auth.router, tags=["authentication"], responses=custom_responses)

init_data()