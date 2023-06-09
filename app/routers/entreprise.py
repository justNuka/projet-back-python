# System Import

# Libs Imports
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from pydantic import Depends
# Local Imports
from models.entreprise import Entreprise
from models.user import User
from config.db import conn
from auth.auth import role , decode_token, entrepriseConnectee

router = APIRouter()

# Fonctions qui seront amenées à être utilisées dans le fichier

"""
Fonction qui permet de vérifier si une entreprise avec le meme nom
"""
def entreprise_exists(firmName: str) -> bool:
    query = text("SELECT COUNT(*) FROM entreprises WHERE firmName = :firmName)")
    result = conn.execute(query, firmName=firmName)

    """
    Récupérer le nombre de lignes retournées par la requête
    result.fetchone() retourne une seule ligne à la fois
    """

    count = result.fetchone()[0]
    return count > 0

def get_entreprise_by_id(entreprise_id: int) -> Entreprise:
    """
    Récupérer une entreprise par son ID
    """
    query = text("SELECT firmName, location FROM entreprises WHERE id = :entreprise_id")
    result = conn.execute(query, entreprise_id=entreprise_id)
    data = result.fetchone()

    if data is None:
        return None
    
    entreprise = Entreprise(
        id=entreprise_id,
        firmName=data[0],
        location=data[1],
    )

    return entreprise

@router.get("/entreprises", user: User = Depends(decode_token))
def get_all_entreprises():
    """
    Récupérer toutes les entreprises
    """
    query = text("SELECT nameFirm, location FROM entreprises")
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
def get_entreprises_by_firm_name(firm_name: str, user: User = Depends(decode_token)):
    """
    Récupérer les entreprises par nom d'entreprise (firmName)
    """
    # Vérification du rôle
    if user.role != "admin" or user.role != "maintainer":
        raise HTTPException(status_code=403, detail="Vous n'avez pas les droits nécessaires pour effectuer cette action")
    
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
def create_entreprise(firmName: str, location: str,  user: User = Depends(decode_token)):
    """
    Créer une nouvelle entreprise
    """
    # Vérifier si l'entreprise existe déjà
    if entreprise_exists(firmName=firmName):
        raise HTTPException(status_code=409, detail="Une entreprise avec même nom existe déjà")
    
    # Vérification du rôle
    if user.role != "admin" or user.role != "maintainer":
        raise HTTPException(status_code=403, detail="Vous n'avez pas les droits nécessaires pour effectuer cette action")

    # Préparation de la requête SQL
    query = text("INSERT INTO entreprises (firmName, location) VALUES (:firmName, :location)")
    
    # Exécution de la requête SQL
    try:
        conn.execute(query, firmName=firmName, location=location)
        return {"message": "Entreprise créée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/entreprises/{entreprise_id}")
def delete_entreprise(entreprise_id: int,  user: User = Depends(decode_token)):
    """
    Supprimer une entreprise par son ID
    """
    existing_entreprise = get_entreprise_by_id(entreprise_id)
    if not existing_entreprise:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    # Vérification du rôle
    if user.role != "admin" or user.role != "maintainer":
        raise HTTPException(status_code=403, detail="Vous n'avez pas les droits nécessaires pour effectuer cette action")

    # Vérification de l'ID de l'entreprise
    if user.entreprise != existing_entreprise.entreprise:
        raise HTTPException(status_code=403, detail="Vous n'êtes pas autorisé à modifier cette entreprise")
    
    query = text("DELETE FROM entreprises WHERE id = :entreprise_id")
    try:
        conn.execute(query, entreprise_id=entreprise_id)
        return {"message": "Entreprise supprimée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.patch("/entreprises/{entreprise_id}")
def partial_update_entreprise(entreprise_id: int, entreprise_data: dict, user: User = Depends(decode_token)):
    """
    Mettre à jour partiellement une entreprise par son ID
    """    
    existing_entreprise = get_entreprise_by_id(entreprise_id)
    if not existing_entreprise:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    # Vérification du rôle
    if user.role != "admin" or user.role != "maintainer":
        raise HTTPException(status_code=403, detail="Vous n'avez pas les droits nécessaires pour effectuer cette action")

    # Vérification de l'ID de l'entreprise
    if user.entreprise != existing_entreprise.entreprise:
        raise HTTPException(status_code=403, detail="Vous n'êtes pas autorisé à modifier cette entreprise")
    
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