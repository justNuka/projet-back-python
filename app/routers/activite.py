# System Imports

# Libs Imports
from fastapi import APIRouter, status, HTTPException, Response
from pydantic import BaseModel
# Local Imports
from models.activite import Activite


router = APIRouter()

# Fonctions qui seront amenées à être utilisées dans le fichier
