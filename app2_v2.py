import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/teste')
def index():
    return render_template('testejson.html')


@app.route('/teste2')
def index2():
    return render_template('testejson2.html')


@app.route('/teste3')
def index3():
    return render_template('testejson3.html')

@app.route('/teste4')
def index4():
    return render_template('testejson4.html')

@app.route('/teste5')
def index5():
    return render_template('testejson5.html')

@app.route('/api/say_name', methods=['POST'])
def say_name():
    json = request.get_json()
    first_name = json['first_name']
    last_name = json['last_name']
    return jsonify(first_name=first_name, last_name=last_name)


@app.route('/api/say_name2', methods=['POST'])
def say_name2():
    first = request.form['first_name']
    last = request.form['last_name']
    print(first)
    print(last)
    return jsonify(first_name=first)


@app.route('/api/say_name3', methods=['POST'])
def say_name3():
    first = request.form['first']
    print(first)
    return jsonify(first_name=first)


@app.route('/api/say_name4', methods=['POST'])
def say_name4():
    json = request.get_json()
    first_name = json['first']
    last_name = json['last']
    return jsonify(first_name=first_name, last_name=last_name)


@app.route('/api/say_name5', methods=['POST'])
def say_name5():

    json = request.get_json()
    first_name = json['first']
    last_name = json['last']
    valor = json['combo']
    return jsonify(first_name=valor)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

