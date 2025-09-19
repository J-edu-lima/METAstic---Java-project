import json
from models import Usuario, Meta
from datetime import timedelta, date

def salvar_usuario(usuario: Usuario, path="data.json"):
    def converter(obj):
        if isinstance(obj, timedelta):
            return obj.total_seconds()
        if isinstance(obj, Meta):
            return {
                "nome": obj.nome,
                "tempo_diario": obj.tempo_diario.total_seconds(),
                "progresso_diario": obj.progresso_diario.total_seconds(),
                "ativa": obj.ativa
            }
        if isinstance(obj, Usuario):
            return {
                "nome": obj.nome,
                "dias_consecutivos": obj.dias_consecutivos,
                "ultima_data": obj.ultima_data,
                "metas": [converter(m) for m in obj.metas]
            }
        return obj

    with open(path, "w", encoding="utf-8") as f:
        json.dump(converter(usuario), f, indent=4, ensure_ascii=False)

def carregar_usuario(path="data.json") -> Usuario:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            usuario = Usuario(
                nome=data["nome"],
                dias_consecutivos=data["dias_consecutivos"],
                ultima_data=data.get("ultima_data", date.today().isoformat()),
                metas=[
                    Meta(
                        nome=m["nome"],
                        tempo_diario=timedelta(seconds=m["tempo_diario"]),
                        progresso_diario=timedelta(seconds=m["progresso_diario"]),
                        ativa=m["ativa"]
                    )
                    for m in data["metas"]
                ]
            )
            return usuario
    except FileNotFoundError:
        return Usuario(nome="Usuário")