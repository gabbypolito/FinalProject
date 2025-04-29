
class Weapon:
    def __init__(self, name, attack, defense, speed):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def __str__(self):
        return self.name


class Character:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

    def set_health(self, new_health):
        self.health = max(0, new_health)


class Enemy:
    def __init__(self, health=3, attack=0, defense=0):      # No Defense as of now
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def set_health(self, new_health):
        self.health = max(0, new_health)