from fastapi import APIRouter, status, Depends, HTTPException
from database.models import MittatulosBase, Mittatulos_luo
from database.database import get_session
from database import mittatulos_crud
from sqlmodel import Session

router = APIRouter()

@router.post("/mittatulos", status_code=201)
def create_mittatulos(*, session: Session = Depends(get_session), mittatulos_in: Mittatulos_luo):
    mittatulos = mittatulos_crud.create_mittatulos(session, mittatulos_in)
    return mittatulos


# @router.get("/mittatulos", response_model=list[MittatulosBase])
# def get_mittatulos(*, session: Session = Depends(get_session), mittatulos: str = ""):
#     mittatulos = mittatulos_crud.get_mittatulos(session, mittatulos)
#     return mittatulos

@router.get("/mittatulos/{id}", response_model=MittatulosBase)
def get_mittatulos(*, session: Session = Depends(get_session), id: int):
    return mittatulos_crud.get_mittatulos(session, id)

@router.delete("/mittatulos/{id}")
def delete_mittatulos(*, session: Session = Depends(get_session), id: int):
    return mittatulos_crud.delete_mittatulos(session, id)