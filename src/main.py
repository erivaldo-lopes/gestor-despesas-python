"""
    Ficheiro principal da aplicação.

    Responsável por iniciar o programa e gerir a interação
    com o utilizador através de menus.

    Funcionalidades principais:
    - registo de despesas
    - registo de rendimentos
    - listagem de dados
    - cálculo de saldo financeiro

    Autor: Erivaldo Jorge Centeio Lopes
    Data: 13/03/2026
    Curso: NST PROG28 - Programador de Infromática
"""

from database.connection import conectar
from database.queries import inserir_despesa, inserir_rendimento, listar_despesas, listar_rendimentos

def main():
    try:
        conexao = conectar()
        print("Ligaçao à base de dados bem sucedida!")
        conexao.close()
    except Exception as e:
        print("Erro ao ligar à base de dados: ", e)

    descricao = "Supermercado"
    valor = 45.50
    data = "2026-03-11"
    categoria = 1

    # inserir_despesa(descricao, valor, data, categoria)
    desp = listar_despesas(valor_min=0, data_inicio="2020-12-01")
    # desp2 = listar_despesas(data_inicio='2020-12-01')
    print(desp)


if __name__ == "__main__":
    main()