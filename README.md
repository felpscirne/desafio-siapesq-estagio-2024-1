# Como executar este projeto
Siga as instruções abaixo para executar este projeto em sua máquina local.

## Pré-requisitos
Você precisará ter os seguintes softwares pré-instalados em seu computador:

-Python 3.8 ou superior
-PostgreSQL
-Venv
-Pip

## Passos para a execução
  ### Clone o repositório localmente

  `git clone https://github.com/felpscirne/desafio-siapesq-estagio-2024-1.git`

### Crie um ambiente virtual

  Navegue até o diretório do projeto e crie um ambiente virtual usando o módulo venv do Python.

### Ative o ambiente virtual

Windows:
`.\env\Scripts\activate`

Linux ou MacOS:
`source env/bin/activate`

### Instale as dependências

Instale as dependências do projeto usando o pip. As dependências estão listadas no arquivo `requirements.txt`.
 
  
  `pip install -r requirements.txt`

### Configure o banco de dados

Configure a URL do banco de dados como uma variável de ambiente. Substitua `username`, `password` e `database` pelos detalhes do seu banco de dados PostgreSQL.

Windows:
`$env:DATABASE_URL="postgresql://username:password@localhost/database"`

Linux ou MacOS:
`export DATABASE_URL=postgresql://username:password@localhost/database`

### Execute o projeto

Finalmente, execute o projeto com o comando:
`python app.py`

## Com isso, você já pode acessar localhost:5000 ou testar via Postman








