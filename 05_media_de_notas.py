"""Desafio 5: calcular a média aritmética de três notas."""


def main():
    try:
        primeira_nota = float(input("Digite a primeira nota: ").replace(",", "."))
        segunda_nota = float(input("Digite a segunda nota: ").replace(",", "."))
        terceira_nota = float(input("Digite a terceira nota: ").replace(",", "."))
    except ValueError:
        print("Entrada inválida: informe três notas numéricas.")
        return

    media = (primeira_nota + segunda_nota + terceira_nota) / 3

    # .2f exibe o resultado com duas casas decimais.
    print(f"Média: {media:.2f}")


if __name__ == "__main__":
    main()
