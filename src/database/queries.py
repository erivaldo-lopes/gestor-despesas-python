"""
    Projeto: Sistema de Gestão de Despesas Pessoais

    Ficheiro: queries.py
    Descrição:
    Este módulo contém as funções responsáveis pelas operações
    de base de dados relacionadas com despesas e rendimentos.

    Autor: Erivaldo Jorge Centeio Lopes
    Data: 13/03/2026
    Curso: NST PROG28 - Programador de Infromática

    Dependências:
    - mysql.connector
    - connection.py
"""

from database.connection import conectar
from datetime import datetime, date

def executar_modificacao(sql, valores):
    """
    Executa uma query que modifica dados na base de dados.

    Parâmetros:
    sql (str): instrução SQL a executar
    valores (tuple): valores a inserir na query (opcional)

    Retorna:
    None

    Exemplos:
    INSERT, UPDATE, DELETE
    """

    conexao = None
    cursor = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(sql, valores)
        conexao.commit()
    
    except Exception as e:
        print("Erro ao executar a query: ", e)
    
    finally:
        if cursor: cursor.close()
        if conexao: conexao.close()


    
def executar_consulta(sql, valores = None):
    """
    Executa uma query de leitura na base de dados.

    Retorna:
    lista de resultados da consulta.
    """

    conexao = None
    cursor = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        if valores: cursor.execute(sql, valores)
        else: cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print("Erro ao consultar a base de dados: ", e)
        return []
    finally:
        if cursor: cursor.close()
        if conexao: conexao.close()



def inserir_despesa(descricao, valor, data, id_categoria):
    """
    Insere uma nova despesa na base de dados.

    Parâmetros:
    descricao (str) : descrição da despesa
    valor (float) : valor monetário da despesa
    data (str) : data da despesa no formato YYYY-MM-DD
    id_categoria (int) : identificador da categoria associada

    Retorna:
    None

    Exemplo de utilização:
    inserir_despesa("Supermercado", 45.50, "2026-03-11", 1)
    """

    sql = """
    INSERT INTO despesas(descricao, valor, data, id_categoria)
    VALUES (%s, %s, %s, %s)
    """
    valores = (descricao, valor, data, id_categoria)
    executar_modificacao(sql, valores)
    print("Despesa inserido com sucesso!")

    

def inserir_rendimento(descricao, valor, data):
    """
    Insere um novo rendimento na base de dados.

    Parâmetros:
    descricao (str): descrição do rendimento
    valor (float): valor monetário recebido
    data (str): data do rendimento no formato YYYY-MM-DD

    Retorna:
    None

    Exemplo de utilização:
    inserir_rendimento("salario mes maio", 1000, "2026-05-28")    
    """

    sql = """
    INSERT INTO rendimentos(descricao, valor, data)
    VALUES(%s, %s, %s)
    """
    
    valores = (descricao, valor, data)
    executar_modificacao(sql, valores)
    print("Rendimento inserido com sucesso!")



def listar_despesas(valor_min = 0, data_inicio = "2020-12-31", categoria = None):

    """
    Lista despesas filtradas por valor mínimo, data mínima e categoria.

    Parâmetros:
    valor_minimo (float, opcional): valor mínimo das despesas (padrão = 0)
    data_inicio (str, opcional): data mínima das despesas no formato YYYY-MM-DD (padrão = "2020-12-31")
    categoria (str, opcional): nome da categoria para filtrar; se None, retorna todas as categorias

    Retorna:
    list: lista de tuplos com os dados das despesas.

    Estrutura do resultado:
    (id_despesa, descricao, valor, data, nome_categoria)

    Exemplos de uso:
    - listar todas as despesas: listar_despesas()
    - listar despesas superiores a 50: listar_despesas(valor_minimo=50)
    - listar despesas após 2026-03-01: listar_despesas(data_inicio="2026-03-01")
    - listar despesas >= 50 após 2026-03-01: listar_despesas(valor_minimo=50, data_inicio="2026-03-01")
    - listar despesas da categoria "Lazer": listar_despesas(categoria="Lazer")
    - listar despesas >= 50 da categoria "Lazer" após 2026-03-01: 
            listar_despesas(valor_minimo=50, data_inicio="2026-03-01", categoria="Lazer")
    """

    sql = """
    SELECT d.id_despesa, d.descricao, d.valor, d.data, c.nome
    FROM despesas d
    LEFT JOIN categorias c ON d.id_categoria = c.id_categoria
    WHERE d.valor >= %s AND d.data >= %s
    """

    if isinstance(data_inicio, str): data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    valores = [valor_min, data_inicio]
    if categoria is not None:
        sql += " AND c.nome = %s"
        valores.append(categoria)

    sql += " ORDER BY d.data DESC"

    print("SQL:", sql)
    print("Valores:", valores)
    despesas = executar_consulta(sql, tuple(valores))
    return despesas


def listar_rendimentos(valor_min = 0, data_inicio = "2020-12-31"):
    """
    Lista rendimentos filtrados por valor mínimo e data mínima.

    Parâmetros:
    valor_minimo (float, opcional): valor mínimo dos rendimentos (padrão = 0)
    data_inicio (str, opcional): data mínima dos rendimentos no formato YYYY-MM-DD (padrão = "2020-12-31")

    Retorna:
    list: lista de tuplos com os dados dos rendimentos.

    Estrutura do resultado:
    (id_rendimento, descricao, valor, data)

    Exemplos de uso:
    - listar todos os rendimentos: listar_rendimentos()
    - listar rendimentos superiores a 100: listar_rendimentos(valor_minimo=100)
    - listar rendimentos após 2026-03-01: listar_rendimentos(data_inicio="2026-03-01")
    - listar rendimentos >= 100 após 2026-03-01: listar_rendimentos(valor_minimo=100, data_inicio="2026-03-01")
    """

    sql = """
    SELECT * FROM rendimentos r
    WHERE r.valor >= %s AND r.data >= %s
    ORDER BY r.data DESC
    """

    if isinstance(data_inicio, str): data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    valores = (valor_min, data_inicio)
    rendimentos = executar_consulta(sql, valores)
    return rendimentos