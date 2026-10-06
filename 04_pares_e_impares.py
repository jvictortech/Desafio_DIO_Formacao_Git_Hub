"""Desafio 4: verificar se um número inteiro é par ou ímpar."""


def main():
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida: informe um número inteiro.")
        return

    # % calcula o resto da divisão. Um número par tem resto zero ao dividir por 2.
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")


if __name__ == "__main__":
    main()
