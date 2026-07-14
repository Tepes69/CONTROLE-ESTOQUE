print("Sistema de Controle de Estoque")
produto = input("Digite o nome do produto: ")
estoque = int(input("Digite a quantidade inicial: "))
movimento = input("Digite o tipo de movimentação (entrada/saida): ").lower()
quantidade = int(input("Digite a quantidade movimentada: "))

if estoque < 0:
    print("Estoque inicial inválido.")
else:
    if quantidade <= 0:
        print("A quantidade movimentada deve ser maior que zero.")
    else:
        if movimento == "entrada":
            estoque = estoque + quantidade
            print("Entrada registrada com sucesso.")
        else:
            if movimento == "saida":
                if quantidade > estoque:
                    print("Saída não permitida. Estoque insuficiente.")
                else:
                    estoque = estoque - quantidade
                    print("Saída registrada com sucesso.")
            else:
                print("Tipo de movimentação inválido.")

print("Produto:", produto)
print("Estoque atual:", estoque)