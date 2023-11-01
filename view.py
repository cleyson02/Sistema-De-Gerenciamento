import sqlite3

# Função para conectar ao banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para inserir uma nova sala no banco de dados
def insert_room(nome):
    conn = connect()  # Conectar ao banco de dados
    cursor = conn.cursor()  # Criar um cursor para executar consultas SQL
    cursor.execute("INSERT INTO salas(nome) VALUES(?)", (nome,))  # Inserir uma nova sala
    conn.commit()  # Confirmar a inserção
    conn.close()  # Fechar a conexão com o banco de dados

# Função para remover uma sala com base no ID
def remove_room(id):
    conn = connect()  # Conectar ao banco de dados
    cursor = conn.cursor()  # Criar um cursor para executar consultas SQL
    cursor.execute("SELECT * FROM salas WHERE id = ?", (id,))  # Buscar a sala com o ID fornecido
    existing_room = cursor.fetchone()  # Tentar buscar a sala com o ID fornecido

    if existing_room is not None:
        cursor.execute("DELETE FROM salas WHERE id = ?", (id,))  # Remover a sala com o ID fornecido
        conn.commit()  # Confirmar a remoção
        print(f"Sala com ID {id} foi removida com sucesso.")
    else:
        print(f"Sala com ID {id} não foi encontrada e não pode ser removida.")
    
    conn.close()  # Fechar a conexão com o banco de dados

# Função para inserir informações de usuário no banco de dados
def insert_user(nome, sobrenome, telefone, email):
    conn = connect()  # Conectar ao banco de dados
    cursor = conn.cursor()  # Criar um cursor para executar consultas SQL
    cursor.execute("INSERT INTO usuarios(nome, sobrenome, telefone, email) VALUES (?, ?, ?, ?)", (nome, sobrenome, telefone, email))  # Inserir informações de usuário
    conn.commit()  # Confirmar a inserção
    conn.close()  # Fechar a conexão com o banco de dados

# Função para remover um usuário com base no ID
def remove_user(id):
    conn = connect()  # Conectar ao banco de dados
    cursor = conn.cursor()  # Criar um cursor para executar consultas SQL
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))  # Buscar o usuário com o ID fornecido
    existing_user = cursor.fetchone()  # Tentar buscar o usuário com o ID fornecido

    if existing_user is not None:
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))  # Remover o usuário com o ID fornecido
        conn.commit()  # Confirmar a remoção
        print(f"Usuário com ID {id} foi removido com sucesso.")
    else:
        print(f"Usuário com ID {id} não foi encontrado e não pode ser removido.")
    
    conn.close()  # Fechar a conexão com o banco de dados

# Função para exibir informações das salas existentes no banco de dados
def exibir_salas():
    conn = connect()  # Conectar ao banco de dados
    cursor = conn.cursor()  # Criar um cursor para executar consultas SQL
    salas = cursor.execute("SELECT * FROM salas").fetchall()  # Buscar informações das salas
    conn.close()  # Fechar a conexão com o banco de dados

    if not salas:
        print("Nenhuma sala encontrada.")
        return
    
    print("Salas existentes: ")
    for sala in salas:
        print(f"ID: {sala[0]}")
        print(f"Nome: {sala[1]}")
        print("\n")

# Função para exibir informações dos usuários existentes no banco de dados
def exibir_usuarios():
    conn = connect()  # Conectar ao banco de dados
    cursor = conn.cursor()  # Criar um cursor para executar consultas SQL
    usuarios = cursor.execute("SELECT * FROM usuarios").fetchall()  # Buscar informações dos usuários
    conn.close()  # Fechar a conexão com o banco de dados

    if not usuarios:
        print("Nenhum usuário encontrado.")
        return
    
    print("Usuários existentes: ")
    for usuario in usuarios:
        print(f"ID: {usuario[0]}")
        print(f"Nome: {usuario[1]}")
        print(f"Sobrenome: {usuario[2]}")
        print(f"Telefone: {usuario[3]}")
        print(f"Email: {usuario[4]}")
        print("\n")

remove_room(1)