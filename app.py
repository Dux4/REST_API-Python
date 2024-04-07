from flask import Flask, jsonify

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Eduardo',
     'habilidades': ['Python', 'Flask']
     },
    {'nome': 'Samuel',
     'habilidades': ['Python', 'Django']
     }
]

@app.route('/dev<int:id>')
def desenvolvedor(id):
    desenvolvedor=desenvolvedores[id] #retorna a posicao do vetor
    return jsonify(desenvolvedor)

if __name__ == '__main__':
    app.run()