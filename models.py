from dataclasses import dataclass, field
from datetime import timedelta, date
from typing import List

@dataclass
class Meta:
    nome: str
    tempo_diario: timedelta
    progresso_diario: timedelta = timedelta()
    ativa: bool = True

@dataclass
class Usuario:
    nome: str
    dias_consecutivos: int = 0
    metas: List[Meta] = field(default_factory=list)
    ultima_data: str = field(default_factory=lambda: date.today().isoformat())