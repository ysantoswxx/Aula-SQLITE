#Criar um banco de dados SQLITE e uma tabela
import sqlite3

# criar a conexão com banco de dados cahamdo de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamado de "cursor"  que será usado para execultar os comandos sql
cursor = conexao.cursor()

# #Criar uma tebela no banco de dados 
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER  PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,           
#     curso TEXT
#     )    
# """)

# nome = input("Digite o nome do aluno: ").lower()
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno: ").lower()

# #Inserir um dado na tabela
# cursor.execute("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)
# """, 
# (nome, idade, curso)
# )

# #Confirmar as alteração no banco
# conexao.commit()


#Inserir varios alunos em uma so vez
# alunos = [
#     ("Yago", 28, "Direitos"),
#     ("Jessica", 24, "Computação"),
#     ("breno", 52, "Computação"),
# ]
# #executemy permte inserir multiplas linhas de uma vez so 
# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)
# """,
# (alunos)
# )
# conexao.commit()


#Atualizar dados no banco 
# cursor.execute("""
# UPDATE alunos 
# SET idade = ?, curso = ?
# WHERE id = ? 
# """, (61, "Medicina", 2)
# )
# conexao.commit()


#Função dados no banco 
#consutar os dados no banco 
# cursor.execute("SELECT * FROM alunos")
# #fetchall traz todas as linhas da consuta
# for linha in cursor.fetchall():
#     print(f"ID:{linha[0]}| NOME: {linha[1]} |IDADE:{linha[2]} | CURSO:{linha[3]}")
# print("-"*50)

# pesquisar = input("Digite o curso que deseja pesquisar os alunos: ")
# cursor.execute("SELECT nome, idade FROM  alunos  WHERE curso = ?",(pesquisar,))
# for linha in cursor.fetchall():
#     print(f"NOME: {linha[0]} | IDADE: {linha[1]}")
# print("-"*50)


#Deletar dados do banco
cursor.execute("DELETE FROM alunos WHERE id = ?", (1,))
conexao.commit()
#Sempre fechar a conexção co o banco de dados 
conexao.close()
