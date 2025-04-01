from model.database import Database

class Tarefa:
    def __init__(self, titulo, id=None, data_conclusao=None): # Todos os parâmetros são opcionais
        """Construtor da classe Tarefa."""
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salva uma tarefa no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    @staticmethod # decorador -> não precisa instanciar a classe para usar o método
    def listarTarefas():
        """Retornar uma lista com todas as tarefas já cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else [] # Se tarefas for None, retorna uma lista vazia -> moderna, só funciona em Python
    
    @staticmethod
    def apagarTarefa(idTarefa):
        """Apaga uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,) # Precisa passar como tupla? SIM! -> espera 1 ou mais valores
        db.executar(sql, params)
        db.desconectar()

    @staticmethod
    def buscarTarefa(idTarefa):
        """Busca uma tarefa pelo ID no banco de dados."""
        db = Database()
        db.conectar()
        sql = 'SELECT id, titulo, data_conclusao FROM tarefa WHERE id = %s'
        params = (idTarefa,)
        resultado = db.consultar(sql, params)
        db.desconectar()
        return resultado if resultado else None

    def editarTarefa(idTarefa, titulo, data_conclusao):
        """Editar uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'UPDATE tarefa SET titulo = %s, data_conclusao = %s WHERE id = %s'
        params = (titulo, data_conclusao, idTarefa) # Precisa passar como tupla? SIM! -> espera 1 ou mais valores
        db.executar(sql, params)
        db.desconectar()