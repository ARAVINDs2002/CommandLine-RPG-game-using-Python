# Introduction:
The provided code is a simple Python-based game that simulates a turn-based combat system between a player (character) and an enemy. The player can perform actions such as attacking, healing, and using items during their turn, while the enemy will counterattack during its own turn. The game continues until either the player or the enemy runs out of health.
# Class Structure and Functionality:
The code defines three main classes:

Character
Item
Enemy
Each class represents a distinct component of the game system.

Character Class:
Attributes:

name: The player's name (e.g., "Hero").
health: The player's current health (initialized at 100).
attack_power: The attack power or damage the player deals to enemies (initialized at 15).
inventory: A list that stores the items the player can use during the game (initialized as an empty list).
Methods:

attack(target): The player attacks the target (either an enemy or another character). It reduces the target's health by the player's attack power.
heal(amount): Increases the player's health by a given amount.
use_item(item): Uses an item from the player's inventory. Depending on the item's effect (heal or boost_attack), it applies a corresponding effect and removes the item from the inventory.
Item Class:
Attributes:
name: The name of the item (e.g., "Healing Potion").
effect: The effect the item has on the player (e.g., "heal" or "boost_attack").
Enemy Class:
Attributes:

name: The enemy's name (e.g., "Goblin").
health: The enemy's current health (initialized at 50).
attack_power: The attack power or damage the enemy deals to the player (initialized at 10).
Methods:

attack(target): The enemy attacks the player or another target, reducing their health by the enemy's attack power.
# Game Flow and Logic:
The game flow consists of the following steps:

Player's Turn:

The player is prompted to choose an action: attack, heal, or use an item.
If the player chooses "attack", the player attacks the enemy, reducing the enemy's health by the player's attack power.
If the player chooses "heal", the player's health is increased by 20.
If the player chooses "use item", the player is presented with the items in their inventory and can choose one to use. Items can either heal the player or boost their attack power.
Enemy's Turn:

If the enemy is still alive after the player's turn, the enemy attacks the player, reducing the player's health by the enemy's attack power.
Health Status:

After each turn, the current health of both the player and the enemy is printed for the player to track.
Game End:

The game ends when either the player or the enemy's health reaches zero. If the player's health is greater than zero, the player wins; otherwise, the player loses.
