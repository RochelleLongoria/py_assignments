import random 
from classes import wizards
from classes import jedis

wizard = wizards.Wizard("Harry Potter", "Avada Cadava", random.randint(0,6), 100)
jedi = jedis.Jedi("Anakin Skywalker","The Dark Side", random.randint(0,6), 100)

# Wizard.attack(Anakin)
# Anakin.show_stats()


while wizard.health > 0 and jedi.health > 0:
    wizard.attack(random.randint(0,25))
    if wizard.health <= 0:
        break
    jedi.attack(random.randint(0,25))
    print(f"Harry Potter's Health Status: {wizard.health}")
    print("-------------------------------------------------")
    print(f"Anakin's Health Status: {jedi.health}")
if wizard.health <= 0:
    print("Anakin Wins")
else:
    print("Harry Potter Wins")