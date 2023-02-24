import random

class Jedi:

    def __init__( self , name, power, block, health ):
        self.name = name
        self.power = power
        self.block = block
        self.health = health

    def show_stats( self ):
        print(f"Name: {self.name}\nHealth: {self.health}\n")

    def attack(self,damage):
        if(self.dodge()):
            self.health -= damage
        else:
            self.health -= damage
            return self

    #Healing 
    def healing_force(self):
        self.health += 10
        print(f'{self.name} took a healing potion! \nHealth is now {self.health}')
        return self

    #Dodge
    def dodge(self):
        chance = random.randint(0,6)
        if(chance < self.block):
            print("Anankin was hit")
            return False
        else:
            print("Anankin dodged the attack")
            return True

