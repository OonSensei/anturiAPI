from fastapi import HTTPException
from database.models import AnturitBase, AnturiDB
from sqlmodel import Session, select

def create_anturi(session: Session, anturit_in: AnturitBase):
    anturi_db = AnturiDB.model_validate(anturit_in)
    session.add(anturi_db)
    session.commit()
    session.refresh(anturi_db)
    return anturi_db

def get_anturit(session: Session, anturi: str = ""):
    if anturi != "":
        return session.exec(select(AnturiDB).where(AnturiDB.anturi ==
        anturi)).all()
    return session.exec(select(AnturiDB)).all()

def get_anturi(session: Session, id: int):
    anturi = session.get(AnturiDB, id)
    if not anturi:
        raise HTTPException(status_code=484, detail=f"{id} not found")
    return anturi

def get_antureidentilat(session: Session, tila: str):
    if tila not in ("virhetila", "normaali"):
        raise HTTPException(status_code=400, detail=f"{tila} ei hyväksytty vaihtoehto")
    if tila == "virhetila":
        return session.exec(select(AnturiDB).where(AnturiDB.virhetila == True)).all()
    
    return session.exec(select(AnturiDB).where(AnturiDB.virhetila == False)).all()

    
    

def delete_anturi(session: Session, id: int):
    anturi = session.get(AnturiDB, id)
    if not anturi:
        raise HTTPException(status_code=404, detail="ID not found")
    session.delete(anturi)
    session.commit()
    return {'message': f"Anturi with id {id} deleted"}

def virhetila_anturi(session: Session, id: int):
    anturi = session.get(AnturiDB, id)
    if not anturi:
        raise HTTPException(status_code=404, detail="anturi not found")
    anturi.virhetila = True
    session.add(anturi)
    session.commit()
    return {'message':f"Anturi Error id: {id}"}

def vaihdalohko_anturi(session: Session, id: int, Lohko_ID: int):
    anturi = session.get(AnturiDB, id)
    if not anturi:
        raise HTTPException(status_code=404, detail="anturi not found")
    anturi.lohko_ID = Lohko_ID
    session.add(anturi)
    session.commit()
    return {'message':f"Anturi vaihdettu toiseen lohkoon. Lohko ID:{id}"}


#Jokainen anturi tietää oman uniikin
#tunnisteensa, mutta se ei tiedä mihin lohkoon se kuuluu.
#1. Lisätä antureita järjestelmään
#Muuttaa anturin tilaa
#Muuttaa lohkoa johon anturi kuuluu

#Poistaa yksittäinen mittatulos

#listaa anturit (näytetään tunniste, lohko ja tila)

#listaa tietyn lohkon anturit(näytetään tunniste, tila sekä viimeisin mitta-arvo ja
#sen aikaleima)

