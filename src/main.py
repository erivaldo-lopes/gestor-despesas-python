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
from services.gestor_financas import (
    inserir_despesa,
    listar_despesas,
    editar_despesa,
    eliminar_despesa,
    inserir_rendimento,
    listar_rendimentos,
    editar_rendimento,
    eliminar_rendimento,
    listar_categorias,
    calcular_saldo,
    total_despesas,
    total_rendimentos,
    validar_descricao,
    validar_valor,
    validar_data,
    validar_categoria, 
    validar_id,
    buscar_por_id
)
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
        3 - Editar despesa
        4 - Eliminar despesa
        5 - Inserir rendimento
        6 - Listar rendimentos
        7 - Editar rendimento
        8 - Eliminar rendimento
        9 - Mostrar saldo
        0 - Sair
    """)

        opcao = ask("Escolhe uma opção... ", indent=6)

        match opcao:
            case "1": inserir_despesa_ui() 
            case "2": listar_despesas_ui()
            case "3": editar_despesa_ui()
            case "4": eliminar_despesa_ui()
            case "5": inserir_rendimento_ui()
            case "6": listar_rendimentos_ui()
            case "7": editar_rendimento_ui()
            case "8": eliminar_rendimento_ui()
            case "9": mostrar_saldo_ui()
            case "0":
                pause("Enter para sair", indent=6)
                clear_screen()

                break
            case _:  show_msg("Opção inválida")


# ************* CABEÇALHO ************************************


def header(titulo: str):
    clear_screen()
    print()
    show_msg(f"*****{titulo}*****")
    print()



# ************* DESPESAS ************************************

def inserir_despesa_ui():
    header("NOVA DESPESA")
    categorias_validas = {id: nome for id, nome in listar_categorias()}
    try:
        descricao = validar_descricao()
        valor = validar_valor()
        saldo_atual = calcular_saldo()
        if valor > saldo_atual:
            show_msg(f"Saldo insuficiente! (Saldo atual: {saldo_atual:.2f})")
            return
        data = validar_data(msg="Data (AAAA-MM-DD) [Enter para hoje]: ")
        id_categoria = validar_categoria(categorias_validas)
        inserir_despesa(descricao, valor, data, id_categoria)
    except Exception as exc:
        show_msg(f"Erro: {exc}")
    finally:
        print()
        pause()


def listar_despesas_ui():
    header("LISTA DE DESPESAS")
    categorias_validas = {id: nome for id, nome in listar_categorias()}
    try:
        valor = validar_valor("Valor mínimo: ", permitir_zero=True)
        data = validar_data(msg="Data inicial (AAAA-MM-DD) [Enter para todos]: ", obrigatoria=False)
        categoria = validar_categoria(categorias_validas, obrigatoria=False)
        despesas = listar_despesas(valor, data, categoria)

        print()
        if not despesas:
            show_msg("Sem registos de despesas encontradas...")
        else:
            show_msg(f"{'ID':<4} {'Descrição':<32} {'Valor':>8} {'Data':^12} {'Tipo':<17}")
            show_msg("-" * 75)

            for d in despesas:
                match d:
                    case (id, desc, valor_d, data_d, tipo):
                        show_msg(f"{id:<4} {desc:<32} {valor_d:>8.2f} {data_d.isoformat():^12} {tipo:<17}") # type: ignore

    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()


def editar_despesa_ui():
    header("EDITAR DESPESA")
    categorias_validas = {id: nome for id, nome in listar_categorias()}

    try:
        id_despesa = validar_id("ID da despesa: ")
        despesa = buscar_por_id("despesas", id_despesa)
        if despesa:
            show_msg(f"Despesa encontrada: {despesa}")

        descricao = validar_descricao("Nova descrição: ")
        valor = validar_valor("Novo valor: ")
        data = validar_data("Nova data: ")
        id_categoria = validar_categoria(categorias_validas)

        editar_despesa(id_despesa, descricao, valor, data, id_categoria)
        show_msg("Despesa atualizada com sucesso!")

    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()

def eliminar_despesa_ui():
    header("ELIMINAR DESPESA")
    try:
        id_despesa = validar_id()
        despesa = buscar_por_id("despesas", id_despesa)
        if despesa:
            show_msg(f"Despesa encontrada: {despesa}")
        confirm = ask("Tem a certeza que deseja eliminar? (s/n): ")

        if confirm.lower() != 's':
            show_msg("Operação cancelada.")
            return

        eliminar_despesa(id_despesa)
        show_msg("Despesa eliminada com sucesso!")

    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()


# ************* RENDIMENTOS ************************************

def inserir_rendimento_ui():
    header("NOVO RENDIMENTO")
    try:
        descricao = validar_descricao()
        valor = validar_valor()
        data = validar_data(msg="Data (AAAA-MM-DD) [Enter para hoje]: ")

        inserir_rendimento(descricao, valor, data)
    except Exception as exc:
        show_msg(f"Erro: {exc}")
    finally:
        print()
        pause()


def listar_rendimentos_ui():
    header("LISTA DE RENDIMENTOS")
    try:
        valor = validar_valor("Valor mínimo: ", permitir_zero=True)
        data = validar_data(msg="Data inicial (AAAA-MM-DD) [Enter para todos]: ", obrigatoria=False)
        rendimentos = listar_rendimentos(valor, data)
        
        print()
        if not rendimentos:
            show_msg("Sem registos de rendimento encontrados...")
        else:
            show_msg(f"{'ID':<4} {'Descrição':<32} {'Valor':>8} {'Data':^12}")
            show_msg("-" * 65)
            for r in rendimentos:
                match r:
                    case (id, desc, rend, data):
                        show_msg(f"{id:<4} {desc:<32} {rend:>8.2f} {data.isoformat():>12}") # type: ignore

    except Exception as exc:
        show_msg(f"Erro: {exc}")
    finally:
        print()
        pause()


def editar_rendimento_ui():
    header("EDITAR RENDIMENTO")
    
    try:
        id_rendimento = validar_id("ID do rendimento: ")
        rendimento = buscar_por_id("rendimentos", id_rendimento)
        
        if rendimento:
            show_msg(f"Rendimento encontrado: {rendimento}")

        descricao = validar_descricao("Nova descrição: ")
        valor = validar_valor("Novo valor: ")
        data = validar_data("Nova data: ")

        # Chamada sem a categoria
        editar_rendimento(id_rendimento, descricao, valor, data)
        show_msg("Rendimento atualizado com sucesso!")

    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()

def eliminar_rendimento_ui():
    header("ELIMINAR RENDIMENTO")
    try:
        id_rendimento = validar_id("ID do rendimento: ")
        rendimento = buscar_por_id("rendimentos", id_rendimento)
        
        if rendimento:
            show_msg(f"Rendimento encontrado: {rendimento}")
        confirm = ask("Tem a certeza que deseja eliminar? (s/n): ")

        if confirm.lower() != 's':
            show_msg("Operação cancelada.")
            return

        eliminar_rendimento(id_rendimento)
        show_msg("Rendimento eliminado com sucesso!")

    except Exception as exc:
        show_msg(f"Erro: {exc}")

    finally:
        print()
        pause()



# ************* SALDOS ************************************

def mostrar_saldo_ui():
    header("CONSULTAR SALDO")
    try:
        total_r = total_rendimentos()
        total_d = total_despesas()
        saldo = calcular_saldo()

        print()
        show_msg(f"Total Rendimentos: {total_r:>10.2f}€")
        show_msg(f"Total Despesas:    {total_d:>10.2f}€")
        show_msg("-" * 30)
        show_msg(f"Saldo Atual:       {saldo:>10.2f}€")

    except Exception as exc:
        show_msg(f"Erro: {exc}")
    finally:
        print()
        pause()



if __name__ == "__main__":
    main()