

# Biblio_api

Uma API RESTful simples para gerenciar uma coleção de livros, permitindo consulta, criação, edição e exclusão de registros de livros. Desenvolvida em Python utilizando o framework Flask, esta API é ideal para aprendizado e prototipagem de sistemas baseados em APIs.

## Objetivo
O objetivo deste projeto é criar uma API que disponibilize endpoints para gerenciar livros, permitindo operações CRUD (Create, Read, Update, Delete) de forma estruturada e acessível.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Flask**: Framework leve para construção de APIs RESTful.
- **JSON**: Formato utilizado para troca de dados entre cliente e servidor.

## URL Base
- `http://localhost:8000`

## Endpoints
A API oferece os seguintes endpoints para interação com os recursos de livros:

| Método | Endpoint                | Descrição                          |
|--------|-------------------------|------------------------------------|
| GET    | `/livros`              | Retorna a lista de todos os livros |
| GET    | `/livros/<id>`         | Retorna os detalhes de um livro específico pelo ID |
| POST   | `/livros`              | Cria um novo livro                |
| PUT    | `/livros/<id>`         | Edita um livro existente pelo ID   |
| DELETE | `/livros/<id>`         | Exclui um livro pelo ID           |

## Estrutura dos Dados
Os livros são armazenados em uma lista de dicionários em memória, com a seguinte estrutura:
```json
{
  "id": <integer>,
  "titulo": <string>,
  "autor": <string>
}
```

### Exemplo de Livro
```json
{
  "id": 1,
  "titulo": "Dom Quixote",
  "autor": "Miguel de Cervantes"
}
```

## Como Executar
1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Biblioteca Flask instalada. Instale com:
     ```bash
     pip install flask
     ```

2. **Instruções**:
   - Clone ou copie o código do projeto para um arquivo (ex.: `app.py`).
   - Execute o script com o comando:
     ```bash
     python app.py
     ```
   - A API estará disponível em `http://localhost:8000`.

3. **Testando a API**:
   - Use ferramentas como **Postman**, **cURL**, ou um navegador para testar os endpoints.
   - Exemplos de requisições:
     - **GET** todos os livros:
       ```bash
       curl http://localhost:8000/livros
       ```
     - **POST** para criar um novo livro:
       ```bash
       curl -X POST -H "Content-Type: application/json" -d '{"id": 11, "titulo": "Novo Livro", "autor": "Autor Exemplo"}' http://localhost:8000/livros
       ```
     - **PUT** para editar um livro (ex.: ID 1):
       ```bash
       curl -X PUT -H "Content-Type: application/json" -d '{"titulo": "Dom Quixote Editado", "autor": "Miguel de Cervantes"}' http://localhost:8000/livros/1
       ```
     - **DELETE** para excluir um livro (ex.: ID 1):
       ```bash
       curl -X DELETE http://localhost:8000/livros/1
       ```

## Estrutura do Código
- **Fonte de Dados**: Uma lista de dicionários em memória (`livros`), contendo informações como ID, título e autor.
- **Endpoints**:
  - `GET /livros`: Retorna todos os livros.
  - `GET /livros/<id>`: Retorna um livro específico pelo ID.
  - `POST /livros`: Adiciona um novo livro à lista.
  - `PUT /livros/<id>`: Atualiza os dados de um livro existente.
  - `DELETE /livros/<id>`: Remove um livro da lista.

## Possíveis Melhorias
- Adicionar validação de entrada para os dados enviados via POST e PUT.
- Implementar um banco de dados (ex.: SQLite, PostgreSQL) em vez de uma lista em memória.
- Adicionar autenticação para proteger os endpoints.
- Incluir mais campos nos livros, como ano de publicação ou gênero.
- Implementar tratamento de erros mais robusto (ex.: livro não encontrado).

## Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções! Para isso, envie um *pull request* ou abra uma *issue* no repositório.

## Licença
Este projeto é de código aberto e está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
