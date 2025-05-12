vendas = []

while True:
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade vendida: "))

    vendas.append({
        "produto": produto,
        "quantidade": quantidade
    })

    cont = input("Deseja continuar? (s/n): ")
    if cont.lower() != 's':
        break

print("\n--- Vendas Realizadas ---")
for venda in vendas:
    print(f"{venda['produto']} - {venda['quantidade']} unidades")