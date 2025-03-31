from flask import Flask, render_template, request, redirect, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST']) # decorator/anotação para a ROTA
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo = titulo, data_conclusao = data_conclusao)
        tarefa.salvarTarefa()
        return redirect(url_for('index'))

    tarefas = Tarefa.listarTarefas() # Chama o método estático da classe Tarefa e recebe um dicionário
    return render_template("index.html", tarefas= tarefas, title='Minhas Tarefas')

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    Tarefa.apagarTarefa(idTarefa)
    return redirect(url_for('index')) # Redireciona para a rota index após apagar a tarefa

@app.route('/edit/<int:idTarefa>', methods=['GET', 'POST'])
def edit(idTarefa):
    if request.method == 'GET':
        # Busca a tarefa pelo ID e exibe no formulário
        tarefa = Tarefa.buscarTarefaPorId(idTarefa)
        return render_template('index.html', tarefa=tarefa, editando=True)
    elif request.method == 'POST':
        # Atualiza a tarefa com os novos dados enviados pelo formulário
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)
        tarefa.editarTarefaPorId(idTarefa)  # Chama o método para atualizar no banco
        return redirect(url_for('index'))  # Redireciona para a página principal