import sqlite3

conexao = sqlite3.connect('banco') 
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('DROP TABLE produtos')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Isabel", "Itália", "isa@gmail.com", 12345678)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (2, "Maria", "Londres", "maria@gmail.com", 12345679)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (3, "Lucas", "Russia", "lucas@gmail.com", 12345677)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (4, "Luis", "Australia", "luis@gmail.com", 12345676)')
#cursor.execute('DELETE FROM usuario where id=1')
#cursor.execute('UPDATE usuario SET endereco = "Brasil" WHERE nome = "Lucas"')
#ORDER BY E DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
#LIMIT E DISTINCT
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')

#GROUP BY E HAVING
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')

#JOIN's
#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (4, "Luis", "Australia", "luis@gmail.com")')

#JOIN - LEFT JOIN
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')
#JOIN - RIGHT JOIN
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')
#JOIN - FULL JOIN
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')

#SUB-CONSULTAS
dados = cursor.execute('SELECT * FROM usuario WHERE nome in (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close 