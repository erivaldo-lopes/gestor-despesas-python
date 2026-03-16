"""
    Modelo de dados para Despesa.

    Este módulo define a estrutura da entidade Despesa utilizada
    no sistema de gestão de despesas pessoais.

    Uma despesa representa um gasto financeiro efetuado pelo utilizador,
    como alimentação, transporte, habitação ou lazer.

    Cada despesa pode estar associada a uma categoria, permitindo
    organizar e analisar os gastos de forma mais estruturada.

    Autor: Erivaldo Jorge Centeio Lopes
    Data: 13/03/2026
    Curso: NST PROG28 - Programador de Infromática
"""


class Despesa:
    """
        Construtor da classe Despesa.

        Parâmetros:
        descricao (str): descrição da despesa
        valor (float): valor monetário da despesa
        data (str): data da despesa no formato YYYY-MM-DD
        id_categoria (int): identificador da categoria associada
    """
    
    def __init__(self, id_despesa, descricao, valor, data, id_categoria):
        self.id_despesa = id_despesa
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.id_categoria = id_categoria