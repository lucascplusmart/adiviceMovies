from pydantic import BaseModel

class UsuarioInput(BaseModel):
    nome: str
    login: str
    senha: str

class UsuarioOutput(BaseModel):
     # ler os dados a partir de um objeto ORM (como os modelos do SQLAlchemy)
    model_config = {
        'from_attributes': True
    }
    
    id: int
    nome: str
    login: str

   