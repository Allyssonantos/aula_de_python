# Definindo o cardápio
cardapio = {
    "1": {"nome": "Água", "preco": 1},
    "2": {"nome": "Coxinha", "preco": 6.9},
    "3": {"nome": "Hambúrguer", "preco": 5.99},
    "4": {"nome": "Batata Frita", "preco": 10.99},
    "5": {"nome": "Refrigerante", "preco": 7.99},
    "6": {"nome": "Suco de Laranja", "preco": 1.9},
    "7": {"nome": "Sorvete", "preco": 10.99},
    "8": {"nome": "Café", "preco": 4.99}
}


# Função para exibir o cardápio
def exibir_cardapio():
    print("=== Cardápio ===")
    for codigo, item in cardapio.items():
        print(f"{codigo}: {item['nome']} - R${item['preco']:.2f}")


# Função principal
def main():
    exibir_cardapio()
    opcao = input("Digite o número do item desejado: ")
    if opcao not in cardapio:
        print("Opção inválida!")
        return

    quantidade = int(input("Digite a quantidade desejada: "))
    total = cardapio[opcao]["preco"] * quantidade
    print(f"Total a pagar: R${total:.2f}")


if __name__ == "__main__":
    main()
