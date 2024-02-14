from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def hello_world():
      return '<p>Hello from Flask!</p><table><tr><td><b>Aluno:</b></td><td>Murillo de Araujo Ferreira</td></tr><tr><td><b>Prontuário:</b></td><td>PT3019993</td></tr></table>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

