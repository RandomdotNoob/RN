class Card:
    pass


class Minion(Card):
    def __init__(self, name, attack, max_hp, cost):
        self.name = name
        self.attack = attack
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.cost = cost

    def __str__(self):
        return " Minion {} with {} attack and {} health that costs {}".format(self.name,
         self.attack, self.max_hp, self.cost)

    def __repr__(self):
        return " Minion {} with {} attack and {} health that costs {}".format(self.name,
        self.attack, self.hp, self.cost)

    def hp_limit(self):
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0 and print(self.name + " is still Alive")

    def is_dead(self):
        return self.hp <= 0 and print(self.name + " is Dead")

    def die(self, other):
        if self.attack > other.hp:
            return other.is_dead() and print(other.name + " is dead") and delattr(other, other.name)
        elif other.attack > self.hp:
            return self.is_dead() and print(self.name + " is dead") and delattr(self, self.name)

    def heal(self):
        amount = self.hp + 1
        self.hp += amount
        return self.hp and print(self.name + " is now healed, Minion Health: " + str(self.hp))


ArchEnemy = Minion("Arch Enemy", 5, 3, 3)

print(ArchEnemy)
print(ArchEnemy.name)
print(ArchEnemy.attack)
print(ArchEnemy.hp)
print(ArchEnemy.cost)
print(ArchEnemy.is_dead())
print(ArchEnemy.is_alive())
print(ArchEnemy.heal())
