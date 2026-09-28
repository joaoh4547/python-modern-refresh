from contextlib import contextmanager


# ============================================================
# 1. CONTEXT MANAGER COM ARQUIVO
# ============================================================

with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Olá, mundo")


# ============================================================
# 2. EQUIVALENTE SEM WITH
# ============================================================

file = open("example_manual.txt", "w", encoding="utf-8")

try:
    file.write("Olá, mundo")
finally:
    file.close()


# ============================================================
# 3. CONTEXT MANAGER MANUAL COM __enter__ E __exit__
# ============================================================

class Connection:
    def __enter__(self):
        print("Abrindo conexão")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Fechando conexão")


with Connection() as connection:
    print("Usando conexão")


# ============================================================
# 4. CONTEXT MANAGER COM contextlib.contextmanager
# ============================================================

@contextmanager
def connection():
    print("Abrindo conexão")

    try:
        yield "CONEXÃO ATIVA"
    finally:
        print("Fechando conexão")


with connection() as conn:
    print("Usando:", conn)


# ============================================================
# 5. CLEANUP MESMO QUANDO OCORRE ERRO
# ============================================================

try:
    with connection() as conn:
        print("Usando:", conn)

        raise RuntimeError("deu ruim")

except RuntimeError as error:
    print("Erro capturado:", error)