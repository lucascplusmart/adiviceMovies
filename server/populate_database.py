from config.database import db_config
from schemas.movies import Filme, Diretor, Ator, UsuarioFilmesAssistidos
from schemas.users import Usuario


def popular_filmes():
    # Dropar apenas as tabelas desejadas
    db_config.Base.metadata.drop_all(bind=db_config.engine, tables=[
        Usuario.__table__,
        Filme.atores.property.secondary,
        Filme.diretores.property.secondary,
        Filme.__table__,
        Diretor.__table__,
        Ator.__table__,
        UsuarioFilmesAssistidos.__table__,

    ])

    # Recriar essas tabelas
    db_config.Base.metadata.create_all(bind=db_config.engine, tables=[
        Usuario.__table__,
        Diretor.__table__,
        Ator.__table__,
        Filme.__table__,
        Filme.atores.property.secondary,
        Filme.diretores.property.secondary,
        UsuarioFilmesAssistidos.__table__,
    ])

    session = db_config.SessionLocal()
    try:
        # Diretores genéricos
        nomes_diretores = ["Diretor A", "Diretor B", "Diretor C", "Diretor D", "Diretor E"]
        diretores = [Diretor(nome=nome) for nome in nomes_diretores]
        session.add_all(diretores)
        session.flush()
        diretores_map = {d.nome: d for d in diretores}

        # Atores genéricos
        nomes_atores = ["Ator 1", "Ator 2", "Ator 3", "Ator 4", "Ator 5", "Ator 6"]
        atores = [Ator(nome=nome) for nome in nomes_atores]
        session.add_all(atores)
        session.flush()
        atores_map = {a.nome: a for a in atores}

        # Criar 10 filmes
        filmes = [
            Filme(titulo="Filme A", descricao="Ação e aventura", ano=2020, genero="Ação",
                  diretores=[diretores_map["Diretor A"]], atores=[atores_map["Ator 1"], atores_map["Ator 2"]]),
            Filme(titulo="Filme B", descricao="Drama profundo", ano=2019, genero="Drama",
                  diretores=[diretores_map["Diretor B"]], atores=[atores_map["Ator 2"], atores_map["Ator 3"]]),
            Filme(titulo="Filme C", descricao="Suspense psicológico", ano=2021, genero="Suspense",
                  diretores=[diretores_map["Diretor C"]], atores=[atores_map["Ator 1"], atores_map["Ator 4"]]),
            Filme(titulo="Filme D", descricao="Ficção científica", ano=2022, genero="Ficção",
                  diretores=[diretores_map["Diretor D"]], atores=[atores_map["Ator 5"]]),
            Filme(titulo="Filme E", descricao="Comédia leve", ano=2023, genero="Comédia",
                  diretores=[diretores_map["Diretor E"]], atores=[atores_map["Ator 6"]]),
            Filme(titulo="Filme F", descricao="Drama romântico", ano=2021, genero="Drama",
                  diretores=[diretores_map["Diretor A"]], atores=[atores_map["Ator 3"]]),
            Filme(titulo="Filme G", descricao="Ação explosiva", ano=2018, genero="Ação",
                  diretores=[diretores_map["Diretor B"]], atores=[atores_map["Ator 4"], atores_map["Ator 5"]]),
            Filme(titulo="Filme H", descricao="Suspense de tirar o fôlego", ano=2020, genero="Suspense",
                  diretores=[diretores_map["Diretor C"]], atores=[atores_map["Ator 1"]]),
            Filme(titulo="Filme I", descricao="Comédia pastelão", ano=2017, genero="Comédia",
                  diretores=[diretores_map["Diretor D"]], atores=[atores_map["Ator 6"], atores_map["Ator 2"]]),
            Filme(titulo="Filme J", descricao="Ficção futurista", ano=2022, genero="Ficção",
                  diretores=[diretores_map["Diretor E"]], atores=[atores_map["Ator 3"], atores_map["Ator 5"]]),
        ]
        session.add_all(filmes)
        session.commit()

        print("Filmes, diretores, atores e assistidos resetados com sucesso!")
    except Exception as e:
        session.rollback()
        print("Erro ao popular banco de dados:", e)
    finally:
        session.close()

if __name__ == "__main__":
    popular_filmes()
