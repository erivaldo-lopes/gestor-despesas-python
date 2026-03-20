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
from database.queries import inserir_despesa, inserir_rendimento, listar_despesas, listar_rendimentos, listar_categorias
from decimal import Decimal as dec
from datetime import datetime
from utils.con_utils import clear_screen, pause, show_msg, ask


DEFAULT_DATA = datetime.strptime("2020-12-31", "%Y-%m-%d").date()

def main():

    try:
        conexao = conectar()
        show_msg("Ligaçao à base de dados bem sucedida!")
        conexao.close()
    except Exception as e:
        show_msg("Erro ao ligar à base de dados: ", e)

    while True:
        clear_screen()
        show_msg(
    """\n
     GESTOR DE DESPESAS
        1 - Inserir despesa
        2 - Listar despesas
        3 - Inserir rendimento
        4 - Listar rendimentos
        0 - Sair
    """)

        opcao = ask("Escolhe uma opão... ", indent=6)

        match opcao:
            case "1": inserir_despesa_ui() 
            case "2": listar_despesas_ui()
            case "3": inserir_rendimento_ui()
            case "4": listar_rendimentos_ui()
            case "0":
                pause("Enter para sair", indent=6)
                clear_screen()

                break
            case _:  show_msg("Opção inválida")
def header(titulo: str):
    clear_screen()
    print()
    show_msg(f"*****{titulo}*****")
    print()


def inserir_despesa_ui():
    titulo = "NOVA DESPESA"
    header(titulo)

    # 1. Carregar categorias como um dicionário de IDs {id: nome}
    categorias_dict = {id: nome for id, nome in listar_categorias()}

    try:
        # --- DESCRIÇÃO ---
        descricao = ask("Descrição: ")
        if not descricao:
            raise Exception("A descrição não pode estar vazia!")

        # --- VALOR ---
        valor_input = ask("Valor: ")
        try:
            valor = float(valor_input)
        except ValueError:
            raise Exception("O valor inserido não é válido!")
        if valor <= 0:
            raise Exception("O valor deve ser superior a 0!")

        # --- DATA ---
        data_input = ask("Data (AAAA-MM-DD) [Enter para Hoje]: ")
        if data_input:
            if len(data_input) != 10:
                raise Exception("Data deve ter o formato AAAA-MM-DD.")
            data = datetime.strptime(data_input, "%Y-%m-%d").date()
        else:
            data = datetime.now().date()

        print()
        # --- CATEGORIA (SELEÇÃO POR ID) ---
        show_msg("Categorias disponíveis:")
        for id_cat, nome_cat in categorias_dict.items():
            show_msg(f" {id_cat} - {nome_cat}", indent=6)
        print()
        id_escolhido = ask("Digite o NÚMERO da categoria: ")

        # Validar se o ID é um número e se existe no dicionário
        if not id_escolhido.isdigit():
            raise Exception("Deves inserir o número (ID) da categoria!")
        
        id_categoria = int(id_escolhido)
        if id_categoria not in categorias_dict:
            raise Exception(f"O ID '{id_categoria}' não existe na lista!")

        # --- INSERIR NA BD ---
        # Agora passamos o id_categoria (inteiro) que a base de dados espera
        inserir_despesa(descricao, valor, data, id_categoria)

    except Exception as exc:
        show_msg(f"\n Erro: {exc}")

    finally:
        print()
        pause()


def listar_despesas_ui():
    titulo = "LISTA DE DESPESAS"
    header(titulo)
    categorias_validas = [c for _, c in listar_categorias() if c]
    try:
        # VALOR
        valor_input = ask("Valor mínimo: ")
        try:
            valor = float(valor_input) if valor_input else 0.0
        except ValueError:
            raise Exception("O valor inserido não é válido!")

        # DATA
        data_input = ask("Data início (AAAA-MM-DD): ")
        if data_input:
            if len(data_input) != 10:
                raise Exception("Data deve ter o formato AAAA-MM-DD.")
            data = datetime.strptime(data_input, "%Y-%m-%d").date()
        else:
            data = DEFAULT_DATA

        # CATEGORIA
        categoria = ask("Categoria: ")
        if categoria and categoria not in categorias_validas:
            raise Exception(f"Categoria '{categoria}' inválida! Escolha entre: {', '.join(str(c) for c in categorias_validas)}")
        categoria = categoria if categoria else None

        # QUERY
        despesas = listar_despesas(valor, data, categoria)

        print()
        if not despesas:
            show_msg("Sem registos de despesas encontradas...")
        else:
            show_msg(f"{'ID':<4} {'Descrição':<32} {'Valor':<10} {'Data':<12} {'Tipo':<15}")
            show_msg("-" * 75)

            for d in despesas:
                match d:
                    case (id, desc, valor_d, data_d, tipo):
                        show_msg(f"{id:<4} {desc:<32} {valor_d:<10.2f} {data_d.isoformat():<12} {tipo:<15}") # type: ignore

    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()

def inserir_rendimento_ui():
    titulo = "NOVO RENDIMENTO"
    header(titulo)

    try:
        # DESCRIÇÃO
        descricao = ask("Descrição: ")
        if not descricao:
            raise Exception("A descrição não pode estar vazia!")

        # VALOR
        valor_input = ask("Valor: ")
        try:
            valor = float(valor_input)
        except ValueError:
            raise Exception("O valor inserido não é um número válido!")

        if valor <= 0:
            raise Exception("O valor do rendimento deve ser superior a 0!")

        # DATA
        data_input = ask("Data (AAAA-MM-DD) [Enter para Hoje]: ")
        if data_input:
            if len(data_input) != 10:
                raise Exception("Data deve ter o formato AAAA-MM-DD.")
            data = datetime.strptime(data_input, "%Y-%m-%d").date()
        else:
            data = datetime.now().date()

        # INSERIR NA BD (Sem o parâmetro categoria)
        inserir_rendimento(descricao, valor, data)


    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()


def listar_rendimentos_ui():
    titulo = "LISTA DE RENDIMENTOS"
    header(titulo)
    try:
        valor_input = ask("Valor mínimo: ")
        if valor_input and not valor_input.replace('.', '', 1).isdigit():
            raise Exception("O valor inserido não é um número válido!")
        valor = float(valor_input) if valor_input else 0.00

        data_input = ask("Data início (AAAA-MM-DD): ")
        if data_input:
            if len(data_input) != 10:
                raise Exception("Data deve ter o formato AAAA-MM-DD.")
            data = datetime.strptime(data_input, "%Y-%m-%d").date() # type: ignore
        else:
            data = DEFAULT_DATA

        rendimentos = listar_rendimentos(valor, data)
        
        print()
        if not rendimentos:
            show_msg("Sem registos de rendimento encontrados...")
        else:
            show_msg(f"{'ID':<4} {'Descrição':<32} {'Valor':<12} {'Data':<12}")
            show_msg("-" * 65)
            
            for r in rendimentos:
                match r:
                    case (id, desc, rend, data):
                        show_msg(f"{id:<4} {desc:<32} {rend:<12.2f} {data.isoformat():<12}") # type: ignore

    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()


if __name__ == "__main__":
    main()