from vikingsClasses import Viking, Saxon, War
import random

# Lists of names for Vikings and Saxons with capital letters
viking_names = ["Albert", "Andres", "Archie", "Dani", "David", "Gerard", "German", "Graham", "Imanol", "Laura"]
saxon_names = ["Alfred", "Brian", "Charles", "Edward", "Fred", "George", "Harry", "Jack", "Ken", "Leo"]

# Create a War instance
war = War()

# Create 5 Vikings
for i in range(5):
    viking_name = random.choice(viking_names)
    viking = Viking(viking_name, 100, random.randint(50, 100))
    war.addViking(viking)

# Create 5 Saxons
for i in range(5):
    saxon_name = random.choice(saxon_names)
    saxon = Saxon(saxon_name, 100, random.randint(50, 100))
    war.addSaxon(saxon)

round_count = 0

while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    if war.vikingArmy and war.saxonArmy:
        viking = random.choice(war.vikingArmy)
        saxon = random.choice(war.saxonArmy)
        result = saxon.receiveDamage(viking.attack())
        print("="*50)
        print(f"Round {round_count}: {viking.name} the Viking attacks {saxon.name} the Saxon")
        print(result)
        if saxon.health <= 0:
            war.saxonArmy.remove(saxon)
        print("-"*30)

    if war.vikingArmy and war.saxonArmy:
        viking = random.choice(war.vikingArmy)
        saxon = random.choice(war.saxonArmy)
        result = viking.receiveDamage(saxon.attack())
        print(f"Round {round_count}: {saxon.name} the Saxon attacks {viking.name} the Viking")
        print(result)
        if viking.health <= 0:
            war.vikingArmy.remove(viking)
        print("-"*30)

    print(f"Round: {round_count} // Viking army: {len(war.vikingArmy)} warriors and Saxon army: {len(war.saxonArmy)} warriors")
    print(war.showStatus())
    round_count += 1

if len(war.vikingArmy) > 0:
    print("Surviving Vikings:")
    for viking in war.vikingArmy:
        print(f"- {viking.name} the Viking with {viking.health} health")
else:
    print("Surviving Saxons:")
    for saxon in war.saxonArmy:
        print(f"- {saxon.name} the Saxon with {saxon.health} health")
