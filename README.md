# 🎬 AdviceMovies - API de Recomendação de Filmes

Este projeto é uma API desenvolvida com **FastAPI** e banco de dados **SQLite**, que permite:

- Cadastrar usuários
- Listar filmes
- Marcar filmes como assistidos
- Gerar recomendações personalizadas de filmes com base em preferências do usuário

---

## 📁 Estrutura de Pastas

~~~bash
adviceMovies/
├── server/
│   ├── main.py                    # Ponto de entrada FastAPI
│   ├── routers/                   # Endpoints da API
│   │   ├── users.py
│   │   └── movies.py
│   ├── services/                  # Lógica de negócio
│   │   ├── users.py
│   │   └── movies.py
│   ├── schemas/                   # Modelos ORM (SQLAlchemy)
│   │   ├── users.py
│   │   └── movies.py
│   ├── models/                    # Modelos Pydantic (request/response)
│   │   ├── users.py
│   │   └── movies.py
│   ├── config/
│   │   └── database.py            # Configuração do banco SQLite
│   ├── populate_database.py       # Script de carga inicial de dados
│   ├── Dockerfile                 # Dockerfile da aplicação
│   └── requirements.txt           # Dependências da aplicação
├── docker-compose.yml             # Docker Compose (na raiz)
└── README.md                      # Documentação do projeto
~~~
---

## 🧩 Banco de Dados - SQLite

O banco de dados é um arquivo local SQLite (`database.db`), gerenciado com SQLAlchemy.

### Principais tabelas:

- `t_usuarios`: Usuários cadastrados  
- `t_filmes`: Filmes disponíveis  
- `t_atores`: Atores  
- `t_diretores`: Diretores  
- `t_usuario_filmes_assistidos`: Relacionamento de filmes assistidos pelos usuários
#### DER (Diagrama Entidade-Relacionamento):
![DRE](https://github.com/user-attachments/assets/bf2dfb3a-5b54-4cb8-822a-14573e120a62)

## 🚀 Endpoints da API

### 👤 Usuário

#### `POST /usuario/cadastrar`  
Cadastra um novo usuário.

**Request:**
~~~json
{
  "nome": "Lucas",
  "login": "lucas123",
  "senha": "123456"
}
~~~

### 🎬 Filmes
#### GET /filmes/
Lista todos os filmes cadastrados.

~~~json
[
	{
		"id": 1,
		"titulo": "...",
		"descricao": "...",
		"ano": 1972,
		"genero": "...",
		"diretores": [
			"..."
		],
		"atores": [
			"..."
		]
	},
    {
		"id": 2,
		"titulo": "...",
		"descricao":"...",
		"ano": 1999,
		"genero": "...",
		"diretores": [
			"..."
		],
		"atores": [
			"..."
		]
	},
]
~~~

#### POST /filmes/assistir
Registra um filme como assistido por um usuário.

Request:

~~~json
{
  "usuario_id": 1,
  "filme_id": 3,
  "nota": 5
}
~~~

#### GET /filmes/{usuario_id}/recomendacoes
Gera recomendações com base nos filmes assistidos pelo usuário. A recomendação considera:

- Gêneros favoritos
- Diretores favoritos
- Atores favoritos

Response:


~~~json
[
  {
    "id": 6,
    "titulo": "Matrix Reloaded",
    "descricao": "Continuação de Matrix",
    "ano": 2003,
    "genero": "Ação"
  }
]
~~~

----

## 🐳 Como subir o projeto com Docker

1. Certifique-se de que o Docker e o Docker Compose estão instalados e em execução.

2. No terminal, navegue até a raiz do projeto (onde está o `docker-compose.yml`).

3. Execute o comando abaixo para construir a imagem e subir o container:

~~~bash
docker compose up --build
~~~
