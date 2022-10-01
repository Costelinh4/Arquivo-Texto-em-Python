import mysql.connector
from prettytable import PrettyTable


def abrebanco():
    try:
        global conexao
        conexao = mysql.connector.Connect(host='localhost',database='univap',user='root', password='')

        if conexao.is_connected():

            global comandosql
            comandosql = conexao.cursor()
            comandosql.execute('select database();')
            nomebanco = comandosql.fetchone()
            return 1
        else:
            print('Conexão não realizada com banco')
            return 0
    except Exception as erro:
        print(f'Erro : {erro}')
        return 0


def mostrartodasdisciplinas(codigodisciplina): #select all
    grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from disciplinas where codigodisc = {codigodisciplina};')
        tabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1]])

        else:
            print('Não existem disciplinas cadastradas!!!')
        return tabela
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')


def mostrartodasdisciplinasxprofessores(codprofessor):
    grid = PrettyTable(['Código da disciplina no curso','Código da Disciplina','Código do Professor',
                        'Curso','Carga Horária', 'Ano letivo'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from disciplinasxprofessores where codprofessor = {codprofessor} ORDER BY codprofessor;')
        tabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4],registro[5]])

        else:
            print('Não existem valores cadastrados!!!')
        return tabela
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')


def mostrartodosprofessores():
    grid = PrettyTable(['Registro dos Professores','Nome dos Professores'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from professores;')
        tabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1]])
        else:
            print('Não existem professores cadastrados!!!')
        return tabela
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')



abrebanco()
professor = (mostrartodosprofessores())
for i in range(len(professor)):
    arquivo = open(f'{professor[i][0]}.html', 'w')

    texto = f'\nDisciplinas do Professor: {professor[i][1]}'
    tabela = (mostrartodasdisciplinasxprofessores(codprofessor=professor[i][0]))
    for x in range(len(tabela)):
        if x != 0 and tabela[x][3] != tabela[x-1][3]:
            texto += f'<br>curso: {tabela[x][3]}'
        if x == 0:
            texto += f'<br>curso: {tabela[x][3]}'
            texto += '<br>Código disciplina | Nome disciplina'
        disciplina = mostrartodasdisciplinas(codigodisciplina=tabela[x][1])
        for c in range(len(disciplina)):
            texto += f'<br>{disciplina[c][0]} | {disciplina[c][1]}'
    arquivo.write(texto)






