### Instalação

1. Clone o repositório:
> git clone https://github.com/DCOMP-UFS/2022-2-praticas-projetoinca.git

2. Crie um ambiente virtual:
> python -m venv venv

3. Ative o ambiente virtual:
> venv/Scripts/activate

4. Instale as dependências:
> pip install -r requisitos.txt

5. Execute o servidor:
> python manage.py runserver


### API

#### Visão Geral
Esta API permite aos usuários fazerem CRUD (Create, Retrieve, Update e Delete) de pacientes, fisioterapeutas, instituições e administradores.

#### Endpoints
##### GET /paciente
Retorna uma lista de todas as pacientes.

Exemplo de resposta:
~~~JSON
[
    {
        "id": 4,
        "matricula": "98239",
        "nome": "Cintia",
        "sobrenome": "Ferreira",
        "altura": 1.6,
        "peso": 70.0,
        "imc": 23.0
    },
    {
        "id": 5,
        "matricula": "645445",
        "nome": "Fulana",
        "sobrenome": "Detal",
        "altura": 1.7,
        "peso": 80.0,
        "imc": 21.0
    },
    {
        "id": 6,
        "matricula": "94239",
        "nome": "Maria",
        "sobrenome": "José",
        "altura": 1.65,
        "peso": 50.0,
        "imc": 20.0
    }
]
~~~
##### POST paciente/
Cria uma nova paciente.

Parâmetros de requisição:

matricula - matricula da paciente,
nome - Nome da paciente,
sobrenome - Sobrenome da paciente,
altura - Altura da paciente,
peso - Peso da paciente,
imc - IMC da paciente

Exemplo de corpo da requisição:
~~~JSON
{
    "matricula": "98239",
    "nome": "Cintia",
    "sobrenome": "Ferreira",
    "altura": 1.6,
    "peso": 70.0,
    "imc": 23.0
}
~~~
Exemplo de resposta:
~~~JSON
{
    "id": 3,
    "matricula": "98239",
    "nome": "Cintia",
    "sobrenome": "Ferreira",
    "altura": 1.6,
    "peso": 70.0,
    "imc": 23.0
}
~~~

##### PUT paciente/{id}/
Atualiza uma paciente existente.

Parâmetros de requisição
matricula - matricula da paciente
nome - Nome da paciente.
sobrenome - Sobrenome da paciente
altura - Altura da paciente.
peso - Peso da paciente.
imc - IMC da paciente

Exemplo de corpo da requisição:

~~~JSON
{
    "matricula": "98239",
    "nome": "Cintia",
    "sobrenome": "Ferreira",
    "altura": 1.6,
    "peso": 78.0,
    "imc": 23.0
}
~~~

##### DELETE paciente/{id}/
Deleta uma paciente existente.

Exemplo de resposta:

HTTP 202 Accepted

Erros

A API pode retornar os seguintes erros:

400 Bad Request - O corpo da requisição está mal formado ou faltando algum parâmetro obrigatório.
401 Unauthorized - O usuário não está autenticado.
404 Not Found - O recurso solicitado não foi encontrado.
405 Method Not Allowed - O método HTTP não é suportado pelo endpoint solicitado.
500 Internal Server Error - Ocorreu um erro interno no servidor.



