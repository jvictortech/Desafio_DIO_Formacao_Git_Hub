"""Desafio 6: verificar se uma palavra é um palíndromo."""


def main():
    palavra = input("Digite uma palavra: ").strip()

    if not palavra:
        print("Entrada inválida: digite uma palavra.")
        return

    # casefold() ignora diferenças entre letras maiúsculas e minúsculas.
    palavra_normalizada = palavra.casefold()
    # O fatiamento [::-1] produz uma string com os caracteres na ordem inversa.
    palavra_invertida = palavra_normalizada[::-1]

    if palavra_normalizada == palavra_invertida:
        print(f'"{palavra}" é um palíndromo.')
    else:
        print(f'"{palavra}" não é um palíndromo.')


if __name__ == "__main__":
    main()
