import csv
from pathlib import Path


# ============================================================
# 1. PREPARANDO DIRETÓRIO
# ============================================================

data_dir = Path("data")

data_dir.mkdir(
    parents=True,
    exist_ok=True,
)


# ============================================================
# 2. ESCREVENDO CSV COM csv.writer
# ============================================================

csv_path = data_dir / "users.csv"

users = [
    ["id", "name", "age"],
    [1, "Joao", 26],
    [2, "Maria", 24],
    [3, "Ana", 31],
]

with csv_path.open(
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.writer(file)

    writer.writerows(users)


# ============================================================
# 3. LENDO CSV COM csv.reader
# ============================================================

with csv_path.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# 4. LENDO CSV COM DictReader
# ============================================================

with csv_path.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# ============================================================
# 5. ESCREVENDO CSV COM DictWriter
# ============================================================

users_dict = [
    {
        "id": 1,
        "name": "Joao",
        "age": 26,
    },
    {
        "id": 2,
        "name": "Maria",
        "age": 24,
    },
]

dict_csv_path = data_dir / "users_dict.csv"

with dict_csv_path.open(
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "id",
            "name",
            "age",
        ],
    )

    writer.writeheader()
    writer.writerows(users_dict)


# ============================================================
# 6. CAMPOS COM VÍRGULA
# ============================================================

users_with_city = [
    {
        "id": 1,
        "name": "Joao",
        "city": "Novo Horizonte, SP",
    },
    {
        "id": 2,
        "name": "Maria",
        "city": "Rio de Janeiro, RJ",
    },
]

city_path = data_dir / "users_with_city.csv"

with city_path.open(
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "id",
            "name",
            "city",
        ],
    )

    writer.writeheader()
    writer.writerows(users_with_city)


# ============================================================
# 7. DELIMITADOR PERSONALIZADO
# ============================================================

semicolon_path = data_dir / "users_semicolon.csv"

with semicolon_path.open(
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "id",
            "name",
            "age",
        ],
        delimiter=";",
    )

    writer.writeheader()
    writer.writerows(users_dict)


with semicolon_path.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    reader = csv.DictReader(
        file,
        delimiter=";",
    )

    for row in reader:
        print(row)


# ============================================================
# 8. CONVERSÃO DE TIPOS
# ============================================================

with dict_csv_path.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        user_id = int(row["id"])
        age = int(row["age"])

        print(
            f"id={user_id} ({type(user_id).__name__}), "
            f"age={age} ({type(age).__name__})"
        )


# ============================================================
# 9. CSV SEM HEADER
# ============================================================

no_header_path = data_dir / "users_no_header.csv"

no_header_path.write_text(
    "1,Joao,26\n"
    "2,Maria,24\n",
    encoding="utf-8",
)

with no_header_path.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    reader = csv.DictReader(
        file,
        fieldnames=[
            "id",
            "name",
            "age",
        ],
    )

    for row in reader:
        print(row)


# ============================================================
# 10. CSV COM DADOS INCONSISTENTES
# ============================================================

inconsistent_path = data_dir / "users_inconsistent.csv"

inconsistent_path.write_text(
    "id,name,age\n"
    "1,Joao,26\n"
    "2,Maria\n"
    "3,Ana,31,EXTRA\n",
    encoding="utf-8",
)

with inconsistent_path.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# ============================================================
# 11. DETECTANDO DELIMITADOR COM Sniffer
# ============================================================

unknown_delimiter_path = data_dir / "unknown_delimiter.csv"

unknown_delimiter_path.write_text(
    "id;name;age\n"
    "1;Joao;26\n"
    "2;Maria;24\n",
    encoding="utf-8",
)

with unknown_delimiter_path.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    sample = file.read(1024)

    dialect = csv.Sniffer().sniff(sample)

    print("Delimitador detectado:", dialect.delimiter)

    has_header = csv.Sniffer().has_header(sample)

    print("Tem header?", has_header)