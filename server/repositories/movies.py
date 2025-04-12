from sqlalchemy.orm import Session
from schemas.movies import Filme, UsuarioFilmesAssistidos


def listar_filmes(session: Session):
    return session.query(Filme).all()


def salvar_filme_assistido(session: Session, assistir: UsuarioFilmesAssistidos):
    session.add(assistir)


def buscar_filme_assistido(session: Session, usuario_id: int, filme_id: int):
    return session.query(UsuarioFilmesAssistidos).filter_by(usuario_id=usuario_id, filme_id=filme_id).first()


def buscar_filmes_assistidos_por_usuario(session: Session, usuario_id: int):
    assistidos = session.query(UsuarioFilmesAssistidos).filter_by(usuario_id=usuario_id).all()
    return [registro.filme for registro in assistidos]


def buscar_preferencias_usuario(session: Session, usuario_id: int):
    registros = session.query(UsuarioFilmesAssistidos).filter(
        UsuarioFilmesAssistidos.usuario_id == usuario_id,
        UsuarioFilmesAssistidos.nota >= 3
    ).all()

    generos = set()
    diretores = set()
    atores = set()

    for registro in registros:
        filme = registro.filme
        generos.add(filme.genero)
        diretores.update(diretor.id for diretor in filme.diretores)
        atores.update(ator.id for ator in filme.atores)

    return {
        "generos": list(generos),
        "diretores": list(diretores),
        "atores": list(atores),
    }

def buscar_filmes_por_preferencias(session: Session, preferencias: dict, ids_assistidos: list[int]):
    query = session.query(Filme).distinct()

    if preferencias["generos"]:
        # IN
        query = query.filter(Filme.genero.in_(preferencias["generos"]))

    if preferencias["diretores"]:
        # exist
        query = query.join(Filme.diretores).filter(Filme.diretores.any(id__in=preferencias["diretores"]))

    if preferencias["atores"]:
        # exist
        query = query.join(Filme.atores).filter(Filme.atores.any(id__in=preferencias["atores"]))

    if ids_assistidos:
        # Not IN
        query = query.filter(~Filme.id.in_(ids_assistidos))

    return query.all()
 