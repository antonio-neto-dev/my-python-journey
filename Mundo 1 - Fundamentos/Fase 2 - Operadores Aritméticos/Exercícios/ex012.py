preco_produto = float(input("Insira o preço do produto: R$"))
preco_descontado = preco_produto * 0.95
print(f"O novo preço com 5% de desconto é R${preco_descontado:,.2f}".replace(",", "x").replace(".", ",").replace("x", "."))