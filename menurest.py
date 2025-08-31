# Mensagem de boas-vindas com nome completo e cardápio
print("-------- Bem-vindo à Loja de Marmitas do Gabriel Matos Pinho ---------")
print("------------------------------ Cardápio ------------------------------")
print("-------| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF)  |-------")
print("-------|    P    |        R$ 16,00     |       R$ 15,00       |-------")
print("-------|    M    |        R$ 18,00     |       R$ 17,00       |-------")
print("-------|    G    |        R$ 22,00     |       R$ 21,00       |-------")
print("----------------------------------------------------------------------")

# Acumulador de pedidos
total = 0

# while, break, continue
while True:
    # Input do sabor
    sabor = input("\nDigite o sabor (BA para Bife Acebolado ou FF para Filé de Frango): ").upper()
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente.")
        continue  # volta para o início do while

    # Input do tamanho
    tamanho = input("Digite o tamanho (P, M ou G): ").upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente.")
        continue  # volta para o início do while

    # Estrutura if/elif/else aninhada para definir preço
    if sabor == "BA":
        if tamanho == "P":
            preco = 16
        elif tamanho == "M":
            preco = 18
        else:
            preco = 22
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15
        elif tamanho == "M":
            preco = 17
        else:
            preco = 21

    print(f"Você escolheu {sabor} tamanho {tamanho}. Valor: R$ {preco}")
    total += preco  # somando no acumulador

    # Deseja pedir mais?
    mais = input("Deseja pedir mais alguma coisa? (S para sim / N para não): ").upper()
    if mais == "S":
        continue
    elif mais == "N":
        break
    else:
        print("Opção inválida. Encerrando pedido.")
        break

# Exibindo o total
print(f"\nValor total do pedido: R$ {total}")