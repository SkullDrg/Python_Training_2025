def criar_vendedores_com_id(qtd):
    vendedores = {}
    for i in range(1, qtd + 1):
        while True:
            try:
                nome = input(f"Digite o nome do vendedor (ID {i}): ").strip()

                if not nome:
                    raise ValueError("O nome não pode ser vazio.")

                # Remove espaços e verifica se só há letras
                nome_sem_espacos = nome.replace(" ", "")
                if not nome_sem_espacos.isalpha():
                    raise ValueError("O nome deve conter apenas letras e espaços.")

                break  # Nome válido
            except ValueError as e:
                print(f"Entrada inválida: {e}. Tente novamente.")

        while True:
            try:
                venda = float(input(f"Digite o valor total de vendas de {nome}: "))
                vendedores[i] = (nome, venda)
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Tente novamente.")
    return vendedores

def mostrar_top_vendedores(vendedores, top=2):
    # Ordenar os itens do dicionário pelo valor da venda (índice 1 da tupla)
    top_vendas = sorted(vendedores.items(), key=lambda item: item[1][1], reverse=True)

    print(f"\nOs {top} vendedores que mais venderam foram:")
    for id_vendedor, (nome, venda) in top_vendas[:top]:
        print(f"ID {id_vendedor}: {nome} com R$ {venda:.2f}")

def main():
    vendedores = criar_vendedores_com_id(4)
    mostrar_top_vendedores(vendedores)

if __name__ == "__main__":
    main()
