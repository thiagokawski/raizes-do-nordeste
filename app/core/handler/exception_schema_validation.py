from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def handler_validation_schema(request: Request, exc: RequestValidationError):
    erros_formatados = []
    
    for err in exc.errors():
        loc = err.get("loc", [])
        loc = [str(l) for l in loc if l != "body"]
        path = ""
        for l in loc:
            if l.isdigit():
                path += f"[{l}]"
            else:
                if path:
                    path += f".{l}"
                else:
                    path = l

        mensagem = "Campo inválido"
        if err["type"] == "string_type":
            mensagem = "Campo deve ser uma string"
        elif err["type"] == "missing":
            mensagem = "Campo obrigatório"
        elif err["type"] == "none_not_allowed":
            mensagem = "Campo não pode ser nulo"

        erros_formatados.append({
            "message": mensagem,
            "local": path
        })

    return JSONResponse(
        status_code=422,
        content={
            "status": 422,
            "erros": erros_formatados
        }
    )