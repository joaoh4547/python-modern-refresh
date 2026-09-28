# ============================================================
# 1. IMPORT ABSOLUTO
# ============================================================

from python_refresh.math_utils import add, subtract, average


print(add(10, 20))
print(subtract(30, 10))
print(average([10, 20, 30]))


# ============================================================
# 2. __name__
# ============================================================

print("Nome do módulo:", __name__)


# ============================================================
# 3. PONTO DE ENTRADA
# ============================================================

def main() -> None:
    print("Executando modules_and_packages como ponto de entrada")


if __name__ == "__main__":
    main()


# ============================================================
# 4. OBSERVAÇÃO SOBRE EXECUÇÃO COMO MÓDULO
# ============================================================

# Com estrutura src/, uma forma correta de executar este módulo
# é a partir da pasta src:
#
# python -m python_refresh.modules_and_packages
#
# Em vez de:
#
# python python_refresh/modules_and_packages.py
#
# Isso mantém o contexto de package e evita problemas
# com imports absolutos e relativos.


# ============================================================
# 5. IMPORT CIRCULAR - CONCEITO
# ============================================================

# Exemplo ruim:
#
# user_service.py
#     importa order_service.py
#
# order_service.py
#     importa user_service.py
#
# Isso pode gerar algo como:
#
# ImportError: cannot import name ...
# from partially initialized module ...
#
# Normalmente, a melhor solução é reorganizar as dependências
# ou extrair conceitos compartilhados para outro módulo.


# ============================================================
# 6. IMPORT LOCAL - USAR COM CUIDADO
# ============================================================

def optional_example() -> None:
    # Import local é permitido em Python.
    #
    # Pode ser útil para:
    # - dependência opcional
    # - biblioteca pesada
    # - evitar carregar algo sem necessidade
    #
    # Mas não deve ser usado como muleta para esconder
    # problemas de arquitetura/import circular.

    import math

    print(math.sqrt(16))


optional_example()