#  Gestor de Despesas e Rendimentos (Python + MySQL)

## Descrição do Projeto 
Esta aplicação foi desenvolvida para facilitar o controlo financeiro pessoal. O sistema permite o registo detalhado de ganhos e gastos, utilizando uma base de dados **MySQL** para garantir que nenhuma informação se perca. 

O projeto foi estruturado seguindo os princípios do **SDLC (Software Development Life Cycle)**, focando-se numa arquitetura limpa e na separação de responsabilidades.

---

## Funcionalidades
- **Gestão de Fluxo:** Registo de despesas e rendimentos.
- **Filtros Avançados:** - Pesquisa por valor mínimo.
  - Filtragem por data inicial.
  - Segmentação por categoria (exclusivo para despesas).
- **Organização:** Categorização inteligente de gastos.
- **Persistência:** Integração total com base de dados relacional.

---

## Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Base de Dados:** MySQL
- **Conector:** `mysql-connector-python`
- **Ferramentas:** VS Code, Git e GitHub

---

## Estrutura do Projeto
Para uma melhor organização, todo o código fonte reside na diretoria `src/`.

# Gestor de Despesas Python

```text
gestor-despesas-python/
├── src/                        # Código fonte
│   ├── database/               # Camada de dados
│   │   ├── connection.py       # Configuração da conexão
│   │   └── queries.py          # Consultas SQL (CRUD)
│   ├── models/                 # Lógica de negócio
│   │   ├── despesa.py
│   │   └── rendimento.py
│   ├── sql/                    # Scripts de base de dados
│   │   └── schema.sql          # Criação de tabelas e sementes
│   └── main.py                 # Ponto de entrada da aplicação
├── .gitignore                  # Ficheiros ignorados pelo Git
└── README.md                   # Documentação do projeto 
```

## Base de Dados

O sistema utiliza uma base de dados **MySQL** com as seguintes tabelas principais:

*   `categorias`
*   `despesas`
*   `rendimentos`

### Exemplo de Relação

A estrutura segue uma lógica de chave estrangeira para organização:

> **categorias (1)** ──── **(N) despesas**


## 🚀 Instalação

1. **Clonar o repositório**

   git clone https://github.com/SEU_USERNAME/gestor-despesas-python.git
   cd gestor-despesas-python

2. **Criar ambiente virtual**
  ```bash
   python -m venv .venv
   ```
**Ativar:**

*   **Windows:**
    ```powershell
    .venv\Scripts\activate
    ```

*   **Linux / Mac:**
    ```bash
    source .venv/bin/activate
    ```


3. **Instalar dependências**
```powershel
pip install mysql-connector-python
```

Configuração da Base de Dados
Criar a base de dados no MySQL.
Executar o script:
```bash
sql/schema.sql
```
Este script cria:
base de dados
tabelas
categorias iniciais

Configurar a ligação no ficheiro:
```bash
database/connection.py
```
Exemplo:

*   host = "localhost"
*   user = "root"
*   password = "sua_password"
*   database = "gestor_despesas"
*   Executar o Programa

No terminal:
```bash
python main.py
```

A aplicação irá ligar-se à base de dados e executar as funcionalidades implementadas.
Exemplo de Consulta

*   Listar despesas com filtros:
*   listar_despesas(valor_min=50, data_inicio="2024-01-01", categoria="Lazer")

## Melhorias Futuras
Possíveis evoluções do projeto:
*   Interface gráfica (Tkinter ou Web)
*   Sistema de múltiplos utilizadores
*   Gestão de grupos familiares
*   Cálculo automático de saldo mensal
*   Exportação de relatórios
*   Dashboard com gráficos

# Autor
## Erivaldo Lopes
## NST PROG28 Programador de Informática
## 10790 - Projeto de programação

