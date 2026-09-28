import sys


# ============================================================
# 1. GENERATOR BÁSICO COM YIELD
# ============================================================

def count():
    print("começou")

    yield 1

    print("continuou")

    yield 2

    print("continuou de novo")

    yield 3


generator = count()

print(next(generator))
print(next(generator))
print(next(generator))

# Se descomentar, gera StopIteration:
# print(next(generator))


# ============================================================
# 2. RETURN VS YIELD
# ============================================================

def numbers_with_return(limit: int) -> list[int]:
    numbers = []

    for number in range(limit):
        numbers.append(number)

    return numbers


def numbers_with_yield(limit: int):
    for number in range(limit):
        yield number


numbers_list = numbers_with_return(5)
numbers_generator = numbers_with_yield(5)

print("Lista:", numbers_list)
print("Tipo da lista:", type(numbers_list))

print("Generator:", numbers_generator)
print("Tipo do generator:", type(numbers_generator))


# ============================================================
# 3. CONSUMINDO GENERATOR COM FOR
# ============================================================

for number in numbers_with_yield(5):
    print(number)


# ============================================================
# 4. DIFERENÇA DE MEMÓRIA
# ============================================================

large_list = numbers_with_return(1_000_000)
large_generator = numbers_with_yield(1_000_000)

print("Lista:", sys.getsizeof(large_list), "bytes")
print("Generator:", sys.getsizeof(large_generator), "bytes")


# ============================================================
# 5. GENERATOR É CONSUMÍVEL
# ============================================================

generator = numbers_with_yield(3)

print("Primeira leitura:", list(generator))
print("Segunda leitura:", list(generator))


# ============================================================
# 6. GENERATOR EXPRESSION
# ============================================================

squares_list = [
    number ** 2
    for number in range(10)
]

squares_generator = (
    number ** 2
    for number in range(10)
)

print("Lista de quadrados:", squares_list)
print("Generator de quadrados:", squares_generator)

print("Generator materializado:", list(squares_generator))


# ============================================================
# 7. USANDO GENERATOR DIRETO EM OUTRA FUNÇÃO
# ============================================================

total = sum(
    number ** 2
    for number in range(1000)
)

print("Soma dos quadrados:", total)


# ============================================================
# 8. EXEMPLO PRÁTICO: BATCHES
# ============================================================

def create_batches(data: list[int], batch_size: int):
    for start in range(0, len(data), batch_size):
        end = start + batch_size
        yield data[start:end]


dataset = list(range(1, 11))

for batch in create_batches(dataset, 3):
    print("Batch:", batch)