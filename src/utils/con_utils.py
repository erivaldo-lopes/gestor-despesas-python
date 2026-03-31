"""
    Utilitários (essencialmente funções) para usar em programas que
    correm no terminal.
"""

import os

__all__ = (
    'ask',
    'show_msg',
    'pause',
    'clear_screen',
)

_indentation = 3

def ask(msg: str, indent: int | None = None) -> str:
    """Solicita input ao utilizador com indentação."""
    indent = _indentation if indent is None else indent
    return input(f"{indent * ' '}{msg}")

def show_msg(*args, indent: int | None = None, **kargs):
    """Exibe uma mensagem no terminal com indentação."""
    indent = _indentation if indent is None else indent
    print_args = [' ' * (indent - 1), *args] if indent > 0 else [*args]
    print(*print_args, **kargs)

def clear_screen():
    """Limpa o terminal conforme o sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause( msg: str = "Pressione [Enter] para continuar...", indent: int | None = None):
    """Faz uma pausa na execução e aguarda input."""
    indent = _indentation if indent is None else indent
    ask(msg, indent)
