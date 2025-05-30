import mysql.connector
from PyQt5 import uic,QtWidgets

conexao = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="270315",
    database="pyprojeto"
)

valor_id = 0



def funcao_principal():
    
    modelo = formulario.lineEdit.text()
    marca = formulario.lineEdit_2.text()
    ano = formulario.lineEdit_3.text()
    ano = int(ano)
    
    cursor = conexao.cursor()
    command = f'INSERT INTO tabela (modelo, marca, ano) VALUES ("{modelo}","{marca}",{ano})'
    cursor.execute(command)
    conexao.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    ok.show()
    ok.pushButton.clicked.connect(ok.close)

def tela_lista():
    menu.close()
    telaLista.show()#chama tela

    cursor = conexao.cursor()
    command = f'SELECT * FROM tabela'
    cursor.execute(command)
    resultado = cursor.fetchall()

    telaLista.tableWidget.setRowCount(len(resultado))
    telaLista.tableWidget.setColumnCount(4)

    for i in range(0, len(resultado)):
        for j in range(0, 4):
            telaLista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

def funcao_deleta():
    
    linha = telaLista.tableWidget.currentRow()#saber qual linha ta cendo clicada
    telaLista.tableWidget.removeRow(linha) #remover a linha da tela
    print(linha)

    cursor = conexao.cursor()
    command = f'SELECT * FROM tabela' #selecionar a linha do banco de dados
    cursor.execute(command)
    dados = cursor.fetchall()
    
    id = dados[linha][0]
    command = f'DELETE FROM tabela WHERE id = "{str(id)}" ' #deletar a linha do banco de dados
    cursor.execute(command)
    conexao.commit()

    ok.show()
    ok.pushButton.clicked.connect(ok.close)

def funcao_editar():
    
    global valor_id
    linha = telaLista.tableWidget.currentRow()
    

    cursor = conexao.cursor()
    command = f'SELECT * FROM tabela'
    cursor.execute(command)
    dados = cursor.fetchall()
    
    id = dados[linha][0]
    command = f'SELECT * FROM tabela WHERE id = "{str(id)}" ' #pegar os dados que eu quero alterar
    cursor.execute(command)
    dados_carro = cursor.fetchall() 
    valor_id = id
    
    telaEditar.show() #tela editar
    telaEditar.lineEdit.setText(str(dados_carro[0][0]))
    telaEditar.lineEdit_2.setText(str(dados_carro[0][1]))
    telaEditar.lineEdit_3.setText(str(dados_carro[0][2]))
    telaEditar.lineEdit_4.setText(str(dados_carro[0][3]))


def funcao_salvar_dados():
    global valor_id
    
    modelo = telaEditar.lineEdit_2.text()
    marca = telaEditar.lineEdit_3.text()
    ano = telaEditar.lineEdit_4.text()
    ano = int(ano)
    
    #salvar dados

    cursor = conexao.cursor()
    command = f'UPDATE tabela SET modelo = "{modelo}", marca = "{marca}", ano = "{ano}" WHERE id = "{valor_id}"'
    cursor.execute(command)
    conexao.commit()

    telaEditar.close()
    telaLista.close()
    tela_lista()

    ok.show()
    ok.pushButton.clicked.connect(ok.close)

app = QtWidgets.QApplication([])
menu = uic.loadUi("menu.ui")
formulario=uic.loadUi("formulario.ui")
telaLista = uic.loadUi("lista.ui")
telaEditar = uic.loadUi("editor_lista.ui")
ok = uic.loadUi("notificacao.ui")

menu.pushButton_2.clicked.connect(menu.close)
menu.pushButton_2.clicked.connect(formulario.show)
menu.pushButton.clicked.connect(tela_lista)
menu.pushButton_3.clicked.connect(menu.close)

formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(formulario.close)
formulario.pushButton_2.clicked.connect(menu.show)

telaLista.pushButton.clicked.connect(funcao_deleta)
telaLista.pushButton_2.clicked.connect(funcao_editar)
telaLista.pushButton_3.clicked.connect(telaLista.close)
telaLista.pushButton_3.clicked.connect(menu.show)
telaEditar.pushButton.clicked.connect(funcao_salvar_dados)

menu.show() #chama tela
app.exec()