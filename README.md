# 🎯 METAstic – Gerenciador de Metas Pessoais

Aplicativo desktop standalone desenvolvido em **Python + Flet**, focado no controle de metas diárias, produtividade, consistência e gerenciamento de tempo pessoal.

---

## 🧠 Objetivo

O sistema busca ajudar o usuário a:

- Criar metas com tempo diário definido.
- Controlar e registrar o tempo de dedicação via timer integrado.
- Acompanhar o progresso diário de cada meta.
- Manter um contador de dias consecutivos com todas as metas concluídas.

---

## 🧱 Estrutura de Dados (Entidades)

Apesar do projeto estar em **paradigma procedural**, as entidades ainda são representadas como estruturas/dicionários:

### 👤 Usuário

- `nome: str` — nome do usuário.
- `dias_consecutivos: int` — total de dias em que todas as metas foram concluídas.
- `metas: list` — lista de metas associadas.

### ✅ Meta

- `nome: str` — nome da meta.
- `tempo_diario: int` — tempo desejado por dia (em minutos).
- `estado: str` — "ATIVA" ou "DESATIVADA".
- `progresso: int` — tempo acumulado no dia (em minutos).

### ⏱️ Timer (não persistido)

- `meta_ref` — referência à meta em andamento.
- `tempo_restante: int` — minutos restantes para concluir a meta.
- `tempo_gasto: int` — minutos gastos na sessão.

---

## 🔁 Relacionamentos

- Um **Usuário** possui várias **Metas**.
- Uma **Meta** pode estar vinculada temporariamente a um **Timer**.
- O **Timer** atualiza o progresso da **Meta** em tempo real.

---

## 🏗️ Estrutura Modular (Procedural)

project-root/
│── main.py # Ponto de entrada do app (Flet)
│── ui/ # Interface gráfica
│ └── screens.py # Telas e layouts principais
│── core/ # Regras do domínio (procedural)
│ ├── user.py # Manipulação de usuários
│ ├── meta.py # Manipulação de metas
│ └── timer.py # Lógica de contagem de tempo
│── storage/ # Persistência local
│ └── repository.py # Leitura/Escrita em JSON ou SQLite
└── docs/ # Documentação do projeto

yaml
Copiar código

---

## 💾 Persistência

Banco local: **SQLite (sqlite3)** ou **JSON** para simplicidade inicial.

**Dados persistidos:**

- Usuário
- Metas

---

## 🧰 Tecnologias Utilizadas

- Python 3.12+
- Flet (interface desktop)
- SQLite / JSON (persistência local)

---

## ✅ Status do Projeto

- 🚧 Estrutura modular inicial definida.
- ⏱️ Timer funcional em testes.
- 💾 Persistência básica em JSON prevista para próxima etapa.

---

## 📄 Licença

Uso pessoal e educacional. Nenhuma licença formal definida ainda.
