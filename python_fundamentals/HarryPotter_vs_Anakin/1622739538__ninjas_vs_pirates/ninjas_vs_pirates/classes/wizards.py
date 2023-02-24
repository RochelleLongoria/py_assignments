import random


class Wizard:

    def __init__( self , name, power, block, health ):
        self.name = name
        self.power = power
        self.block = block
        self.health = health
    
    #Overall Stats
    def show_stats( self ):
        print(f"Name: {self.name}\nHealth: {self.health}\n")
    
    #Attack
    def attack(self,damage):
        if(self.dodge()):
            self.health -= damage
        else:
            self.health -= damage
            return self

    #Healing 
    def healing_potion(self):
        self.health += 10
        print(f'{self.name} took a healing potion! \nHealth is now {self.health}')
        return self

    #Dodge
    def dodge(self):
        chance = random.randint(0,6)
        if(chance < self.block):
            print("Harry was attacked")
            return False
        else:
            print("Harry dodged the attack")
            return True
    