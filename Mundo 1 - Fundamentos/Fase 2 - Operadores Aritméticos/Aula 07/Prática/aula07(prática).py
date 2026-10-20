num1 = int(input("Insira um número: "))
num2 = int(input("Insira mais um número: "))
soma = num1 + num2
multiplicacao = num1 * num2
divisao = num1 / num2
subtracao = num1 - num2
divisao_inteira = num1 // num2
potencia = num1 ** num2
raiz = num1**(1/2)
print(f"A soma é {soma}, a multiplicação é {multiplicacao}, a divisão é {divisao:.2} e a subtração é {subtracao}")
print(f"A divisão inteira é {divisao_inteira} e a exponenciação é {potencia}")
print(f"A raiz quadrada de {num1} é {raiz}")