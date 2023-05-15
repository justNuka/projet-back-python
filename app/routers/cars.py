# Libs Imports
import hashlib
from fastapi import APIRouter, status, HTTPException, Response
from pydantic import BaseModel
# Local Imports
from models.cars import Car, ECarColors, ECarStates, carOptionnalFields
from db.cars import cars as carsDefaultList
from routers.user import users

router = APIRouter()

cars = []


def init_data():
    cars.extend(carsDefaultList)


@router.get("/cars")
def getCar() -> list[Car]:
    """
    Récupérer tout les utilisateurs
    """
    if len(cars) == 0:
        return Response(status_code=204)
    return cars


@router.get("/cars/search")
async def getCarByCarName(ownerId: str):
    """
    Récupérer une voiture par son propriétaire
    """
    if ownerId not in [user["id"] for user in users]:
        raise HTTPException(status_code=400, detail="Invalid user")
    return list(filter(lambda x: x["new_owner"] == ownerId, cars))


@router.post("/cars", status_code=status.HTTP_201_CREATED)
async def createCar(car: Car) -> Car:
    """
    Créer une voiture
    """
    if car.color not in ECarColors:
        raise HTTPException(status_code=400, detail="Invalid color")
    if car.state not in ECarStates:
        raise HTTPException(status_code=400, detail="Invalid state")
    if car.sale_employee not in [user["id"] for user in users]:
        raise HTTPException(status_code=400, detail="Invalid sale_employee")
    if car.previous_owner not in [user["id"] for user in users]:
        raise HTTPException(status_code=400, detail="Invalid previous_owner")
    if car.new_owner not in [user["id"] for user in users]:
        raise HTTPException(status_code=400, detail="Invalid new_owner")
    car.id = cars[-1]["id"] + 1
    cars.append(car)
    return car


@router.delete("/cars/{carId}")
async def deleteCarById(carId: int) -> Car:
    """
    Supprimer une voiture par son id
    """
    oldCar = list(filter(lambda x: x["id"] == carId, cars))
    cars.remove(oldCar[0])
    return oldCar[0]


@router.put("/cars/{carId}")
async def updateCarById(carId: int, car: Car) -> Car:
    """
    Mettre à jour une voiture par son id
    """
    if car.color not in ECarColors:
        raise HTTPException(status_code=400, detail="Invalid color")
    if car.state not in ECarStates:
        raise HTTPException(status_code=400, detail="Invalid state")
    if car.sale_employee not in [user["id"] for user in users]:
        raise HTTPException(status_code=400, detail="Invalid sale_employee")
    if car.previous_owner not in [user["id"] for user in users]:
        raise HTTPException(status_code=400, detail="Invalid previous_owner")
    if car.new_owner not in [user["id"] for user in users]:
        raise HTTPException(status_code=400, detail="Invalid new_owner")
    oldCar = list(filter(lambda x: x["id"] == carId, cars))
    cars.remove(oldCar[0])
    cars.append(car.__dict__)
    return car


@router.patch("/cars/{carId}")
async def updateCarById(carId: int, car: carOptionnalFields) -> Car:
    """
    Mettre à jour une voiture par son id
    """
    oldCar = list(filter(lambda x: x["id"] == carId, cars))

    cars.remove(oldCar[0])

    if car.km:
        oldCar[0].km = car.km
    if car.color and car.color in ECarColors:
        if car.color not in ECarColors:
            raise HTTPException(status_code=400, detail="Invalid color")
        oldCar[0].color = car.color
    if car.sell_price:
        oldCar[0].sell_price = car.sell_price
    if car.buy_price:
        oldCar[0].buy_price = car.buy_price
    if car.options:
        oldCar[0].options = car.options
    if car.state and car.state in ECarStates:
        if car.state not in ECarStates:
            raise HTTPException(status_code=400, detail="Invalid state")
        oldCar[0].state = car.state
    if car.construction_year:
        oldCar[0].construction_year = car.construction_year
    if car.parking_spot:
        oldCar[0].parking_spot = car.parking_spot
    if car.arrival_date:
        oldCar[0].arrival_date = car.arrival_date
    if car.sale_employee:
        if car.sale_employee not in [user["id"] for user in users]:
            raise HTTPException(
                status_code=400, detail="Invalid sale_employee")
        oldCar[0].sale_employee = car.sale_employee
    if car.previous_owner:
        if car.previous_owner not in [user["id"] for user in users]:
            raise HTTPException(
                status_code=400, detail="Invalid previous_owner")
        oldCar[0].previous_owner = car.previous_owner
    if car.new_owner:
        if car.new_owner not in [user["id"] for user in users]:
            raise HTTPException(status_code=400, detail="Invalid new_owner")
        oldCar[0].new_owner = car.new_owner

    cars.append(oldCar[0].__dict__)
    return oldCar[0]
