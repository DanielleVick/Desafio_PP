from personagem import Personagem
import random

class Heroi(Personagem):
    def __init__(self, nome, idade, ataque, defesa, vida, item):
        super().__init__(nome, idade, ataque, defesa, vida)
        self.item = item

    def usar_item(self):
        print(f"{self.nome} usou {self.item['nome']}!")
        efeito = self.item["efeito"]
        if "vida" in efeito:
            self.vida += efeito["vida"]
            print(f"✨ A vida de {self.nome} aumentou em {efeito['vida']} pontos!")
        if "ataque" in efeito:
            self.ataque += efeito["ataque"]
            print(f"⚡ O ataque de {self.nome} aumentou em {efeito['ataque']} pontos!")

    def usar_habilidade(self, inimigo):
        print(f"\n🔥 {self.nome} ativou sua HABILIDADE ESPECIAL! 🔥")
        if self.nome == "Ester":
            cura = random.randint(25, 45)
            self.vida += cura
            print(f"💫 Cura Divina! {self.nome} recuperou {cura} de vida!")
        elif self.nome == "Larissa":
            dano = self.ataque + random.randint(25, 40)
            inimigo.vida -= dano
            print(f"💥 Explosão de Energia! {self.nome} causou {dano} de dano em {inimigo.nome}!")
        elif self.nome == "Danielle":
            total_dano = 0
            print("🔥 Danielle lança 3 bolas de fogo!")
            for i in range(3):
                dano = self.ataque // 2 + random.randint(10, 25)
                total_dano += dano
                print(f"💣 Bola de fogo {i+1}! {inimigo.nome} levou {dano} de dano!")
            inimigo.vida -= total_dano
            print(f"🔥 Total de dano causado: {total_dano}!")

    def frase_inicial(self):
        frases = {
            "Ester": "A luz divina guiará minha espada!",
            "Larissa": "Hora de causar um pouquinho de destruição...",
            "Danielle": "Se prepara, Lord Tunav. Vai sentir a minha essência!",
        }
        print(f"\n{self.nome}: \"{frases[self.nome]}\"\n")

    def frase_durante_batalha(self):
        falas = [
            "Isso é tudo que você tem?",
            "Você vai precisar de mais que isso pra me parar!",
            "Agora começou a ficar interessante!"
        ]
        print(f"{self.nome}: \"{random.choice(falas)}\"")

    def frase_vitoria(self):
        print(f"\n{self.nome}: \"A justiça sempre vence!\"")

    def frase_derrota(self):
        print(f"\n{self.nome}: \"Não... ainda não acabou...\"")


def criar_heroinas():
    ester = Heroi(
        "Ester", idade=405, ataque=30, defesa=60, vida=120,
        item={"nome": "Escudo Sagrado", "efeito": {"defesa": 20, "vida": 10}}
    )
    larissa = Heroi(
        "Larissa", idade=212, ataque=60, defesa=30, vida=100,
        item={"nome": "Espada Rubra", "efeito": {"ataque": 25}}
    )
    danielle = Heroi(
        "Danielle", idade=502, ataque=80, defesa=50, vida=80,
        item={"nome": "Cristal Solar", "efeito": {"ataque": 15, "vida": 20}}
    )
    return [ester, larissa, danielle]
