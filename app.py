from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #decorator/anotação para a ROTA
def agenda():
    return render_template("base.html", title='Agenda')