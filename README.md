# Resolvendo Códigos em Python com apoio de IA

Soluções dos seis exercícios do desafio **Resolvendo Códigos em Python com o GitHub Copilot**. Este projeto foi desenvolvido com apoio do **ChatGPT**, alternativa expressamente permitida no enunciado do curso.

Os programas usam entrada pelo terminal e trabalham os fundamentos de Python: strings, conversão de tipos, operadores aritméticos e condicionais.

## Exercícios

| Nº | Arquivo | Objetivo | Conceito central |
| --- | --- | --- | --- |
| 1 | [01_concatenando_dados.py](01_concatenando_dados.py) | Unir dois dados em uma única string. | `input()` e `+` entre strings. |
| 2 | [02_repetindo_textos.py](02_repetindo_textos.py) | Repetir um texto a quantidade de vezes informada. | `int()` e `*` entre string e inteiro. |
| 3 | [03_operacoes_matematicas.py](03_operacoes_matematicas.py) | Calcular uma operação entre dois números. | `float()`, `+`, `-`, `*`, `/` e condicionais. |
| 4 | [04_pares_e_impares.py](04_pares_e_impares.py) | Identificar um número par ou ímpar. | Resto da divisão com `%`. |
| 5 | [05_media_de_notas.py](05_media_de_notas.py) | Calcular a média de três notas. | Soma, divisão e formatação decimal. |
| 6 | [06_palindromos.py](06_palindromos.py) | Verificar se uma palavra é um palíndromo. | Comparação e inversão de strings com `[::-1]`. |

## Como executar

É necessário ter **Python 3** instalado. O projeto não utiliza pacotes externos.

1. Baixe e extraia os arquivos ou clone o repositório.
2. Abra o terminal na pasta que contém os arquivos `.py`.
3. Execute o exercício desejado e informe os dados solicitados.

No Windows, por exemplo:

```powershell
py 01_concatenando_dados.py
```

Se o comando `py` não estiver disponível, tente:

```powershell
python 01_concatenando_dados.py
```

No Linux ou macOS:

```bash
python3 01_concatenando_dados.py
```

Para executar outro exercício, substitua o nome do arquivo pelo correspondente na tabela.

## Exemplos e explicações

### 1. Concatenando dados

```text
Digite o primeiro dado: Python
Digite o segundo dado: 3
Resultado: Python3
```

`input()` retorna uma string. Por isso, o operador `+` une os dados, mesmo quando um deles contém dígitos. Não é acrescentado um separador automaticamente; um espaço digitado faz parte do resultado.

### 2. Repetindo textos

```text
Digite o texto: Oi!
Quantas vezes deseja repetir? 3
Resultado: Oi!Oi!Oi!
```

`texto * quantidade` repete o conteúdo da string. A quantidade deve ser um inteiro igual ou maior que zero. Zero produz uma string vazia; entradas inválidas ou negativas exibem uma mensagem explicativa.

### 3. Operações matemáticas simples

```text
Digite o primeiro número: 10
Digite o segundo número: 5
Escolha a operação (+, -, *, /): +
Resultado: 15.0
```

O programa realiza adição, subtração, multiplicação ou divisão, conforme a escolha do usuário. Aceita decimais com ponto ou vírgula, como `2.5` ou `2,5`. Divisão por zero e operadores desconhecidos exibem uma mensagem em vez de realizar o cálculo.

### 4. Números pares e ímpares

```text
Digite um número inteiro: 7
O número 7 é ímpar.
```

Se `numero % 2` for zero, o número é par; caso contrário, é ímpar. A regra também funciona para zero e inteiros negativos.

### 5. Média de notas

```text
Digite a primeira nota: 8
Digite a segunda nota: 9
Digite a terceira nota: 7
Média: 8.00
```

A média aritmética é calculada por `(primeira_nota + segunda_nota + terceira_nota) / 3`. As notas podem usar ponto ou vírgula decimal. O programa calcula apenas a média, sem definir aprovação ou reprovação, pois o enunciado não estabelece esse critério.

### 6. Palíndromos

```text
Digite uma palavra: Arara
"Arara" é um palíndromo.
```

Um palíndromo pode ser lido da mesma forma nos dois sentidos. `casefold()` normaliza maiúsculas e minúsculas, e `[::-1]` inverte a string. O programa ignora espaços no início e no fim; acentos, pontuação e espaços internos são preservados. Uma entrada vazia é recusada.

## Uso do ChatGPT

O ChatGPT auxiliou na elaboração dos códigos, na explicação dos conceitos e na conferência de exemplos de execução. Os arquivos incluem comentários nos pontos principais para facilitar o estudo.

Sugestões de prompts para reproduzir a atividade e compreender as soluções:

1. "Escreva um programa simples em Python que leia duas strings e as concatene. Explique por que input() retorna uma string."
2. "Leia um texto e uma quantidade inteira em Python e repita o texto. Explique o operador * e trate quantidades negativas."
3. "Leia dois números e uma operação entre +, -, * e /. Use condicionais e trate divisão por zero."
4. "Verifique se um inteiro é par ou ímpar usando %. Explique a regra com exemplos."
5. "Calcule a média aritmética de três notas e apresente o resultado com duas casas decimais."
6. "Verifique se uma palavra é um palíndromo usando [::-1] e uma comparação que ignore maiúsculas e minúsculas."

## Validação

Os seis programas foram executados em Python 3.12 com entradas de exemplo e casos como zero, números negativos, decimais com vírgula, divisão por zero, entrada não numérica e palavras com maiúsculas. Os resultados esperados foram conferidos.
