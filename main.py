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
cursor.execute("""
UPDATE alunos 
SET idade = ?, curso = ?
WHERE id = ? 
""", (61, "Medicina", 2)
)
conexao.commit()