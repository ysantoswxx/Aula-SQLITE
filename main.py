#Criar um banco de dados SQLITE e uma tabela
import sqlite3

# criar a conexão com banco de dados cahamdo de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamado de "cursor"  que será usado para execultar os comandos sql
cursor = conexao.cursor()