# Character class representing the player's character
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.inventory = []  # Player's inventory for storing items

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount}. Current health: {self.health}")

    def use_item(self, item):
        if item.effect == "heal":
            self.heal(20)  # Example healing effect
        elif item.effect == "boost_attack":
            self.attack_power += 5  # Example attack boost
        self.inventory.remove(item)
        print(f"{self.name} used {item.name}.")


# Item class for various game items
class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


# Enemy class representing the opponent
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")


# Initialize player, items, and enemy
player = Character("Hero", 100, 15)
healing_potion = Item("Healing Potion", "heal")
sword_upgrade = Item("Sword Upgrade", "boost_attack")
player.inventory.append(healing_potion)
player.inventory.append(sword_upgrade)

enemy = Enemy("Goblin", 50, 10)

# Game loop
while player.health > 0 and enemy.health > 0:
    # Player's turn
    action = input("Choose an action (attack/heal/use item): ")

    if action == "attack":
        player.attack(enemy)
    elif action == "heal":
        player.heal(20)
    elif action == "use item":
        if len(player.inventory) > 0:
            # Let player choose which item to use
            item_names = [item.name for item in player.inventory]
            print("Available items:", item_names)
            chosen_item = input("Which item would you like to use? ")
            for item in player.inventory:
                if item.name == chosen_item:
                    player.use_item(item)
                    break
        else:
            print("No items available.")

    # Enemy's turn if it's still alive
    if enemy.health > 0:
        enemy.attack(player)

    # Print current health status
    print(f"{player.name} Health: {player.health}, {enemy.name} Health: {enemy.health}")

# Determine the winner
if player.health > 0:
    print("You won!")
else:
    print("You lost!")
