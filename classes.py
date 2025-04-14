class Weapons:
    def __init__(self, damage=0, range=0, crit=0):
        self.damage = damage
        self.range = range
        self.crit = crit

    def do_damage(self, other):
        other.health -= self.damage


class Character:
    def __init__(self):
        self.hearts = 10

    def take_damage(self, other):
        self.hearts -= other.damage


class Enemies:
    def __init__(self, health=3, damage=0, defense=0):
        self.health = health
        self.damage = damage


#Character List:
Bull = Enemies(health=3, damage=3)
Knight = Enemies(health=3, damage=20)
