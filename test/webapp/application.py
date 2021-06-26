from flask import Flask, request, render_template

application = Flask(__name__)

@application.route("/")
def login():
    return render_template('login.html')

@application.route("/inicio")
def inicio():
    return render_template('inicio.html')

# SE EJECUTA CUANDO SE LLAMA ESTE ARCHIVO COMO PRINCIPAL
if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0')