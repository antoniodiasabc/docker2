import os
from flask import Flask, render_template, json, request, jsonify
from flaskext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
#app.config['MYSQL_DATABASE_HOST'] = '172.17.0.7'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = _password
            cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', ( _name,_email,_hashed_password))
            conn.commit()

            return render_template('signup.html')
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/list',methods=['POST','GET'])
def listar():
    try:
            
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute ('select user_name from tbl_user') 
            data = cursor.fetchall()
            print(data[0]);
            for x in range(len(data)):
                print(data[x])

            conn.commit()
            return render_template('signup2.html', datas=data)

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()




@app.route('/listjson',methods=['POST','GET'])
def listjson():
    try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute ('select user_name from tbl_user') 
            data = cursor.fetchall()
            print(data[0]);
            for x in range(len(data)):
                print(data[x])

            conn.commit()
            return jsonify(data)

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()


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
    print(first)
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

