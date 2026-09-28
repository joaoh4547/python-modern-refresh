from functools import wraps
from time import perf_counter


# ============================================================
# 1. FUNÇÃO COMO OBJETO
# ============================================================

def execute(function):
    print("Antes")

    function()

    print("Depois")


def say_hello():
    print("Olá")


execute(say_hello)


# ============================================================
# 2. DECORATOR BÁSICO
# ============================================================

def log_execution(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Iniciando: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finalizando: {function.__name__}")

        return result

    return wrapper


@log_execution
def sum_numbers(a: int, b: int) -> int:
    return a + b


result = sum_numbers(10, 20)

print("Resultado:", result)


# ============================================================
# 3. PRESERVANDO METADADOS COM @wraps
# ============================================================

print("Nome da função:", sum_numbers.__name__)


# ============================================================
# 4. DECORATOR PRÁTICO: MEDIR TEMPO
# ============================================================

def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        result = function(*args, **kwargs)

        end = perf_counter()

        elapsed = end - start

        print(
            f"{function.__name__} levou "
            f"{elapsed:.6f} segundos"
        )

        return result

    return wrapper


@measure_time
def calculate_sum(limit: int) -> int:
    return sum(range(limit))


result = calculate_sum(1_000_000)

print("Soma:", result)


# ============================================================
# 5. MÚLTIPLOS DECORATORS
# ============================================================

@log_execution
@measure_time
def process_data(limit: int) -> int:
    return sum(
        number ** 2
        for number in range(limit)
    )


result = process_data(100_000)

print("Resultado:", result)