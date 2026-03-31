"""
    Projeto: Sistema de Gestão de Despesas Pessoais
    Ficheiro: gestor_financas.py

    Descrição:
    Este módulo representa a camada de lógica da aplicação (services),
    responsável por intermediar a comunicação entre a interface (main)
    e a base de dados (queries).

    Inclui:
    - Encaminhamento de operações de despesas e rendimentos
    - Cálculo de totais e saldo financeiro
    - Validação de inputs do utilizador
    - Verificação da existência de registos antes de operações críticas

    Objetivo:
    Centralizar a lógica de negócio da aplicação, garantindo uma separação
    clara entre interface, lógica e acesso a dados.

    Autor: Erivaldo Jorge Centeio Lopes
    Data: 30/03/2026
    Curso: NST PROG28 - Programador de Infromática
"""

from database import queries 
from datetime import datetime
from utils.con_utils import ask, show_msg

DEFAULT_DATA = datetime.strptime("2020-12-31", "%Y-%m-%d").date()

# ------- VALIDAÇÕES ---------------------------------

def validar_descricao(msg="Descrição: "):
    """
    Pede uma descrição válida (não vazia e até 30 caracteres).
    """
    while True:
        descricao = ask(msg)
        if not descricao:
            show_msg("Erro: A descrição não pode estar vazia.")
            continue
        
        if len(descricao) > 30:
            show_msg(f"Erro: A descrição é demasiado longa. MAX: 30 caracteres).")
            continue
            
        return descricao



def validar_valor(msg="Valor: ", permitir_zero=False):
    """
    Valida um valor numérico positivo.
    """
    while True:
        valor_input = ask(msg)
        try:
            valor = float(valor_input)

            if valor < 0 or (valor == 0 and not permitir_zero):
                raise ValueError

            return valor
        except ValueError:
            show_msg("Valor inválido! Insira um número positivo.")


def validar_data(msg, obrigatoria=True):
    """
    Valida uma data no formato YYYY-MM-DD.

    - Se obrigatória e vazio → assume data atual
    - Se não obrigatória e vazio → assume DEFAULT_DATA
    """
    from datetime import datetime

    while True:
        data_input = ask(msg)

        if not data_input:
            if obrigatoria:
                return datetime.now().date()
            else:
                return DEFAULT_DATA

        try:
            if len(data_input) != 10:
                raise ValueError

            return datetime.strptime(data_input, "%Y-%m-%d").date()
        except ValueError:
            show_msg("Formato de data inválido! Use AAAA-MM-DD.")


def validar_categoria(categorias_dict, obrigatoria=True):
    """
    Valida seleção de categoria por ID.

    - Se obrigatória=False e input vazio → retorna None
    - Se houver input → valida sempre
    """

    while True:
        show_msg("Categorias disponíveis:")
        for id_cat, nome in categorias_dict.items():
            show_msg(f"{id_cat} - {nome}", indent=6)

        escolha = ask("Escolha o ID da categoria: ")

        # Caso não obrigatório e vazio
        if not escolha:
            if not obrigatoria:
                return None
            show_msg("Categoria obrigatória!")
            continue

        # Validação do input
        if not escolha.isdigit():
            show_msg("Deve inserir um número válido!")
            continue

        escolha = int(escolha)

        if escolha not in categorias_dict:
            show_msg("Categoria inválida!")
            continue

        return escolha


def validar_id(msg="ID: "):
    """
    Valida um ID numérico.
    """
    while True:
        valor = ask(msg)
        if valor.isdigit():
            return int(valor)
        show_msg("ID inválido!")



# ---------- DESPESAS ----------
def inserir_despesa(*args, **kwargs):
    """
    Encaminha a inserção de uma despesa para a camada de base de dados.
    """

    return queries.inserir_despesa(*args, **kwargs)
    

def listar_despesas(*args, **kwargs):
    """
    Obtém a lista de despesas com possíveis filtros aplicados.
    """

    return queries.listar_despesas(*args, **kwargs)


def editar_despesa(*args, **kwargs):
    """
    Edita uma despesa existente.
    """

    return queries.editar_despesa(*args, **kwargs)


def eliminar_despesa(id_despesa):
    """
    Elimina uma despesa existente.
    """
    return queries.eliminar_despesa(id_despesa)



# ---------- RENDIMENTOS ----------
def inserir_rendimento(*args, **kwargs):
    """
    Encaminha a inserção de um rendimento para a base de dados.
    """

    return queries.inserir_rendimento(*args, **kwargs)

def listar_rendimentos(*args, **kwargs):
    """
    Obtém a lista de rendimentos com possíveis filtros.
    """

    return queries.listar_rendimentos(*args, **kwargs)


def editar_rendimento(*args, **kwargs):
    """
    Edita um rendimento existente.
    """
    return queries.editar_rendimento(*args, **kwargs)


def eliminar_rendimento(id_rendimento):
    """
    Elimina um rendimento existente.
    """
    return queries.eliminar_rendimento(id_rendimento)



# ---------- CATEGORIAS ----------
def listar_categorias():
    """
    Retorna todas as categorias disponíveis na base de dados.
    """

    return queries.listar_categorias()


# ---------- GERAL ----------

def total_despesas():
    """
    Calcula o somatório de todos os registos na tabela de despesas.
    Returns:
        float: Valor total das despesas encontradas.
    """

    return queries.somar_coluna("despesas")

def total_rendimentos():
    """
    Calcula o somatório de todos os registos na tabela de rendimentos.
    Returns:
        float: Valor total dos rendimentos encontrados.
    """

    return queries.somar_coluna("rendimentos")


def calcular_saldo():
    """
    Calcula a diferença líquida entre o total de rendimentos e despesas.
    Returns:
        float: O saldo final (Rendimentos - Despesas).
    """

    return total_rendimentos() - total_despesas()

def buscar_por_id(tabela, id_procurado):
    """
    Procura um registo pelo ID numa tabela específica.
    Parâmetros:
    tabela (str): nome da tabela
    id_procurado (int): ID a procurar
    Retorna:
    tuple: registo encontrado
    Lança:
    Exception: caso o registo não exista
    """

    item = queries.buscar_por_id(tabela, id_procurado)
    if item is None:
        raise Exception("Registo não encontrado!")
    return item