"""
    Módulo de ligação à base de dados.

    Este ficheiro contém a função responsável por estabelecer
    a ligação entre a aplicação Python e a base de dados MySQL.

    Função principal:
    - conectar()

    A ligação é utilizada por todos os módulos que necessitam
    executar queries SQL.

    Autor: Erivaldo Jorge Centeio Lopes
    Data: 30/03/2026
    Curso: NST PROG28 - Programador de Infromática

"""

import mysql.connector

def conectar():
    """
    Cria e retorna uma ligação à base de dados MySQL.

    Retorna:
    connection : objeto de ligação à base de dados

    Lança:
    Exception : caso ocorra erro na ligação
    """

    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Lmxy20#a",
        database = "gestor_despesas"
    )

    return conexao
    