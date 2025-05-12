vendas = []

while True:
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade vendida: "))
    preco_unitario = float(input("Preço unitário (R$): "))

    vendas.append({
        "produto": produto,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "total": quantidade * preco_unitario
    })

    if input("Deseja continuar? (s/n): ").lower() != "s":
        break

print("\n--- Vendas Realizadas ---")
for venda in vendas:
    print(
        f"{venda['produto']}: "
        f"{venda['quantidade']} × R${venda['preco_unitario']:.2f} "
        f"= R${venda['total']:.2f}"
    )

print(f"\nTotal geral: R${sum(v['total'] for v in vendas):.2f}")