import sqlite3

# conectar ao banco de dados ou criar um novo banco de dados
con = sqlite3.connect('dados.db')

# criando tabela de salas
con.execute('CREATE TABLE salas(\
            id INTEGER PRIMARY KEY,\
            sala TEXT)')

# criando tabela de usuários
con.execute('CREATE TABLE usuarios(\
            id INTEGER PRIMARY KEY,\
            nome TEXT,\
            sobrenome TEXT,\
            telefone TEXT,\
            email TEXT)')

#criando tabela de reservas
con.execute('CREATE TABLE reservas(\
            id INTEGER PRIMARY KEY,\
            id_sala INTEGER,\
            id_usuario INTEGER,\
            data_reserva TEXT,\
            horario_reserva TEXT,\
            data_devolucao TEXT,\
            horario_devolucao TEXT,\
            FOREIGN KEY(id_sala) REFERENCES salas(id),\
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')