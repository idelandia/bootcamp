import sqlite3

conexao = sqlite3.connect('banco') 
cursor = conexao.cursor()


#dados = cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR, idade INT, curso VARCHAR)')
#dados = cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "João", 25, "Engenharia")')
#dados = cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Mariana", 22, "Engenharia")')
#dados = cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Pedro", 20, "Direito")')
#dados = cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Eliza", 23, "Arquitetura")')
#dados = cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Luiz", 21, "Economia")')

#dados = cursor.execute('SELECT * FROM alunos')
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
#dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#dados = cursor.execute('UPDATE alunos SET idade = 26 WHERE id = 3')
#dados = cursor.execute('DELETE FROM usuario where id = 1')

#alunos.commit()
#alunos.close()

#dados = cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY , nome VARCHAR, idade INT, saldo FLOAT)')
#dados = cursor.execute('INSERT INTO clientes VALUES (1, "Carlos", 35, 1500.00)')
#dados = cursor.execute('INSERT INTO clientes VALUES (2, "Mariana", 28, 2000.00)')
#dados = cursor.execute('INSERT INTO clientes VALUES (3, "Lucas", 40, 1800.00)')
#dados = cursor.execute('INSERT INTO clientes VALUES (4, "Julia", 22, 1200.00)')


#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade >= 30')
#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#dados = cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT max(saldo) FROM clientes)')
#dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo >= 1000')
#dados = cursor.execute('UPDATE clientes SET saldo = 1600.00 WHERE id = 2')
#dados = cursor.execute('DELETE FROM clientes WHERE id = 4')

#dados = cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR, valor FLOAT, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id)) ')
#dados = cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "Produto A", 100.00)')
#dados = cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 2, "Produto B", 150.50)')
#dados = cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 1, "Produto C", 200.75)')
#dados = cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 3, "Produto A", 120.30)')

#dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON clientes.id = compras.cliente_id')
dados = cursor.execute('SELECT * FROM compras')

for clientes in dados:
    print(clientes)


clientes.commit()
clientes.close()