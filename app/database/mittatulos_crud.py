from fastapi import HTTPException
from database.models import MittatulosBase, Mittatulos_luo
from sqlmodel import Session, select

def create_mittatulos(session: Session, mittatulos_in: Mittatulos_luo):
    mittatulos_db = MittatulosBase.model_validate(mittatulos_in)
    session.add(mittatulos_db)
    session.commit()
    session.refresh(mittatulos_db)
    return mittatulos_db

def get_mittatulos(session: Session, id: int = None):
    if id != None:
        return session.exec(select(MittatulosBase).where(MittatulosBase.id ==
        id)).first()
    else:
        return session.exec(select(MittatulosBase)).all()

def delete_mittatulos(session: Session, id: int):
    mittatulos = session.get(MittatulosBase, id)
    if not mittatulos:
        raise HTTPException(status_code=404, detail="ID not found")
    session.delete(mittatulos)
    session.commit()
    return {'message': f"mittatulos with id {id} deleted"}
