"""Desafio 2: repetir uma string a quantidade de vezes informada."""


def main():
    texto = input("Digite o texto: ")

    try:
        quantidade = int(input("Quantas vezes deseja repetir? "))
    except ValueError:
        print("Entrada inválida: informe um número inteiro.")
        return

    if quantidade < 0:
        print("A quantidade de repetições não pode ser negativa.")
        return

    # O operador * repete a string. Com zero repetições, o resultado é vazio.
    resultado = texto * quantidade
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
