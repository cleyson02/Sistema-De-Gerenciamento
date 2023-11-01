import sqlite3

# conectar ao banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# função para inserir uma nova sala
def insert_room(nome):
    conn = connect()
    conn.execute("INSERT INTO salas(nome) VALUES(?)", (nome))

# função para inserir usuários
def insert_user(nome, sobrenome, telefone, email):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, telefone, email) VALUES (?, ?, ?, ?)", (nome, sobrenome, telefone, email))

# funcao para exibir as salas
def exibir_salas():
    conn = connect()
    salas = conn.execute("SELECT * FROM salas").fetchall()
    conn.close()

    if not salas:
        print("Nenhuma sala encontrada.")
        return
    
    print("Salas existentes: ")
    for sala in salas:
        print(f"ID: {sala[0]}")
        print(f"Nome: {sala[1]}")
        print("\n")

exibir_salas()