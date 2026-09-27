from copy import deepcopy


def show_section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ============================================================
# 1. REFERÊNCIAS E MUTABILIDADE
# ============================================================

show_section("1. Referências e mutabilidade")

numbers = [10, 20, 30]
other_numbers = numbers

other_numbers.append(40)

print("numbers:", numbers)
print("other_numbers:", other_numbers)

print("Mesmo objeto?", numbers is other_numbers)


# ============================================================
# 2. SHALLOW COPY
# ============================================================

show_section("2. Shallow copy")

numbers = [10, 20, 30]
other_numbers = numbers.copy()

other_numbers.append(40)

print("numbers:", numbers)
print("other_numbers:", other_numbers)

print("Mesmo objeto?", numbers is other_numbers)


# ============================================================
# 3. SHALLOW COPY COM OBJETOS INTERNOS
# ============================================================

show_section("3. Shallow copy com objetos internos")

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print("a:", a)
print("b:", b)

print("a e b são o mesmo objeto?", a is b)
print("a[0] e b[0] são o mesmo objeto?", a[0] is b[0])


# ============================================================
# 4. DEEP COPY
# ============================================================

show_section("4. Deep copy")

a = [[1, 2], [3, 4]]
b = deepcopy(a)

b[0].append(99)

print("a:", a)
print("b:", b)

print("a e b são o mesmo objeto?", a is b)
print("a[0] e b[0] são o mesmo objeto?", a[0] is b[0])


# ============================================================
# 5. LIST, TUPLE E SET
# ============================================================

show_section("5. List, tuple e set")

numbers_list = [10, 20, 20, 30]
numbers_tuple = (10, 20, 20, 30)
numbers_set = {10, 20, 20, 30}

print("list:", numbers_list)
print("tuple:", numbers_tuple)
print("set:", numbers_set)


# ============================================================
# 6. DICT
# ============================================================

show_section("6. Dict")

user = {
    "name": "Joao",
    "age": 26,
    "city": "Novo Horizonte",
}

print("Nome:", user["name"])

# get() não lança KeyError caso a chave não exista
print("Email:", user.get("email"))

# Também podemos definir um valor padrão
print("Email com fallback:", user.get("email", "não informado"))


# ============================================================
# 7. MERGE DE DICTS
# ============================================================

show_section("7. Merge de dicts")

user = {
    "name": "Joao",
    "age": 26,
}

updated_user = user | {
    "age": 27,
    "active": True,
}

print("Original:", user)
print("Atualizado:", updated_user)


# Forma equivalente usando unpacking:
updated_user_with_unpacking = {
    **user,
    "age": 27,
    "active": True,
}

print("Atualizado com **:", updated_user_with_unpacking)


# ============================================================
# 8. LIST COMPREHENSION
# ============================================================

show_section("8. List comprehension")

numbers = [1, 2, 3, 4, 5, 6]

squares = [
    number ** 2
    for number in numbers
]

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print("Quadrados:", squares)
print("Quadrados dos pares:", even_squares)


# ============================================================
# 9. DICT COMPREHENSION
# ============================================================

show_section("9. Dict comprehension")

names = ["ana", "joao", "maria"]

lengths = {
    name: len(name)
    for name in names
}

print("Tamanho dos nomes:", lengths)


long_name_lengths = {
    name: len(name)
    for name in names
    if len(name) > 3
}

print("Nomes com mais de 3 caracteres:", long_name_lengths)


# ============================================================
# 10. SET COMPREHENSION
# ============================================================

show_section("10. Set comprehension")

numbers = [1, 2, 2, 3, 3, 4]

squares_set = {
    number ** 2
    for number in numbers
}

print("Quadrados sem duplicação:", squares_set)


# ============================================================
# 11. *ARGS E **KWARGS
# ============================================================

show_section("11. *args e **kwargs")


def create_user(name, *skills, **details):
    print(f"Nome: {name}")
    print(f"Skills: {skills}")
    print(f"Detalhes: {details}")


create_user(
    "Joao",
    "Python",
    "Java",
    "SQL",
    age=26,
    active=True,
    city="Novo Horizonte",
)


# ============================================================
# 12. UNPACKING COM * E **
# ============================================================

show_section("12. Unpacking com * e **")

skills = [
    "Python",
    "Java",
    "SQL",
]

details = {
    "age": 26,
    "active": True,
    "city": "Novo Horizonte",
}

create_user(
    "Joao",
    *skills,
    **details,
)