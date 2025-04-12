from models import *


class FilmeOutput(BaseModel):
      # ler os dados a partir de um objeto ORM (como os modelos do SQLAlchemy)
    model_config = {
        'from_attributes': True
    }

    id: int
    titulo: str
    descricao: str
    ano: int
    genero: str
    diretores: List[str]
    atores: List[str]


class AssistirFilmeInput(BaseModel):
    usuario_id: int
    filme_id: int
    nota: Optional[int] = None
