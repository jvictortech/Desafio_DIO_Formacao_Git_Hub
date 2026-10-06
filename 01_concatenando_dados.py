"""Desafio 1: receber dois dados e concatená-los em uma string."""


def main():
    # input() sempre devolve uma string, mesmo se o usuário digitar números.
    primeiro_dado = input("Digite o primeiro dado: ")
    segundo_dado = input("Digite o segundo dado: ")

    resultado = primeiro_dado + segundo_dado
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
