class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.is_alive():
            other.health -= self.attack_power
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            if not other.is_alive():
                print(f"{other.name} повержен!")
        else:
            print(f"{self.name} не может атаковать, он повержен.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = 0

        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                # Ход игрока
                self.player.attack(self.computer)
                print(f"{self.computer.name} имеет {self.computer.health} здоровья\n")
            else:
                # Ход компьютера
                self.computer.attack(self.player)
                print(f"{self.player.name} имеет {self.player.health} здоровья\n")

            # Чередуем ход
            turn += 1

        
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")

player = Hero("Игрок")
computer = Hero("Компьютер")

game = Game(player, computer)
game.start()