# Libs Imports
from fastapi import APIRouter, status, HTTPException, Response
from pydantic import BaseModel
# Local Imports
from models.planning import Planning, PlanningOptionnalFields
from db.planning import plannings as planningsDefaultList


router = APIRouter()

plannings = []


def init_data():
    plannings.extend(planningsDefaultList)

@router.get("/plannings")
def getPlanning() -> list[Planning]:
    """
    Récupérer tous les planings
    Vérifie si la liste est vide, si oui, retourne un code 204
    """
    if len(plannings) == 0:
        return Response(status_code=204)
    return plannings


@router.get("/plannings/search")
async def getPlanningByPlanningTitle(planningTitle: str):
    """
    Récupérer un planning par son titre
    """
    return list(filter(lambda x: x["title"] == planningTitle, plannings))


@router.post("/plannings", status_code=status.HTTP_201_CREATED)
async def createPlanning(planning: Planning) -> Planning:
    """
    Crée un planning
    """
    if planning.title.lower() in [(planning["title"]).lower() for planning in plannings]:
        raise HTTPException(status_code=400, detail="A planning with the same title is already created")
    planning.id = plannings[-1]["id"] + 1
    plannings.append(planning.__dict__)
    return planning


@router.delete("/plannings/{planningId}")
async def deletePlanningById(planningId: int) -> Planning:
    """
    Supprimer un planning par son id
    """
    oldPlanning = list(filter(lambda x: x["id"] == planningId, plannings))
    plannings.remove(oldPlanning[0])
    return oldPlanning[0]


@router.put("plannings/{planningId}")
async def updatePlanningById(planningId: int, planning: Planning) -> Planning:
    """
    Mettre à jour un planning par son id
    """
    oldPlanning = list(filter(lambda x: x["id"] == planningId, plannings))
    plannings.remove(oldPlanning[0])
    plannings.append(planning.__dict__)
    return planning


@router.patch("/plannings/{planningId}")
async def updatePlanningById(planningId: int, planning: PlanningOptionnalFields) -> Planning:
    """
    Mettre à jour un planning par son id
    """
    oldPlanning = list(filter(lambda x: x["id"] == planningId, plannings))

    plannings.remove(oldPlanning[0])

    if planning.title is not None:
        oldPlanning[0]["name"] = planning.title
    if planning.description is not None:
        oldPlanning[0]["description"] = planning.description

    plannings.append(oldPlanning[0].__dict__)
    return oldPlanning[0]