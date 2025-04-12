from fastapi import HTTPException
from repositories import users
from schemas.users import Usuario
from config.database import db_config
from models.users import UsuarioOutput

def cadastrar_usuario(nome: str, login: str, senha: str) -> UsuarioOutput:
    db = db_config.SessionLocal()
    try:
        if users.buscar_por_login(db, login):
            raise HTTPException(status_code=400, detail="Login já existe")

        usuario = Usuario(nome=nome, login=login, senha=senha)
        users.salvar(db, usuario)
        db.commit()
        db.refresh(usuario)

        return UsuarioOutput.model_validate(usuario)
    except:
        db.rollback()
        raise
    finally:
        db.close()