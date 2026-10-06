"""Desafio 3: realizar uma operação simples entre dois números."""


def main():
    try:
        # float() permite decimais; replace() também aceita a vírgula decimal.
        primeiro_numero = float(input("Digite o primeiro número: ").replace(",", "."))
        segundo_numero = float(input("Digite o segundo número: ").replace(",", "."))
    except ValueError:
        print("Entrada inválida: informe dois números válidos.")
        return

    operacao = input("Escolha a operação (+, -, *, /): ").strip()

    if operacao == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "*":
        resultado = primeiro_numero * segundo_numero
    elif operacao == "/":
        if segundo_numero == 0:
            print("Não é possível dividir por zero.")
            return
        resultado = primeiro_numero / segundo_numero
    else:
        print("Operação inválida: escolha +, -, * ou /.")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
