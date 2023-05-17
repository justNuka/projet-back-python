# System Import

# Libs Imports
from fastapi import APIRouter, HTTPException, status
from sqlalchemy import text
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
def get_all_activites():
    """
    Récupérer toutes les activités
    """
    entrepriseConnectee = entreprise
    query = text("SELECT title, entreprise, user, created_by, start_date, end_date, description, city, address, zipCode, country FROM activites WHERE entreprise = :entrepriseConnectee")
    result = conn.execute(query)
    data = result.fetchall()

    activites = []
    for row in data:

        activite = Activite(**dict(row))

        activite = {
            "title": data[0],
            "entreprise": data[1],
            "user": data[2],
            "created_by": data[3],
            "start_date": data[4],
            "end_date": data[5],
            "description": data[6],
            "city": data[7],
            "address": data[8],
            "zipCode": data[9],
            "country": data[10],
        }

        activites.append(activite)

    return activites


@router.get("/activites/search")
def get_activites_by_title(title: str):
    """
    Récupérer les activités par leur titre
    """
    query = text("SELECT title, entreprise, user, created_by, start_date, end_date, description, city, address, zipCode, country FROM activites WHERE title = :title")
    result = conn.execute(query, title=title)
    data = result.fetchall()

    activites = []

    for row in data:
        activite = Activite(**dict(row))

        activite = {
            "title": data[0],
            "entreprise": data[1],
            "user": data[2],
            "created_by": data[3],
            "start_date": data[4],
            "end_date": data[5],
            "description": data[6],
            "city": data[7],
            "address": data[8],
            "zipCode": data[9],
            "country": data[10],
        }

        activites.append(activite)
    return activites

@router.post("/activites", status_code=status.HTTP_201_CREATED)
def create_activite(title: str, entreprise: int, user: int, created_by: int, start_date: str, end_date: str, description: str, city: str, address: str, zipCode: str, country: str, current_user: User = Depends(decode_token)):
    """
    Créer un nouvel utilisateur
    """
    if not is_maintainer(current_user):
        raise HTTPException(status_code=401, detail="Vous n'êtes pas autorisé à effectuer cette action")

    if activite_exists(title, entreprise):
        raise HTTPException(status_code=400, detail="Une activité avec le même titre existe déjà dans cette entreprise")

    query = text("INSERT INTO activites (title, entreprise, user, created_by, start_date, end_date, description, city, address, zipCode, country) VALUES (:title, :entreprise, :user, :created_by, :start_date, :end_date, :description, :city, :address, :zipCode, :country)")
    try:
        conn.execute(query, title=title, entreprise=entreprise, user=user, created_by=created_by, start_date=start_date, end_date=end_date, description=description, city=city, address=address, zipCode=zipCode, country=country)
        return {"message": "Activité créée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/activites/{activite_id}")
def delete_activite(activite_id: int, current_user: User = Depends(decode_token)):
    """
    Supprimer une activité par son ID
    """
    if not is_maintainer(current_user):
        raise HTTPException(status_code=401, detail="Vous n'êtes pas autorisé à effectuer cette action")

    query = text("DELETE FROM activites WHERE id = :activite_id")
    try:
        conn.execute(query, activite_id=activite_id)
        return {"message": "Activité supprimée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/activites/{activite_id}")
def update_activite(activite_id: int, activite_data: dict, current_user: User = Depends(decode_token)):
    """
    Mettre à jour une activité par son ID
    """
    if not is_maintainer(current_user):
        raise HTTPException(status_code=401, detail="Vous n'êtes pas autorisé à effectuer cette action")

    existing_activite = get_activite_by_id(activite_id)
    if not existing_activite:
        raise HTTPException(status_code=404, detail="Activité non trouvée")

    query = text("UPDATE activites SET title = :title, entreprise = :entreprise, user = :user, created_by = :created_by, start_date = :start_date, end_date = :end_date, description = :description, city = :city, address = :address, zipCode = :zipCode, country = :country WHERE id = :activite_id")
    try:
        conn.execute(
            query,
            title=activite_data["title"],
            entreprise=activite_data["entreprise"],
            user=activite_data["user"],
            created_by=activite_data["created_by"],
            start_date=activite_data["start_date"],
            end_date=activite_data["end_date"],
            description=activite_data["description"],
            city=activite_data["city"],
            address=activite_data["address"],
            zipCode=activite_data["zipCode"],
            country=activite_data["country"],
            activite_id=activite_id
        )
        return {"message": "Activité mise à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))