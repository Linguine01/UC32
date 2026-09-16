from flask import Flask, render_template, request

app = Flask(__name__)

tarefas = []

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/tarefas", methods=["GET", "POST"])
def lista_tarefas():
    if request.method == "POST":
        tarefa = request.form["tarefa"]
        tarefas.append(tarefa)

    return render_template("tarefas.html", tarefas=tarefas)

if __name__ == "__main__":
    app.run(debug=True)