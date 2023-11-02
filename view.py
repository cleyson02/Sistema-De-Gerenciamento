import sqlite3

# Função para conectar ao banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para inserir uma nova sala no banco de dados
def insert_room(nome):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO salas(nome) VALUES(?)", (nome,))
    conn.commit()
    conn.close()

# Função para remover uma sala com base no ID
def remove_room(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM salas WHERE id = ?", (id,))
    existing_room = cursor.fetchone()

    if existing_room is not None:
        cursor.execute("DELETE FROM salas WHERE id = ?", (id,))
        conn.commit()
        print(f"Sala com ID {id} foi removida com sucesso.")
    else:
        print(f"Sala com ID {id} não foi encontrada e não pode ser removida.")
    
    conn.close()

# Função para inserir informações de usuário no banco de dados
def insert_user(nome, sobrenome, telefone, email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios(nome, sobrenome, telefone, email) VALUES (?, ?, ?, ?)", (nome, sobrenome, telefone, email))  # Inserir informações de usuário
    conn.commit()
    conn.close()

# Função para remover um usuário com base no ID
def remove_user(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    existing_user = cursor.fetchone()

    if existing_user is not None:
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conn.commit()  # Confirmar a remoção
        print(f"Usuário com ID {id} foi removido com sucesso.")
    else:
        print(f"Usuário com ID {id} não foi encontrado e não pode ser removido.")
    
    conn.close()

# Função para exibir informações das salas existentes no banco de dados
def exibir_salas():
    conn = connect()
    cursor = conn.cursor()
    salas = cursor.execute("SELECT * FROM salas").fetchall()
    conn.close()

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
    conn = connect()
    cursor = conn.cursor()
    usuarios = cursor.execute("SELECT * FROM usuarios").fetchall()
    conn.close()

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

# Função para reservar as salas
def insert_loan(id_sala, id_usuario, data_reserva, horario_reserva, data_devolucao, horario_devolucao):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservas(id_sala, id_usuario, data_reserva, horario_reserva, data_devolucao, horario_devolucao) VALUES (?, ?, ?, ?, ?, ?)", (id_sala, id_usuario, data_reserva, horario_reserva, data_devolucao, horario_devolucao)) # Inserir informações da reserva
    conn.commit()
    conn.close()

# Função para exibir todas as salas reservadas no momento
def get_rooms_on_loan():
    conn = connect()
    cursor = conn.cursor()
    result = cursor.execute("SELECT reservas.id, salas.nome, usuarios.nome, usuarios.sobrenome, reservas.data_reserva, reservas.horario_reserva, reservas.data_devolucao, reservas.horario_devolucao\
                            FROM salas\
                            INNER JOIN reservas ON salas.id = reservas.id_sala\
                            INNER JOIN usuarios ON usuarios.id = reservas.id_usuario\
                            WHERE reservas.data_devolucao IS NULL AND reservas.horario_devolucao IS NULL").fetchall()
    conn.close()
    
    if not result:
        print("Nenhuma sala está reservada no momento.")
    else:
        print("Salas reservadas no momento: ")
        for sala in result:
            print(f"ID da reserva: {sala[0]}")
            print(f"Nome da sala: {sala[1]}")
            print(f"Nome do usuário: {sala[2]} {sala[3]}")
            print(f"Data de reserva: {sala[4]}")
            print(f"Horário de reserva: {sala[5]}")
            print(f"Data de devolução: {sala[6]}")
            print(f"Horário de devolução: {sala[7]}")
            print("\n")

# Função para atualizar a data e o horário da devolução
def update_loan_return_date(id_reserva, data_devolucao, horario_devolucao):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE reservas SET data_devolucao = ?, horario_devolucao = ? WHERE id = ?", (data_devolucao, horario_devolucao, id_reserva))
    conn.commit()
    conn.close()

# Função para remover uma reserva com base no ID da reserva
def remove_loan(id_reserva):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservas WHERE id = ?", (id_reserva,))
    existing_reservation = cursor.fetchone()

    if existing_reservation is not None:
        cursor.execute("DELETE FROM reservas WHERE id = ?", (id_reserva,))
        conn.commit()
        print(f"Reserva com ID {id_reserva} foi removida com sucesso.")
    else:
        print(f"Reserva com ID {id_reserva} não foi encontrada e não pode ser removida.")
    
    conn.close()

remove_room(1)