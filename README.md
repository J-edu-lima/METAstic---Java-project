
# 🎯 Gerenciador de Metas Pessoais

Aplicativo desktop para controle de metas diárias com foco em produtividade, consistência e gerenciamento de tempo pessoal.

---

## 🧠 Objetivo

Permitir ao usuário:

- Criar metas com tempo diário definido.
- Controlar e registrar o tempo de dedicação via timer.
- Acompanhar o progresso diário de cada meta.
- Aumentar um contador de dias consecutivos ao concluir todas as metas do dia.

---

## 🧱 Entidades Principais

### 🧍 Usuario
- `nome`: String — nome do usuário.
- `diasConsecutivosCompletos`: int — total de dias em que todas as metas foram concluídas.
- `metas`: List<Meta> — metas associadas ao usuário.

### ✅ Meta
- `nome`: String — nome da meta.
- `tempoDiario`: Duration — tempo desejado por dia.
- `estado`: Enum (ATIVA / DESATIVADA)
- `progressoDiario`: Duration — tempo acumulado no dia.

### ⏱️ Timer *(não persistido)*
- `meta`: referência à meta ativa.
- `tempoRestante`: Duration — tempo restante para concluir a meta.
- `tempoGasto`: Duration — tempo gasto na sessão.

---

## 🔁 Relacionamentos

- Um `Usuario` possui várias `Meta`.
- Uma `Meta` pode estar sendo controlada temporariamente por um `Timer`.
- O `Timer` atualiza o `progressoDiario` da `Meta` ativa.

---

## 🏗️ Arquitetura de Pacotes

```text
src/
└── main/
    └── java/
        └── com/
            └── projeto/
                ├── domain/          # Núcleo da lógica de negócio
                │   ├── model/       # Entidades: Usuario, Meta, etc.
                │   └── service/     # Lógica e validações do domínio
                ├── application/     # Casos de uso (regras de aplicação)
                ├── ui/              # Interface (JavaFX)
                │   ├── controller/  # Controladores JavaFX
                │   └── view/        # Layouts (FXML)
                └── infra/           # Infraestrutura do projeto
                    ├── repository/  # Implementações dos repositórios
                    ├── config/      # Configurações do Spring e banco
                    └── database/    # Inicialização e dados locais
````

---

## 💾 Persistência

* Banco: **H2** em modo arquivo (salvo localmente).
* Framework: **Spring Data JPA**
* Entidades persistidas:

  * `Usuario`
  * `Meta`

---

## 🧰 Tecnologias Utilizadas

* **Java 17+**
* **JavaFX** (Frontend)
* **Spring Boot** (Backend & Lógica de Aplicação)
* **H2 Database** (Persistência local)
* **Maven** (Gerenciamento de dependências)

---

## ✅ Status do Projeto

🚧 Em desenvolvimento — estruturação inicial concluída, implementações em progresso.

---

## 📄 Licença

Uso pessoal e educacional. Nenhuma licença formal definida ainda.

