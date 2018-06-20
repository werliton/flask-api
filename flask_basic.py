from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/alunos")
def getAlunos():
    return jsonify({
        "id":"10",
        "nome":"UseKio"
    })

if __name__ == '__main__':
    app.run(debug=True)