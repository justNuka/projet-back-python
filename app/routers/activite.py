# System Import

# Libs Imports
import hashlib
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
import rsa
from pydantic import Depends
# Local Imports
from models.activite import Activite
from models.user import User
from config.db import conn
from auth.auth import is_maintainer 
from auth.auth import entreprise
from auth.auth import decode_token

router = APIRouter()

# Fonctions qui seront amenées à être utilisées dans le fichier

"""
Fonction qui permet de vérifier si une activité avec le même title existe déjà dans l'entreprise
"""
def activite_exists(title: str, entreprise: int) -> bool:
    query = text("SELECT COUNT(*) FROM activites WHERE title = :title AND entreprise=entreprise")
    result = conn.execute(query, title=title, entreprise=entreprise)

    """
    Récupérer le nombre de lignes retournées par la requête
    result.fetchone() retourne une seule ligne à la fois
    """

    count = result.fetchone()[0]
    return count > 0

def get_activite_by_id(activite_id: int) -> Activite:
    """
    Récupérer une activite par son ID
    """
    query = text("SELECT title, entreprise, user, created_by, start_date, end_date, description, city, address, zipCode, country FROM activites WHERE id = :activite_id")
    result = conn.execute(query, activite_id=activite_id)
    data = result.fetchone()

    if data is None:
        return None

    activite = Activite(
        title=data[0]
        entreprise=data[1]
        user=data[2]
        created_by=data[3]
        start_date=data[4]
        end_date=data[5]
        description=data[6]
        city=data[7]
        address=data[8]
        zipCode=data[9]
        country=data[10]
    )

    return activite


@router.get("/activites")
def get_all_entreprises():
    """
    Récupérer toutes les activités
    """
    entrepriseConnectee = entreprise
    query = text("SELECT title, entreprise, user, created_by, start_date, end_date, description, city, address, zipCode, country FROM activites WHERE entreprise = :entrepriseConnectee")
    result = conn.execute(query)
    data = result.fetchall()

    entreprises = []
    for row in data:
        name_firm = row[0]
        location = row[1]

        entreprise = {
            "nameFirm": name_firm,
            "location": location,
        }

        entreprises.append(entreprise)

    return entreprises


@router.get("/entreprises/search")
def get_entreprises_by_firm_name(firm_name: str):
    """
    Récupérer les entreprises par nom d'entreprise (firmName)
    """
    query = text("SELECT nameFirm, location FROM entreprises WHERE nameFirm = :firm_name")
    result = conn.execute(query, firm_name=firm_name)
    data = result.fetchall()

    entreprises = []
    for row in data:
        name_firm = row[0]
        location = row[1]

        entreprise = {
            "nameFirm": name_firm,
            "location": location,
        }

        entreprises.append(entreprise)

    return entreprises

@router.post("/entreprises")
def create_entreprise(firmName: str, location: str):
    """
    Créer un nouvel utilisateur
    """
    if entreprise_exists(firmName=firmName):
        raise HTTPException(status_code=409, detail="Une entreprise avec même nom existe déjà")

    # Préparation de la requête SQL
    query = text("INSERT INTO entreprises (firmName, location) VALUES (:firmName, :location)")
    
    # Exécution de la requête SQL
    try:
        conn.execute(query, firmName=firmName, location=location)
        return {"message": "Entreprise créée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/entreprises/{entreprise_id}")
def delete_entreprise(entreprise_id: int):
    """
    Supprimer une entreprise
    """
    query = text("DELETE FROM entreprises WHERE id = :entreprise_id")
    try:
        conn.execute(query, entreprise_id=entreprise_id)
        return {"message": "Entreprise supprimée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/entreprises/{entreprise_id}")
def update_entreprise(entreprise_id: int, firmName: str, location: str):
    """
    Mettre à jour une entreprise
    """
    query = text("UPDATE entreprises SET firmName = :firmName, location = :location WHERE id = :entreprise_id")
    try:
        conn.execute(query, firmName=firmName, location=location, entreprise_id=entreprise_id)
        return {"message": "Entreprise mise à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/entreprises/{entreprise_id}")
def partial_update_entreprise(entreprise_id: int, entreprise_data: dict):
    """
    Mettre à jour partiellement une entreprise par son ID
    """
    existing_entreprise = get_entreprise_by_id(entreprise_id)
    if not existing_entreprise:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # Récupérer les données existantes de l'entreprise
    firmName = existing_entreprise.firmName
    location = existing_entreprise.location

    # Mettre à jour les champs spécifiés dans entreprise_data
    if "firmName" in entreprise_data:
        name = entreprise_data["firmName"]
    if "location" in entreprise_data:
        surname = entreprise_data["location"]

    query = text("UPDATE entreprises SET firmName = :firmName, location = :location WHERE id = :entreprise_id")
    try:
        conn.execute(
            query,
            firmName = firmName,
            location = location,
            entreprise_id=entreprise_id,
        )
        return {"message": "Entreprise mise à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))