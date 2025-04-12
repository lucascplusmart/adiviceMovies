from config.database import  db_config
from schemas.movies import Filme, Diretor, Ator

def popular_filmes():
    # Dropar e recriar as tabelas
    db_config.Base.metadata.drop_all(bind=db_config.engine)
    db_config.Base.metadata.create_all(bind=db_config.engine)

    session = db_config.SessionLocal()
    try:
        # Criar diretores
        nomes_diretores = [
            "Francis Ford Coppola", "Christopher Nolan", "Fernando Meirelles",
            "David Fincher", "Lana Wachowski", "Peter Jackson",
            "Ridley Scott", "Quentin Tarantino", "Robert Zemeckis"
        ]
        diretores = [Diretor(nome=nome) for nome in nomes_diretores]
        session.add_all(diretores)
        session.flush()  # Garante que IDs estejam disponíveis
        diretores_map = {d.nome: d for d in diretores}

        # Criar atores
        nomes_atores = [
            "Marlon Brando", "Matthew McConaughey", "Alexandre Rodrigues",
            "Brad Pitt", "Keanu Reeves", "Elijah Wood",
            "Russell Crowe", "John Travolta", "Leonardo DiCaprio", "Tom Hanks"
        ]
        atores = [Ator(nome=nome) for nome in nomes_atores]
        session.add_all(atores)
        session.flush()
        atores_map = {a.nome: a for a in atores}

        # Criar os filmes com os diretores e atores associados
        filmes = [
            Filme(
                titulo="O Poderoso Chefão",
                descricao="Máfia italiana",
                ano=1972,
                genero="Crime",
                diretores=[diretores_map["Francis Ford Coppola"]],
                atores=[atores_map["Marlon Brando"]]
            ),
            Filme(
                titulo="Interestelar",
                descricao="Viagem no tempo e espaço",
                ano=2014,
                genero="Ficção científica",
                diretores=[diretores_map["Christopher Nolan"]],
                atores=[atores_map["Matthew McConaughey"]]
            ),
            Filme(
                titulo="Cidade de Deus",
                descricao="Favela carioca",
                ano=2002,
                genero="Drama",
                diretores=[diretores_map["Fernando Meirelles"]],
                atores=[atores_map["Alexandre Rodrigues"]]
            ),
            Filme(
                titulo="Clube da Luta",
                descricao="Crítica à sociedade de consumo",
                ano=1999,
                genero="Drama",
                diretores=[diretores_map["David Fincher"]],
                atores=[atores_map["Brad Pitt"]]
            ),
            Filme(
                titulo="Matrix",
                descricao="Realidade simulada",
                ano=1999,
                genero="Ação",
                diretores=[diretores_map["Lana Wachowski"]],
                atores=[atores_map["Keanu Reeves"]]
            )
        ]

        session.add_all(filmes)
        session.commit()
        print("Filmes, diretores e atores inseridos com sucesso!")
    except Exception as e:
        session.rollback()
        print("Erro ao popular banco de dados:", e)
    finally:
        session.close()

if __name__ == "__main__":
    popular_filmes()
