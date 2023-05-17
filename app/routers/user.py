# System Import

# Libs Imports
import hashlib
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
import rsa
from fastapi import Depends
# Local Imports
from models.user import User
from config.db import conn
from auth.auth import decode_token, role, entrepriseConnectee
from auth.auth import loadKeys, public_key, private_key

router = APIRouter()

with open('public.pem', mode='wb') as f:
    f.write(public_key.save_pkcs1())

with open('private_key', mode='wb') as f:
    f.write(private_key.save_pkcs1())

# Fonctions qui seront amenées à être utilisées dans le fichier

"""
Fonction qui permet de hasher un mot de passe  
"""
def hash_password(password: str):
    return hashlib.sha256(f'{password}'.encode('utf-8')).hexdigest()


"""
Fonction qui permet de vérifier si un utilisateur avec le meme mail OU le même nom ET prénom existe déjà
"""
def user_exists(email: str, name: str, surname: str) -> bool:
    query = text("SELECT COUNT(*) FROM users WHERE email = :email OR (name = :name AND surname = :surname)")
    result = conn.execute(query, email=email, name=name, surname=surname)

    """
    Récupérer le nombre de lignes retournées par la requête
    result.fetchone() retourne une seule ligne à la fois
    """

    count = result.fetchone()[0]
    return count > 0

def get_user_by_id(user_id: int) -> User:
    """
    Récupérer un utilisateur par son ID
    """
    query = text("SELECT name, surname, email, tel FROM users WHERE id = :user_id")
    result = conn.execute(query, user_id=user_id)
    data = result.fetchone()

    if data is None:
        return None

    name = rsa.decrypt(data[0], private_key).decode('utf-8')
    surname = rsa.decrypt(data[1], private_key).decode('utf-8')
    email = rsa.decrypt(data[2], private_key).decode('utf-8')
    tel = rsa.decrypt(data[3], private_key).decode('utf-8')

    user = User(
        id=user_id,
        name=name,
        surname=surname,
        email=email,
        tel=tel,
    )

    return user


@router.get("/users")
def getUser(user: User= Depends(decode_token)) -> list[User]:
    """
    Récupérer tous les utilisateurs
    """
    # Vérification de l'ID de l'entreprise
    user_id = user.id
    existing_user = get_user_by_id(user_id)
    if existing_user.entrepriseConnectee != user.entrepriseConnectee:
        raise HTTPException(status_code=403, detail="Vous n'avez pas accès à cette ressource")
    
    query = text("SELECT * FROM users")
    result = conn.execute(query)
    data = result.fetchall()

    # Créer une liste d'objets User
    users = []

    # Parcourir les données retournées par la requête
    for row in data:
        user = User(**dict(row))

        # Déchiffrement des données avec la clé privée
        decrypted_name = rsa.decrypt(user.name, private_key).decode('utf-8')
        decrypted_surname = rsa.decrypt(user.surname, private_key).decode('utf-8')
        decrypted_email = rsa.decrypt(user.email, private_key).decode('utf-8')
        decrypted_tel = rsa.decrypt(user.tel, private_key).decode('utf-8')

        # Mettre à jour les données dans l'objet User
        user.name = decrypted_name
        user.surname = decrypted_surname
        user.email = decrypted_email
        user.tel = decrypted_tel

        # Ajouter l'objet User à la liste
        users.append(user)

    # Retourner la liste d'objets User
    return users


@router.get("/users/search")
async def getUserBySurname(surname: str, user: User = Depends(decode_token)):
    """
    Récupérer un utilisateur par son nom
    """

    # Vérification de l'ID de l'entreprise
    user_id = user.id
    existing_user = get_user_by_id(user_id)
    if existing_user.entrepriseConnectee != user.entrepriseConnectee:
        raise HTTPException(status_code=403, detail="Vous n'êtes pas autorisé à modifier cet utilisateur")
    
    query = text("SELECT name, surname, email, tel FROM users WHERE surname = :surname")
    result = conn.execute(query, surname=surname)
    data = result.fetchall()

    # Créer une liste d'objets User
    users = []

    # Parcourir les données retournées par la requête
    for row in data:
        name = rsa.decrypt(row[0], private_key).decode('utf-8')
        surname = rsa.decrypt(row[1], private_key).decode('utf-8')
        email = rsa.decrypt(row[2], private_key).decode('utf-8')
        tel = rsa.decrypt(row[3], private_key).decode('utf-8')

        user = {
            "name": name,
            "surname": surname,
            "email": email,
            "tel": tel,
        }
        # Ajouter l'objet User à la liste
        users.append(user)

    # Retourner la liste d'objets User
    return users



