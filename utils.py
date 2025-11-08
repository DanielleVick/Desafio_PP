def escolher_heroina(heroinas):
    print("Escolha sua heroína:")
    for i, h in enumerate(heroinas, start=1):
        print(f"{i} - {h.nome} ({h.idade} anos) → Ataque: {h.ataque}, Defesa: {h.defesa}, Vida: {h.vida}, Item: {h.item['nome']}")

    while True:
        try:
            escolha = int(input("Digite o número da heroína escolhida: "))
            if 1 <= escolha <= len(heroinas):
                return heroinas[escolha - 1]
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Digite um número válido!")


def mostrar_status(heroina, vilao):
    print("\n--- STATUS ---")
    print(f"{heroina.nome} → Vida: {heroina.vida}")
    print(f"{vilao.nome} → Vida: {vilao.vida}")
    print("--------------\n")