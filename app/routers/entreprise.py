# System Import

# Libs Imports
from fastapi import APIRouter, status, HTTPException, Response
from sqlalchemy import text
# Local Imports
from models.entreprise import Entreprise
from config.db import conn

router = APIRouter()

@router.get("/entreprises")
def getEntreprise() -> list[Entreprise]:
    """
    Récupérer toutes les entreprises
    Vérifie si la liste est vide, si oui, retourne un code 204
    """
    if len(entreprises) == 0:
        return Response(status_code=204)
    return entreprises


@router.get("/entreprises/search")
async def getEntrepriseByFirmName(nameFirm: str):
    """
    Récupérer une entreprise par son nom
    """
    return list(filter(lambda x: x["name"] == nameFirm, entreprises))


@router.post("/entreprises", status_code=status.HTTP_201_CREATED)
async def createEntreprise(entreprise: Entreprise) -> Entreprise:
    """
    Créer une entreprise
    """
    if entreprise.firmName.lower() in [(entreprise["firmName"]).lower() for entreprise in entreprises]:
        raise HTTPException(status_code=400, detail="Firm name already used")
    entreprise.id = entreprises[-1]["id"] + 1
    entreprise.append(entreprise.__dict__)
    return entreprise


@router.delete("/entreprise/{entrepriseId}")
async def deleteEntrepriseById(entrepriseId: int) -> Entreprise:
    """
    Supprimer une entreprise par son id
    """
    oldEntreprise = list(filter(lambda x: x["id"] == entrepriseId, entreprises))
    entreprises.remove(oldEntreprise[0])
    return oldEntreprise[0]


@router.put("/entreprises/{entrepriseId}")
async def updateEntrepriseById(entrepriseId: int, user: Entreprise) -> Entreprise:
    """
    Mettre à jour une entreprise par son id
    """
    oldUser = list(filter(lambda x: x["id"] == entrepriseId, entreprises))
    entreprises.remove(oldUser[0])
    entreprises.append(user.__dict__)
    return Entreprise


@router.patch("/entreprises/{entrepriseId}")
async def updateEntrepriseById(entrepriseId: int, entreprise: EntrepriseOptionnalFields) -> Entreprise:
    """
    Mettre à jour une entreprise par son id
    """
    oldEntreprise = list(filter(lambda x: x["id"] == entrepriseId, entreprises))

    entreprises.remove(oldEntreprise[0])

    if entreprise.firmName is not None:
        oldEntreprise[0]["nameFirm"] = entreprise.firmName
    if entreprise.location is not None:
        oldEntreprise[0]["location"] = entreprise.location

    entreprises.append(oldEntreprise[0].__dict__)
    return oldEntreprise[0]