from schemas import *
from datetime import datetime


class FilmeDiretor(db_config.Base):
    __tablename__ = "t_filmes_diretores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    filme_id = Column(Integer, ForeignKey("t_filmes.id"))
    diretor_id = Column(Integer, ForeignKey("t_diretores.id"))


class FilmeAtor(db_config.Base):
    __tablename__ = "t_filmes_atores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    filme_id = Column(Integer, ForeignKey("t_filmes.id"))
    ator_id = Column(Integer, ForeignKey("t_atores.id"))

class Filme(db_config.Base):
    __tablename__ = "t_filmes"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    ano = Column(Integer)
    genero = Column(String)

    diretores = relationship("Diretor", secondary="t_filmes_diretores", back_populates="filmes")
    atores = relationship("Ator", secondary="t_filmes_atores", back_populates="filmes")
    filmes_assistidos = relationship("UsuarioFilmesAssistidos", back_populates="filme")

class Diretor(db_config.Base):
    __tablename__ = "t_diretores"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    filmes = relationship("Filme", secondary="t_filmes_diretores", back_populates="diretores")


class Ator(db_config.Base):
    __tablename__ = "t_atores"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    filmes = relationship("Filme", secondary="t_filmes_atores", back_populates="atores")

class UsuarioFilmesAssistidos(db_config.Base):
    __tablename__ = "t_usuario_filmes_assistidos"

    id = Column(Integer, primary_key=True, index=True)
    data_assistido = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer, ForeignKey("t_usuarios.id"), nullable=False)
    filme_id = Column(Integer, ForeignKey("t_filmes.id"), nullable=False)
    nota = Column(Integer, nullable=True)  # Avaliação de 1 a 5 (opcional)

    usuario = relationship("Usuario", back_populates="filmes_assistidos")
    filme = relationship("Filme", back_populates="filmes_assistidos")
