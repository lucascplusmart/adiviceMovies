from fastapi import APIRouter
from typing import List
from services import movies
from models.movies import FilmeOutput, AssistirFilmeInput

router = APIRouter(prefix="/filmes", tags=["Filmes"])

@router.get("/", response_model=List[FilmeOutput])
def listar_filmes() -> FilmeOutput:
    return movies.listar_filmes()

@router.post("/assistir")
def assistir_filmes(assistir: AssistirFilmeInput):
    return movies.assistir_filmes(assistir)


@router.get("/{usuario_id}/recomendacoes", response_model=list[FilmeOutput])
def recomendar_filmes(usuario_id: int):
    return movies.recomendar_filmes(usuario_id)
