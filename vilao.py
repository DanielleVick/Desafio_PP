from personagem import Personagem
import random

class Vilao(Personagem):
    def __init__(self, nome, idade, ataque, defesa, vida):
        super().__init__(nome, idade, ataque, defesa, vida)

    def provocar(self):
        falas = [
            "Vocês são apenas ecos do passado...",
            "Séculos se passaram, e ainda ninguém foi páreo para mim.",
            "Eu derrotei heróis mais poderosos do que vocês."
        ]
        print(f"{self.nome}: \"{random.choice(falas)}\"")

    def frase_derrota(self):
        print(f"\n{self.nome}: \"N-não... impossível... eu era eterno...\"")

    def frase_vitoria(self):
        print(f"\n{self.nome}: \"Mais uma alma que cai diante do poder de Lord Tunav!\"")


def criar_vilao():
    return Vilao("Lord Tunav", idade=1078, ataque=50, defesa=40, vida=150)
