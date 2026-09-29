import json
from dataclasses import asdict, dataclass
from pathlib import Path


# ============================================================
# 1. PYTHON -> STRING JSON
# ============================================================

user_data = {
    "name": "Joao",
    "age": 26,
    "active": True,
}

json_text = json.dumps(
    user_data,
    indent=4,
    ensure_ascii=False,
)

print(json_text)
print(type(json_text))


# ============================================================
# 2. STRING JSON -> PYTHON
# ============================================================

loaded_data = json.loads(json_text)

print(loaded_data)
print(type(loaded_data))


# ============================================================
# 3. SALVANDO JSON EM ARQUIVO
# ============================================================

config_path = Path("data/config.json")

config_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)

with config_path.open(
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        user_data,
        file,
        indent=4,
        ensure_ascii=False,
    )


# ============================================================
# 4. LENDO JSON DE ARQUIVO
# ============================================================

with config_path.open(
    "r",
    encoding="utf-8",
) as file:
    loaded_user_data = json.load(file)

print(loaded_user_data)


# ============================================================
# 5. DATACLASS -> DICT -> JSON
# ============================================================

@dataclass
class User:
    name: str
    age: int
    active: bool = True


user = User(
    name="Joao",
    age=26,
)

user_dict = asdict(user)

print(user_dict)

user_json = json.dumps(
    user_dict,
    indent=4,
    ensure_ascii=False,
)

print(user_json)


# ============================================================
# 6. JSON -> DICT -> DATACLASS
# ============================================================

json_text = """
{
    "name": "Joao",
    "age": 26,
    "active": true
}
"""

user_data = json.loads(json_text)

user = User(**user_data)

print(user)
print(type(user))


# ============================================================
# 7. CONFIGURAÇÃO DE TREINAMENTO
# ============================================================

@dataclass(
    frozen=True,
    slots=True,
)
class TrainingConfig:
    batch_size: int
    learning_rate: float
    epochs: int


training_config = TrainingConfig(
    batch_size=32,
    learning_rate=0.001,
    epochs=20,
)

training_config_path = Path(
    "data/training_config.json"
)

with training_config_path.open(
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        asdict(training_config),
        file,
        indent=4,
        ensure_ascii=False,
    )


with training_config_path.open(
    "r",
    encoding="utf-8",
) as file:
    loaded_training_config_data = json.load(file)

loaded_training_config = TrainingConfig(
    **loaded_training_config_data
)

print(loaded_training_config)