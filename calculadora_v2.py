#Crie uma variável chamada saida e atribua a ela o valor ‘’
saida = 's'
#função adicao
def adicao(a, b):
    return a + b
#função subtração
def subtracao(a, b):
    return a - b
#função multiplicação
def multiplicacao(a, b):
    return a * b
#função divisão
def divisao(a, b):
    if b == 0:
        return 'não foi possível realizar a divisão por 0'
    return a / b

#função calculadora
def calculadora(num1, num2, operacao):
    resultado = None
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Inválido'

    return resultado

#Laço While
while saida.lower() != 'n':
    try:
        #Entrada dos numeros e operação
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo número: '))
        operação = input('Opração desejada(+, -, *, / ou nome): ')
        #Calculadora  e resultado
        resultado = calculadora(num1, num2, operação)
        print(f'Resultado da operação: {resultado}')
    except ValueError:
        print('Inválido! Digite núeros válidos')
    
    #pergunta se deseja sair
    saida = input('Deseja continuar? (S/N): ')

print('Programa encerrado')