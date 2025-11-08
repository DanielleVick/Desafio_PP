class Personagem:
    """
    Classe base para os personagens do jogo.
    Cada personagem tem nome, idade, vida, item e falas específicas.
    """

    def __init__(self, nome, idade, vida, item):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.item = item

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} aumentou para {self.vida}!')

    def downgrade_vida(self, dano=15):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > dano:
            self.vida -= dano
        else:
            self.vida = 0
        print(f'{self.nome} levou dano! Vida atual: {self.vida}')

    def habilidade_especial(self):
        """
        Executa a habilidade especial de cada personagem.
        """
        if self.nome.lower() == "danielle":
            print("🔥 Danielle lança uma bola de fogo poderosa!")
        elif self.nome.lower() == "ester":
            print("✨ Ester invoca uma Cura Divina que restaura suas energias!")
            self.upgrade_vida(20)
        elif self.nome.lower() == "larissa":
            print("💥 Larissa libera uma Explosão de Energia devastadora!")
        else:
            print(f"{self.nome} ainda não descobriu sua habilidade especial...")

    def dialogo_inicial(self):
        """
        Fala antes da luta começar.
        """
        if self.nome.lower() == "danielle":
            print("🔥 Danielle: Vamos mostrar o que é força de verdade!")
        elif self.nome.lower() == "ester":
            print("✨ Ester: Que a luz guie nossa batalha!")
        elif self.nome.lower() == "larissa":
            print("💥 Larissa: Espero que estejam prontos, porque eu tô!")
        else:
            print(f"{self.nome}: Que comecem os desafios!")

    def dialogo_durante_luta(self):
        """
        Fala durante a luta.
        """
        if self.nome.lower() == "danielle":
            print("🔥 Danielle: Sinta o calor da minha chama!")
        elif self.nome.lower() == "ester":
            print("✨ Ester: Tá sentindo a energia?")
        elif self.nome.lower() == "larissa":
            print("💥 Larissa: Não vai ser fácil me derrotar!")
        else:
            print(f"{self.nome}: Eu ainda posso vencer isso!")

    def dialogo_final(self, venceu=True):
        """
        Fala depois da luta.
        """
        if venceu:
            if self.nome.lower() == "danielle":
                print("🔥 Danielle: Vitória ardente como o fogo!")
            elif self.nome.lower() == "ester":
                print("✨ Ester: A luz sempre vence as trevas!")
            elif self.nome.lower() == "larissa":
                print("💥 Larissa: Eu sabia que ninguém me parava!")
            else:
                print(f"{self.nome}: Eu consegui!")
        else:
            if self.nome.lower() == "danielle":
                print("🔥 Danielle: Essa chama ainda não se apagou...")
            elif self.nome.lower() == "ester":
                print("✨ Ester: Mesmo na derrota, a minha energia permanece.")
            elif self.nome.lower() == "larissa":
                print("💥 Larissa: Isso não vai ficar assim!")
            else:
                print(f"{self.nome}: Preciso treinar mais...")

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Item: {self.item}'