@router.post("/users")
def create_user(name: str, surname: str, email: str, password: str, tel: str, entreprise: str, maintainer: bool = False, user: User = Depends(decode_token)):
    """
    Crée un nouvel utilisateur
    """
    if user_exists(email, name, surname):
        raise HTTPException(status_code=409, detail="Un utilisateur avec le même email OU le même nom ET prénom existe déjà.")
    
    # Vérification du rôle "maintainer"
    if not user.maintainer:
        raise HTTPException(status_code=403, detail="Vous n'avez pas les droits nécessaires pour effectuer cette action")

    # Chiffrement des données avec la clé publique
    encrypted_name = rsa.encrypt(name.encode('utf-8'), public_key)
    encrypted_surname = rsa.encrypt(surname.encode('utf-8'), public_key)
    encrypted_email = rsa.encrypt(email.encode('utf-8'), public_key)
    encrypted_tel = rsa.encrypt(tel.encode('utf-8'), public_key)

    entreprise = entreprise
    maintainer = maintainer
    
    # Préparation de la requête SQL
    hashed_password = hash_password(password)
    query = text("INSERT INTO users (name, surname, email, password, tel, entreprise, maintainer) "
                 "VALUES (:name, :surname, :email, :password, :tel, :entreprise, :maintainer)")
    
    # Exécution de la requête SQL
    try:
        conn.execute(query, name=encrypted_name, surname=encrypted_surname,
                     email=encrypted_email, password=hashed_password, tel=encrypted_tel, entreprise=entreprise, maintainer=maintainer)
        return {"message": "Utilisateur créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, user: User = Depends(decode_token)):
    """
    Supprimer un utilisateur par son ID
    """
    existing_user = get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # Vérification du rôle "maintainer"
    if not user.maintainer:
        raise HTTPException(status_code=403, detail="Vous n'avez pas les droits nécessaires pour effectuer cette action")

    # Vérification de l'ID de l'entreprise
    if existing_user.entrepriseConnectee != user.entrepriseConnectee:
        raise HTTPException(status_code=403, detail="Vous n'êtes pas autorisé à modifier cet utilisateur")

    query = text("DELETE FROM users WHERE id = :user_id")
    try:
        conn.execute(query, user_id=user_id)
        return {"message": "Utilisateur supprimé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/users/{user_id}")
def partial_update_user(user_id: int, user_data: dict, current_user: User = Depends(decode_token)):
    """
    Mettre à jour partiellement un utilisateur par son ID
    """
    existing_user = get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # Vérification du rôle "maintainer"
    if not current_user.maintainer:
        raise HTTPException(status_code=403, detail="Vous n'avez pas les droits nécessaires pour effectuer cette action")

    # Vérification de l'ID de l'entreprise
    if current_user.entreprise != existing_user.entreprise:
        raise HTTPException(status_code=403, detail="Vous n'êtes pas autorisé à modifier cet utilisateur")

    # Récupérer les données existantes de l'utilisateur
    name = existing_user.name
    surname = existing_user.surname
    email = existing_user.email
    tel = existing_user.tel

    # Mettre à jour les champs spécifiés dans user_data
    if "name" in user_data:
        name = rsa.encrypt(user_data["name"].encode('utf-8'), public_key)
    if "surname" in user_data:
        surname = rsa.encrypt(user_data["surname"].encode('utf-8'), public_key)
    if "email" in user_data:
        email = rsa.encrypt(user_data["email"].encode('utf-8'), public_key)
    if "tel" in user_data:
        tel = rsa.encrypt(user_data["tel"].encode('utf-8'), public_key)

    query = text("UPDATE users SET name = :name, surname = :surname, email = :email, tel = :tel WHERE id = :user_id")
    try:
        conn.execute(
            query,
            name=name,
            surname=surname,
            email=email,
            tel=tel,
            user_id=user_id,
        )
        return {"message": "Utilisateur mis à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))