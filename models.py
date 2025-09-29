from dataclasses import dataclass
from datetime import timedelta
from typing import List
from time import sleep
from enum import Enum
import threading

class Estado(Enum):
    ATIVA = 1
    PAUSADA = 2
    CONCLUIDA = 3
    PARADA = 4

class Meta:
    def __init__(self, nome: str, minutos_diarios: int):
        self._nome = nome
        self._minutos_diarios = timedelta(minutes=minutos_diarios)

        self._progresso_diario: timedelta = timedelta()
        self._estado: Estado = Estado.PAUSADA
        
        self._pause_event = threading.Event()
        self._pause_event.set()   # começa ativo (não pausado)
        self._stop_event = threading.Event()
        self._thread = None
    
    def get_descricao(self) -> str:
        return self._nome, self._minutos_diarios, self._estado.name, self._progresso_diario
    
    def concluir(self):
        self._estado = Estado.CONCLUIDA
        print(f"✅ Meta '{self._nome}' concluída!")
    
    def iniciar_timer(self):
        if self._thread and self._thread.is_alive():
            print(f"Timer da meta '{self._nome}' já está rodando!")
            return self._thread
        
        def run():
            self._estado = Estado.ATIVA
            while self._progresso_diario < self._minutos_diarios and not self._stop_event.is_set():
                self._pause_event.wait()  # 🔴 bloqueia aqui se estiver pausado
                sleep(1)
                self._progresso_diario += timedelta(seconds=1)
                # print(f"[{self._nome}] progresso: {self._progresso_diario}")

            if not self._stop_event.is_set():
                self.concluir()

        self._thread = threading.Thread(target=run)
        self._thread.start()
        return self._thread

    def pausar(self):
        self._estado = Estado.PAUSADA
        self._pause_event.clear()  # 🔴 congela no próximo loop
        
        sleep(1)
        print(f"\n⏸ Meta '{self._nome}' pausada.")

    def retomar(self):
        self._estado = Estado.ATIVA
        self._pause_event.set()  # 🔵 continua
        
        sleep(1)
        print(f"\n▶ Meta '{self._nome}' retomada.")

    def parar(self):
        self._stop_event.set()
        self._estado = Estado.PARADA
        if self._thread:
            self._thread.join()
       
class Usuario:
    def __init__(self, nome: str):
        self._nome = nome
        self._metas: List[Meta] = []

    def adicionar_meta(self, meta: Meta):
        self._metas.append(meta)
    
    def iniciar_meta(self, nome_meta: str):
        meta = next((m for m in self._metas if m._nome == nome_meta), None)
        if meta:
            meta.iniciar_timer()

    def pausar_meta(self, nome_meta: str):
        meta = next((m for m in self._metas if m._nome == nome_meta), None)
        if meta:
            meta.pausar()

    def excluir_meta(self, meta):
        if meta in self._metas:
            self._metas.remove(meta)
            return True
        return False

    def get_metas(self) -> List[Meta]:
        return self._metas
    