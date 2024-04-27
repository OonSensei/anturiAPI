from fastapi import APIRouter, status, Depends, HTTPException
from database.models import AnturitBase
from database.models import AnturiDB
from database.models import Antureidentiedot
from database.database import get_session
from database import anturit_crud
from sqlmodel import Session

router = APIRouter()

@router.post("/anturit", status_code=201)
def create_anturi(*, session: Session = Depends(get_session), anturi_in: AnturitBase):
    anturi = anturit_crud.create_anturi(session, anturi_in)
    return anturi


@router.get("/anturit", response_model=list[Antureidentiedot])
def get_anturit(*, session: Session = Depends(get_session), anturi: str = ""):
    anturi = anturit_crud.get_anturit(session, anturi)
    return anturi

@router.get("/anturit/{id}", response_model=AnturiDB)
def get_anturi(*, session: Session = Depends(get_session), id: int):
    return anturit_crud.get_anturi(session, id)

@router.get("/anturit_tilanperusteella",response_model=list[Antureidentiedot])
def get_virhetila(*,session: Session = Depends(get_session), tila: str =""):
    tila = anturit_crud.get_antureidentilat(session, tila)
    return tila

@router.delete("/anturit/{id}")
def delete_anturi(*, session: Session = Depends(get_session), id: int):
    return anturit_crud.delete_anturi(session, id)

@router.patch("/virhetila")
def virhetila_anturi(*, session: Session=Depends(get_session), id: int):
    return anturit_crud.virhetila_anturi(session, id)

@router.patch("/anturinvaihto")
def vaihdalohko_anturi(*, session: Session=Depends(get_session), id: int,Lohko_id: int):
    return anturit_crud.vaihdalohko_anturi(session, id, Lohko_id)


