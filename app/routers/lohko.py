from fastapi import APIRouter, status, Depends, HTTPException
from database.models import LohkoBase
from database.models import LohkoDB
from database.models import Lohkotiedot
from database.database import get_session
from database import lohko_crud
from sqlmodel import Session

router = APIRouter()

@router.post("/lohkot", status_code=201)
def create_lohko(*, session: Session = Depends(get_session), lohko_in: LohkoBase):
    lohko = lohko_crud.create_lohko(session, lohko_in)
    return lohko


# @router.get("/lohkot", response_model=list[LohkoDB])
# def get_lohkot(*, session: Session = Depends(get_session), lohko: str = ""):
#     lohko = lohko_crud.get_lohkot(session, lohko)
#     return lohko

@router.get("/lohkot/{id}", response_model=list[Lohkotiedot])
def get_lohko(*, session: Session = Depends(get_session), id: int):
    return lohko_crud.get_lohko(session, id)

@router.delete("/lohkot/{id}")
def delete_lohko(*, session: Session = Depends(get_session), id: int):
    return lohko_crud.delete_lohko(session, id)