from config.database import db_config
from repositories import movies
from models import FilmeOutput, AssistirFilmeInput
from schemas.movies import UsuarioFilmesAssistidos


def listar_filmes() -> list[FilmeOutput]:
    session = db_config.SessionLocal()
    try:
        filmes = movies.listar_filmes(session)

        filmes_output = []
        for filme in filmes:
            filmes_output.append(FilmeOutput(
                id=filme.id,
                titulo=filme.titulo,
                descricao=filme.descricao,
                ano=filme.ano,
                genero=filme.genero,
                diretores=[diretor.nome for diretor in filme.diretores],
                atores=[ator.nome for ator in filme.atores]
            ))

        session.commit()
        return filmes_output
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def assistir_filmes(data: AssistirFilmeInput):
    session = db_config.SessionLocal()
    try:
        # Verifica se já existe uma avaliação do mesmo usuário para o mesmo filme
        filmeAssistido = movies.buscar_filme_assistido(session, data.usuario_id, data.filme_id)

        if filmeAssistido:
            # Se já existir, atualiza a nota
            filmeAssistido.nota = data.nota
        else:
            # Se não existir, cria nova
            filme = UsuarioFilmesAssistidos(
                usuario_id=data.usuario_id,
                filme_id=data.filme_id,
                nota=data.nota
            )
            movies.salvar_filme_assistido(session, filme)

        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def recomendar_filmes(usuario_id: int) -> list[FilmeOutput]:
    session = db_config.SessionLocal()
    try:
        filmes_assistidos = movies.buscar_filmes_assistidos_por_usuario(session, usuario_id)
        ids_assistidos = [filme.id for filme in filmes_assistidos]

        preferencias = movies.buscar_preferencias_usuario(session, usuario_id)

        recomendados = movies.buscar_filmes_por_preferencias(session, preferencias, ids_assistidos)

        recomendacoes_output = []
        for filme in recomendados:
            recomendacoes_output.append(FilmeOutput(
                id=filme.id,
                titulo=filme.titulo,
                descricao=filme.descricao,
                ano=filme.ano,
                genero=filme.genero,
                diretores=[d.nome for d in filme.diretores],
                atores=[a.nome for a in filme.atores]
            ))

        session.commit()
        return recomendacoes_output
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

