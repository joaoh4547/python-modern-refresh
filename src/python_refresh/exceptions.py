# ============================================================
# 1. TRY / EXCEPT
# ============================================================

def divide(a: float, b: float) -> float:
    return a / b


try:
    result = divide(10, 0)

    print("Resultado:", result)

except ZeroDivisionError as error:
    print("Não é possível dividir por zero")
    print("Erro original:", error)


# ============================================================
# 2. ELSE E FINALLY
# ============================================================

try:
    result = divide(10, 2)

except ZeroDivisionError:
    print("Não é possível dividir por zero")

else:
    print("Deu tudo certo")
    print("Resultado:", result)

finally:
    print("Essa parte sempre executa")


# ============================================================
# 3. RAISE
# ============================================================

def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("O valor do saque deve ser maior que zero")

    if amount > balance:
        raise ValueError("Saldo insuficiente")

    return balance - amount


try:
    new_balance = withdraw(1000, 1500)

    print("Novo saldo:", new_balance)

except ValueError as error:
    print("Erro:", error)


# ============================================================
# 4. EXCEÇÃO CUSTOMIZADA
# ============================================================

class InsufficientBalanceError(Exception):
    pass


def withdraw_with_custom_error(
    balance: float,
    amount: float,
) -> float:
    if amount <= 0:
        raise ValueError(
            "O valor do saque deve ser maior que zero"
        )

    if amount > balance:
        raise InsufficientBalanceError(
            f"Saldo insuficiente: saldo={balance}, saque={amount}"
        )

    return balance - amount


try:
    new_balance = withdraw_with_custom_error(
        1000,
        1500,
    )

except InsufficientBalanceError as error:
    print("Erro de saldo:", error)

except ValueError as error:
    print("Erro de valor:", error)


# ============================================================
# 5. ENCADEAMENTO DE EXCEÇÕES
# ============================================================

class ConfigurationError(Exception):
    pass


def load_port(config: dict[str, str]) -> int:
    try:
        return int(config["port"])

    except (KeyError, ValueError) as error:
        raise ConfigurationError(
            "Configuração de porta inválida"
        ) from error


config = {
    "port": "abc",
}

try:
    port = load_port(config)

    print("Porta:", port)

except ConfigurationError as error:
    print("Erro de configuração:", error)


# ============================================================
# 6. RELANÇANDO A EXCEÇÃO ATUAL
# ============================================================

def parse_number(value: str) -> int:
    try:
        return int(value)

    except ValueError:
        print("Falha ao converter valor")
        raise


try:
    parse_number("abc")

except ValueError as error:
    print("Erro capturado externamente:", error)


# ============================================================
# 7. CAPTURA DE MÚLTIPLAS EXCEÇÕES
# ============================================================

data = {
    "age": "abc",
}

try:
    age = int(data["age"])

except (KeyError, ValueError) as error:
    print("Dado inválido:", error)


# ============================================================
# 8. ORDEM DOS EXCEPTS
# ============================================================

try:
    int("abc")

except ValueError:
    print("Erro específico de valor")

except Exception:
    print("Erro genérico")


# ============================================================
# 9. EXCEPTION GENÉRICA COM RELANÇAMENTO
# ============================================================

def process_dataset() -> None:
    raise RuntimeError(
        "Falha inesperada durante o processamento"
    )


try:
    process_dataset()

except Exception as error:
    print("Erro inesperado:", error)

    # Não esconde o problema:
    # raise