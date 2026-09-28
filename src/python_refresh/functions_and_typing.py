from dataclasses import dataclass
from enum import Enum


# ============================================================
# 1. TYPE HINTS BÁSICOS
# ============================================================

def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)

print(result)

# Type hint não impede execução em runtime.
# O PyCharm reclama, mas o Python ainda executa.
print(add("10", "20"))


# ============================================================
# 2. TIPOS COMPOSTOS
# ============================================================

def average(values: list[float]) -> float:
    return sum(values) / len(values)


print(average([10.0, 20.0, 30.0]))


# ============================================================
# 3. TYPE ALIASES
# ============================================================

type UserId = int
type UserData = dict[str, str]


def find_user(user_id: UserId) -> UserData | None:
    if user_id == 1:
        return {
            "name": "Joao",
            "email": "joao@email.com",
        }

    return None


print(find_user(1))
print(find_user(999))


# ============================================================
# 4. DATACLASS
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

print(user)
print(user.name)


# ============================================================
# 5. DATACLASS IMUTÁVEL
# ============================================================

@dataclass(frozen=True)
class Config:
    host: str
    port: int


config = Config(
    host="localhost",
    port=5432,
)

print(config)

# Gera FrozenInstanceError:
# config.port = 3306


# ============================================================
# 6. DATACLASS COM SLOTS
# ============================================================

@dataclass(slots=True)
class Product:
    name: str
    price: float


product = Product(
    name="Teclado",
    price=200.0,
)

print(product)

# Não é possível adicionar atributo não declarado:
# product.stock = 10

print("Possui __dict__?", hasattr(product, "__dict__"))


# ============================================================
# 7. ENUM
# ============================================================

class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BLOCKED = "blocked"


status = UserStatus.ACTIVE

print(status)
print(status.name)
print(status.value)


# ============================================================
# 8. ENUM EM FUNÇÕES
# ============================================================

def can_login(status: UserStatus) -> bool:
    return status == UserStatus.ACTIVE


print(can_login(UserStatus.ACTIVE))
print(can_login(UserStatus.BLOCKED))


# ============================================================
# 9. MATCH / CASE
# ============================================================

def describe_status(status: UserStatus) -> str:
    match status:
        case UserStatus.ACTIVE:
            return "Usuário ativo"

        case UserStatus.INACTIVE:
            return "Usuário inativo"

        case UserStatus.BLOCKED:
            return "Usuário bloqueado"

        case _:
            return "Status desconhecido"


print(describe_status(UserStatus.ACTIVE))
print(describe_status(UserStatus.BLOCKED))