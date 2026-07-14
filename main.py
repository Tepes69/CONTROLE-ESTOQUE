print("Sistema de Controle de Estoque")
produto = input("Digite o nome do produto: ")
estoque = int(input("Digite a quantidade inicial: "))
movimento = input("Digite o tipo de movimentação (entrada/saida): ")
quantidade = int(input("Digite a quantidade movimentada: "))

if movimento == "entrada":
    estoque = estoque + quantidade
    print("Entrada registrada com sucesso.")
else:
    if movimento == "saida":
        estoque = estoque - quantidade
        print("Saída registrada com sucesso.")
    else:
        print("Tipo de movimentação inválido.")

print("Produto:", produto)
print("Estoque atual:", estoque)