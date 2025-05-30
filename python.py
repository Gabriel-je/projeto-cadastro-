import mysql.connector

conexao = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="270315",
    database="pyprojeto"
)
cursor = conexao.cursor()

""" como adiconar valores na tabale
modelo = "mustang"
marca = "ford"
ano = 2014
command = f'INSERT INTO tabela (modelo, marca, ano) VALUES ("{modelo}", "{marca}",{ano})'
cursor.execute(command)
conexao.commit()
"""

"""" como ler os valores da tabela
command = f'SELECT * FROM tabela'
cursor.execute(command)
resultado = cursor.fetchall()
print(resultado)"""

""" update||| modificar tabela
modelo = "ka"
id = 3
commando = f'UPDATE tabela SET modelo = "{modelo}" WHERE id = "3" '
cursor.execute(commando)
conexao.commit()
"""

"""DELETE|||deletar registro da tabela 
id = 3
commando = f'DELETE FROM tabela WHERE id = "{id}" '
cursor.execute(commando)
conexao.commit()
"""


conexao.close()

cursor.close()

