from sqlalchemy.orm import Session
from schemas.users import Usuario

def buscar_por_login(db: Session, login: str):
    return db.query(Usuario).filter(Usuario.login == login).first()

def salvar(db: Session, usuario: Usuario):
    db.add(usuario)
    return usuario

