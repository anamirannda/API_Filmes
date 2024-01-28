from flask import Flask, jsonify, request
def method_name():
    pass
def method_name():
    pass

filme = Flask(__name__)

nomefilmes = [
    {
        'id': 1,
        'titulo': 'O massacre da Serra Elétrica',
        'diretor': 'Tobe Hooper',
        'ano':1987
    },
    {   'id': 2,
        'titulo': 'Invocação do Mal',
        'diretor': 'James Wan',
        'ano':2013
    },
    {
        'id': 3,
        'titulo': 'Brinquedo Assassino',
        'diretor': 'Tom Holland',
        'ano': 1988
    }
]


@filme.route('/nomefilmes',methods = ['GET'])
def consultar_filme():
    return jsonify(nomefilmes)


@filme.route('/nomefilmes/<int:id>', methods = ['GET'])
def consultar_id(id):
    for film in nomefilmes:
        if film.get('id') == id:
            return jsonify(film)
        

@filme.route('/nomefilmes/<int:id>', methods = ['PUT'])
def editar(id):
    editar_filme = request.get_json()
    for indice,film in enumerate(nomefilmes):
        if film.get('id') ==id:
            nomefilmes[indice].update(editar_filme)
            return jsonify(nomefilmes[indice])        


@filme.route('/nomefilmes',methods = ['POST'])
def adicionar():
    novo_filme = request.get_json()
    nomefilmes.append(novo_filme)
    return jsonify(nomefilmes)


@filme.route('/nomefilmes/<int:id>', methods = ['DELETE'])
def excluir():
    for indice, film in enumerate(nomefilmes):
        if film.get('id') == id:
            del nomefilmes[indice]
            return jsonify(nomefilmes)

filme.run(port = 5000, host = 'localhost', debug = True)





    