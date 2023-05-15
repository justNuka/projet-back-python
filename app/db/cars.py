# Local imports
from models.cars import Car, ECarColors, ECarStates, ECarMotor, CarType

# CARS TYPES


carTypes: list[CarType] = [
    {
        "id": 1,
        "brand": "Renault",
        "model": "Clio",
        "nbDoors": 5,
        "motor": ECarMotor.ESSENCE
    },
    {
        "id": 2,
        "brand": "Peugeot",
        "model": "308",
        "nbDoors": 5,
        "motor": ECarMotor.ESSENCE
    },
    {
        "id": 3,
        "brand": "Citroën",
        "model": "C3",
        "nbDoors": 5,
        "motor": ECarMotor.ESSENCE
    },
    {
        "id": 4,
        "brand": "Citroën",
        "model": "C4",
        "nbDoors": 5,
        "motor": ECarMotor.ESSENCE
    },
    {
        "id": 5,
        "brand": "Citroën",
        "model": "C5",
        "nbDoors": 5,
        "motor": ECarMotor.ESSENCE
    },
    {
        "id": 6,
        "brand": "Toyota",
        "model": "Yaris",
        "nbDoors": 5,
        "motor": ECarMotor.HYBRIDE
    },
    {
        "id": 7,
        "brand": "Toyota",
        "model": "Auris",
        "nbDoors": 5,
        "motor": ECarMotor.HYBRIDE
    },
    {
        "id": 8,
        "brand": "Toyota",
        "model": "Corolla",
        "nbDoors": 5,
        "motor": ECarMotor.HYBRIDE
    }
]

# CARS

cars: list[Car] = [
    {
        "id": 1,
        "km": 10000,
        "type": 1,
        "color": ECarColors.RED,
        "sell_price": 10000,
        "buy_price": 8000,
        "options": ["GPS", "Bluetooth"],
        "state": ECarStates.OK,
        "construction_year": 2015,
        "parking_spot": 1,
        "arrival_date": "2021-01-01",
        "sale_employee": 1,
        "previous_owner": 1,
        "new_owner": 2
    },
    {
        "id": 2,
        "km": 10000,
        "type": 2,
        "color": ECarColors.BLUE,
        "sell_price": 10000,
        "buy_price": 8000,
        "options": ["GPS", "Bluetooth"],
        "state": ECarStates.OK,
        "construction_year": 2015,
        "parking_spot": 1,
        "arrival_date": "2021-01-01",
        "sale_employee": 1,
        "previous_owner": 1,
        "new_owner": 2
    },
    {
        "id": 3,
        "km": 200,
        "type": 3,
        "color": ECarColors.GREEN,
        "sell_price": 10000,
        "buy_price": 8000,
        "options": ["GPS", "Bluetooth"],
        "state": ECarStates.OK,
        "construction_year": 2015,
        "parking_spot": 1,
        "arrival_date": "2021-01-01",
        "sale_employee": 1,
        "previous_owner": 1,
        "new_owner": 2
    },
    {
        "id": 4,
        "km": 0,
        "type": 4,
        "color": ECarColors.BLACK,
        "sell_price": 10000,
        "buy_price": 8000,
        "options": ["GPS", "Bluetooth"],
        "state": ECarStates.OK,
        "construction_year": 2015,
        "parking_spot": 1,
        "arrival_date": "2021-01-01",
        "sale_employee": 1,
        "previous_owner": 1,
        "new_owner": 2
    },
    {
        "id": 5,
        "km": 6723871,
        "type": 5,
        "color": ECarColors.WHITE,
        "sell_price": 10000,
        "buy_price": 8000,
        "options": ["GPS", "Bluetooth"],
        "state": ECarStates.OK,
        "construction_year": 2015,
        "parking_spot": 1,
        "arrival_date": "2021-01-01",
        "sale_employee": 1,
        "previous_owner": 1,
        "new_owner": 2
    },
]
