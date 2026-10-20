salario = float(input("Informe seu salário: R$"))
salario_aumentado = salario * 1.15 + 0.001 # 0.001 é o truque para arredondar qualquer valor
print(f"Novo salário com 15% de aumento: R${salario_aumentado:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")) 
# todos esse replaces foram para tornar a visualização do salário no padrão brasileiro, com o "." separando os milhares e a "," separando os centavos