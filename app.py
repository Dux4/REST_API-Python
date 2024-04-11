from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {
        'id' : '0',
        'nome': 'Eduardo',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id' : '1',
        'nome': 'Samuel',
        'habilidades': ['Python', 'Django']
     }
]

#Devolve um DEV pelo id, altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response=desenvolvedores[id] #retorna a posicao do vetor
        except IndexError:
            mensagemError=  'Desenvolvedor Id {} não existe'.format(id)
            response={'status': 'erro', 'mensagem': mensagemError }
        except Exception:
            mensagem= 'Erro desconhecido. Procure o autor do código '
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem' : 'Registro deletado'})

    #Permite adicionar um novo DEV e lista todos
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
        if request.method == 'POST':
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            print(dados)
            return jsonify(desenvolvedores[posicao])
        elif request.method == 'GET':
            return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True, )