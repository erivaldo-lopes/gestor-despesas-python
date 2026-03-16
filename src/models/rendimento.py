"""
    Modelo de dados para Rendimentos.

    Este módulo define a estrutura da entidade Rendimento utilizada
    no sistema de gestão de despesas pessoais.

    Um rendimento representa qualquer valor financeiro recebido
    pelo utilizador, como salário, prémios ou outras receitas.

    Autor: Erivaldo Jorge Centeio Lopes
    Data: 13/03/2026
    Curso: NST PROG28 - Programador de Infromática
"""

class Rendimento:
    """
        Construtor da classe Rendimento.

        Parâmetros:
        descricao (str): descrição do rendimento
        valor (float): valor monetário recebido
        data (str): data do rendimento no formato YYYY-MM-DD
    """    
    def __init__(self, id_rendimento, descricao, valor, data):
        self.id_rendimento = id_rendimento
        self.descricao = descricao
        self.valor = valor
        self.data = data