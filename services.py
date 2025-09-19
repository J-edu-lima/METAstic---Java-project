from models import Usuario, Meta
from datetime import timedelta, date
import threading
import time

def adicionar_meta(usuario: Usuario, nome: str, minutos: int):
    meta = Meta(nome=nome, tempo_diario=timedelta(minutes=minutos))
    usuario.metas.append(meta)

def progresso_meta(meta: Meta) -> float:
    if meta.tempo_diario.total_seconds() == 0:
        return 0
    return meta.progresso_diario.total_seconds() / meta.tempo_diario.total_seconds()

def concluir_meta(meta: Meta):
    meta.progresso_diario = meta.tempo_diario

def todas_concluidas(usuario: Usuario) -> bool:
    return all(m.progresso_diario >= m.tempo_diario for m in usuario.metas if m.ativa)

def verificar_dia(usuario: Usuario):
    hoje = date.today().isoformat()
    if usuario.ultima_data != hoje:
        # Novo dia começou
        if todas_concluidas(usuario):
            usuario.dias_consecutivos += 1
            
        # Resetar progresso das metas
        for m in usuario.metas:
            m.progresso_diario = timedelta()
        usuario.ultima_data = hoje

def iniciar_timer(meta: Meta, usuario: Usuario, callback, salvar_callback, intervalo: int = 1):
    def run():
        while meta.progresso_diario < meta.tempo_diario:
            time.sleep(intervalo)
            meta.progresso_diario += timedelta(seconds=intervalo)
            callback(meta)
            salvar_callback()

        # Timer concluído
        callback(meta)
        if todas_concluidas(usuario):
            usuario.dias_consecutivos += 1
            salvar_callback()

    thread = threading.Thread(target=run, daemon=True)
    thread.start()