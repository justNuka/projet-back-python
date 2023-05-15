# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel

# CARS TYPES


class CarMotor(Enum):
    DIESEL = "Diesel",
    ESSENCE = "Essence",
    HYBRIDE = "Hybride",
    ELECTRIQUE = "Electrique"


ECarMotor = Enum(
    'CarMotor', ['DIESEL', 'ESSENCE', 'HYBRIDE', 'ELECTRIQUE'])


class CarType(BaseModel):
    id: int
    brand: str
    model: str
    nbDoors: int
    motor: ECarMotor

# CARS


class CarColors(Enum):
    RED = "RED",
    GREEN = "GREEN",
    BLUE = "BLUE",
    PURPLE = "PURPLE",
    BLACK = "BLACK",
    GRAY = "GRAY",
    WHITE = "WHITE",
    YELLOW = "YELLOW",
    ORANGE = "ORANGE",
    BROWN = "BROWN"


ECarColors = Enum('CarColors', ['RED', 'GREEN', 'BLUE', 'PURPLE',
                  'BLACK', 'GRAY', 'WHITE', 'YELLOW', 'ORANGE', 'BROWN'])


class CarStates(Enum):
    DEPLORABLE = "DEPLORABLE",
    BOF = "BOF",
    OK = "OK",
    NICKEL = "NICKEL",
    NEW = "NEW"


ECarStates = Enum('CarStates', ['DEPLORABLE', 'BOF', 'OK', 'NICKEL', 'NEW'])


class Car(BaseModel):
    id: int = None
    type: int
    km: int
    color: ECarColors
    sell_price: float
    buy_price: float
    options: list[str]
    state: ECarStates
    construction_year: int
    parking_spot: int
    arrival_date: str
    sale_employee: int
    previous_owner: int
    new_owner: int


class carOptionnalFields(BaseModel):
    id: int = None
    type: int = None
    km: int = None
    color: ECarColors = None
    sell_price: float = None
    buy_price: float = None
    options: list[str] = None
    state: ECarStates = None
    construction_year: int = None
    parking_spot: int = None
    arrival_date: str = None
    sale_employee: int = None
    previous_owner: int = None
    new_owner: int = None
