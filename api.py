import requests
import json 
import mysql.connector

# Substitua os valores pelos seus próprios
config = {
    'hostname': 'db-teste.mysql.database.azure.com',
    'user': 'leocarv1@db-teste',
    'password': 'Panqueca14!',
    'database': 'mysql',
}

cnx = mysql.connector.connect(user="leocarv1", password="Panqueca14!", host="db-teste.mysql.database.azure.com", port=3306, database="db-dados", ssl_disabled=False)

# Cria a conexão
conn = mysql.connector.connect(**config)

# Cria um cursor
cursor = cnx.cursor()

# Executa uma consulta
cursor.execute("""
    CREATE TABLE Dados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    idade INT,
    endereco VARCHAR(100)
);
""")

# Obtém os resultados da consulta
results = cursor.fetchall()

# Faz algo com os resultados
for row in results:
    # Faça algo com cada linha
    print(row)

# Fecha o cursor
cursor.close()



