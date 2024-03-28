from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    primos = "Tudo vai dar certo caros alunos!"

    return primos

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

