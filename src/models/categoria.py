"""
    Modelo de dados para Categoria.

    Este módulo define a entidade Categoria utilizada para classificar
    as despesas no sistema.

    As categorias permitem organizar os gastos por tipo, facilitando
    a análise financeira e a geração de relatórios.

    Exemplos de categorias incluem:
    - Alimentação
    - Transporte
    - Habitação
    - Lazer
    - Saúde
    - Vestuario

    Autor: Erivaldo Jorge Centeio Lopes
    Data: 30/03/2026
    Curso: NST PROG28 - Programador de Infromática
"""

class Categoria:
    """
        Construtor da classe Categoria.

        Parâmetros:
        nome (str): nome da categoria de despesa
    """
    def __init__(self, id_categoria, nome):
        self.id_categoria = id_categoria
        self.nome = nome