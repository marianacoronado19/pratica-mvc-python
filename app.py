from flask import Flask, render_template, request, redirect, url_for
from model import tarefa
from model.tarefa import Tarefa

app = Flask(__name__)

# Controlador é o cérebro, manda em todos
@app.route("/", methods=['GET', 'POST']) # decorator/anotação para a ROTA
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo = titulo, data_conclusao = data_conclusao) # Cria uma tarefa com os dados do formulário. tarefa é um objeto da classe Tarefa
        tarefa.salvarTarefa()
        return redirect(url_for('index')) # Renderiza de novo a página principal

    tarefas = Tarefa.listarTarefas() # Chama o método estático da classe Tarefa e recebe um dicionário
    return render_template("index.html", tarefas= tarefas, title='Minhas Tarefas', editando=False)

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    Tarefa.apagarTarefa(idTarefa)
    return redirect(url_for('index')) # Redireciona para a rota index após apagar a tarefa

@app.route('/edit/<int:idTarefa>', methods=['GET', 'POST'])
def edit(idTarefa):
    if request.method == 'POST': # Se o método for POST, atualiza os dados da tarefa
        # Atualiza os dados da tarefa no banco de dados
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        Tarefa.editarTarefa(idTarefa, titulo=titulo, data_conclusao=data_conclusao)
        return redirect(url_for('index'))  # Redireciona para a página principal após editar
    elif request.method == 'GET':
        tarefa = Tarefa.buscarTarefa(idTarefa)
        if tarefa:
            return render_template('edit.html', tarefa=tarefa, title='Editar Tarefa', editando=True)
        else:
            return 'Tarefa não encontrada'