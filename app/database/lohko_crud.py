from fastapi import HTTPException
from database.models import LohkoBase, LohkoDB,LohkoCreate,AnturiDB
from sqlmodel import Session, select


def create_lohko(session: Session, lohkot_in: LohkoCreate):
    lohko_db = LohkoDB.model_validate(lohkot_in)
    session.add(lohko_db)
    session.commit()
    session.refresh(lohko_db)
    return lohko_db

# def get_lohkot(session: Session, lohko: str = ""):
#     if lohko != "":
#         return session.exec(select(LohkoDB).where(LohkoDB.lohko ==
#         lohko)).all()
#     return session.exec(select(LohkoDB)).all()

def get_lohko(session: Session, id: int):
    return session.exec(select(AnturiDB).where(AnturiDB.lohko_ID == id)).all()


def delete_lohko(session: Session, id: int):
    lohko = session.get(LohkoDB, id)
    if not lohko:
        raise HTTPException(status_code=404, detail="ID not found")
    session.delete(lohko)
    session.commit()
    return {'message': f"lohko with id {id} deleted"}
