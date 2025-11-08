from personagem import criar_heroinas
from personagem import criar_vilao
from utils import escolher_heroina, mostrar_status
import time

def batalha(heroina, vilao):
    print(f"\n🔥 A batalha entre {heroina.nome} e {vilao.nome} começou! 🔥\n")
    time.sleep(1)

    heroina.frase_inicial()
    vilao.provocar()

    usar_item = input(f"\nDeseja usar o item {heroina.item['nome']}? (s/n): ").lower()
    if usar_item == "s":
        heroina.usar_item()

    while heroina.esta_vivo() and vilao.esta_vivo():
        mostrar_status(heroina, vilao)
        print("1 - Atacar\n2 - Usar Habilidade Especial\n3 - Passar Turno")
        acao = input("Escolha sua ação: ")

        if acao == "1":
            heroina.atacar(vilao)
            heroina.frase_durante_batalha()
        elif acao == "2":
            heroina.usar_habilidade(vilao)
        elif acao == "3":
            print(f"{heroina.nome} observa os movimentos do inimigo...")
        else:
            print("Ação inválida!")

        time.sleep(1)

        if not vilao.esta_vivo():
            print(f"\n{vilao.nome} foi derrotado! {heroina.nome} venceu a batalha!\n")
            heroina.frase_vitoria()
            vilao.frase_derrota()
            break

        print(f"\n{vilao.nome} prepara seu ataque...")
        vilao.provocar()
        vilao.atacar(heroina)
        time.sleep(1)

        if not heroina.esta_vivo():
            print(f"\n☠️ {heroina.nome} foi derrotada por {vilao.nome}... ☠️\n")
            vilao.frase_vitoria()
            heroina.frase_derrota()
            break


def main():
    heroinas = criar_heroinas()
    heroina = escolher_heroina(heroinas)
    vilao = criar_vilao()

    print(f"\n {heroina.nome}, a guerreira de {heroina.idade} anos, enfrenta o antigo Lord Tunav ({vilao.idade} anos)...")
    time.sleep(2)
    batalha(heroina, vilao)


if __name__ == "__main__":
    main()

