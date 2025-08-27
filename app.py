######################
#API COM PYTHON#######
######################

#O QUE É API?
"""
Uma API (Application Programming Interface) é um conjunto de regras e padrões 
que permite a comunicação entre diferentes sistemas, softwares ou componentes de forma estruturada. 
Na prática, uma API define como funções, dados ou serviços podem ser acessados sem que seja necessário 
conhecer os detalhes internos de implementação. Por exemplo, quando um aplicativo de celular consulta o
clima, ele não calcula nada por si mesmo: ele faz uma requisição para uma API de previsão do tempo, que 
retorna os dados já processados. Assim, a API funciona como uma "ponte" que conecta sistemas diferentes, 
garantindo integração, reutilização de recursos e padronização no desenvolvimento de aplicações.
"""

# 1 - Objetivo: Criar um api que disponibiliza a consulta, criação, edição  e exclusão de livros
# 2 - URL base: - localhost
"""
# 3 - EndPoints 
- localhost/livros (GET) 
- localhost/livros (POST) *
- localhost/livro/id (GET)
- localhost/livro/id (PUT))
- localhost/livro (DELETE)
"""
# 4 - Quais recursos seram disponibilizados - Livros


#importação de bibliotecas 
from  flask import Flask, jsonify, request
app  = Flask(__name__)

#fonte de dados
#forma mais simples - usando um dicionario
livros = [

    {"id": 1, "titulo": "Dom Quixote", "autor": "Miguel de Cervantes"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez"},
    {"id": 4, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 5, "titulo": "Crime e Castigo", "autor": "Fiódor Dostoiévski"},
    {"id": 6, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
    {"id": 7, "titulo": "A Revolução dos Bichos", "autor": "George Orwell"},
    {"id": 8, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"},
    {"id": 9, "titulo": "O Nome do Vento", "autor": "Patrick Rothfuss"},
    {"id": 10, "titulo": "Sapiens: Uma Breve História da Humanidade", "autor": "Yuval Noah Harari"}

]

#CONSULTAR TODOS 
#CRIAR UMA FUNCÃO QUE DE ACESSOR A TODOS OS LIVROS
@app.route("/livros", methods=['GET'])
def pegar_livro():
    return jsonify(livros)
#CONSULTAR ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if  livro.get("id") == id:
            return jsonify(livro)
#EDITAR
@app.route('/livros/<int:id>', methods = ['PUT'])
def editar_livros_id(id):
    livro_alterado = request.get_json( )
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#CRIAR
@app.route('/livros', methods = ['POST'])
def incluir_livro( ):
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
#EXCLUIR
@app.route('/livros/<int:id>',methods = ['DELETE'])
def excluir_livro(id):
    for indice,livro  in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

#app run
app.run(port=8000, host='localhost', debug=True)


