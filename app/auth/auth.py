# System Imports
from typing import Annotated
# Libs Imports
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from models.user import User
from sqlalchemy import text
import hashlib
# Local Imports
from routers.user import users
from models.user import User
from config import conn

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

JWT_KEY = "cW1nT8kIC7L8ZnijSHckA2c8f4TgN0DQcI6utcVgZJUdyFv0v0Bek8hxSKESeQV0zjMaK56x2CrzrMuyQBVB7lZ3NiSdvuxJTu18YD55nIBQLRIklzaiYT24iDGJihxvqnsZsmuwJaRFpygLBoRTaa5kVp9eQdmSBWwQ3SooRWTwsWaZDm9CVm3yb3P3X4IAlaAJwT4k"

# Variable global role, pour stocker le rôle de l'utilisateur et l'utiliser ailleurs
is_maintainer = False
entreprise = None

def hash_password(password: str):
    return hashlib.sha256(f'{password}'.encode('utf-8')).hexdigest()


async def decode_token(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        decoded = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
        user_id = decoded.get("id")
        
        # Récupérer le rôle "maintainer" de l'utilisateur à partir de la base de données
        query = text("SELECT entreprise, maintainer FROM users WHERE id = :user_id")
        result = await conn.execute(query, user_id=user_id)
        data = await result.fetchone()
        
        if not data:
            raise credentials_exception

        entrepriseConnectee = data[0]
        is_maintainer = data[1]

        # Vérifier si l'utilisateur est un "maintainer"
        if is_maintainer:
            decoded["maintainer"] = True

        # Créer l'objet User avec les données décodées et les informations sur le maintainer
        user = User(**decoded, entreprise=entrepriseConnectee, maintainer=is_maintainer)

    except (JWTError, TypeError):
        raise credentials_exception

    return user

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    hashed_password = hash_password(form_data.password)
    for user in users:
        if user["email"].lower() == form_data.email.lower():
            if hashed_password == user["password"]:
                data = dict()
                data["id"] = user["id"]
                data["email"] = user["email"]
                data["maintainer"] = user["maintainer"]
                return {
                    "access_token": jwt.encode(data, JWT_KEY, algorithm="HS256"),
                    "token_type": "bearer"
                }
            break
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Incorrect username or password")


@router.get("/items/")
async def read_items(user: Annotated[User, Depends(decode_token)]):
    return {"user": user}