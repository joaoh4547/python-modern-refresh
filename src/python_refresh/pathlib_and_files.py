from pathlib import Path


# ============================================================
# 1. PARTES DO CAMINHO
# ============================================================

file_path = Path("data/example.csv")

print("Caminho:", file_path)
print("Parent:", file_path.parent)
print("Name:", file_path.name)
print("Stem:", file_path.stem)
print("Suffix:", file_path.suffix)


# ============================================================
# 2. CAMINHO ABSOLUTO
# ============================================================

absolute_path = file_path.resolve()

print("Relativo:", file_path)
print("Absoluto:", absolute_path)


# ============================================================
# 3. CRIANDO ESTRUTURA DE DIRETÓRIOS
# ============================================================

project_root = Path.cwd()

directories = [
    project_root / "datasets" / "raw",
    project_root / "datasets" / "processed",
    project_root / "artifacts" / "models",
    project_root / "artifacts" / "metrics",
]

for directory in directories:
    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("Diretório pronto:", directory)

raw_dir = project_root / "datasets" / "raw"

(raw_dir / "users.csv").write_text(
    "id,name\n1,Joao",
    encoding="utf-8",
)

(raw_dir / "products.csv").write_text(
    "id,name\n1,Teclado",
    encoding="utf-8",
)

(raw_dir / "notes.txt").write_text(
    "Arquivo de teste",
    encoding="utf-8",
)

print("\nTodos os arquivos:")

for item in raw_dir.iterdir():
    print(item)

print("\nArquivos CSV:")

for csv_file in raw_dir.glob("*.csv"):
    print(csv_file)

archive_dir = raw_dir / "archive"

archive_dir.mkdir(
    parents=True,
    exist_ok=True,
)

(archive_dir / "old_users.csv").write_text(
    "id,name\n99,Antigo",
    encoding="utf-8",
)


print('\n')

for csv_file in raw_dir.glob("*.csv"):
    print(csv_file)

print('\n')

for csv_file in raw_dir.rglob("*.csv"):
    print(csv_file)