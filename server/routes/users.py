from fastapi import APIRouter
from models.users import UsuarioInput, UsuarioOutput
from services import users


router = APIRouter(prefix="/usuario", tags=["usuario"])


@router.post("/cadastrar", response_model=UsuarioOutput)
def cadastrar_usuario(usuario: UsuarioInput) -> UsuarioOutput:
    return users.cadastrar_usuario(
        nome=usuario.nome, login=usuario.login, senha=usuario.senha
    )

