from schemas import *

class Usuario(db_config.Base):
    __tablename__ = "t_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

    filmes_assistidos = relationship("UsuarioFilmesAssistidos", back_populates="usuario")



