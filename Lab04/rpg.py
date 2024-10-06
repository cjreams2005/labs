
class Item:
    def __int__(self, name, rarity, description, owner):
        self.name = name
        self.rarity = rarity
        self.description = description
        self.owner = owner
class Weapon(Item):
    def __init__(self, name, damage, type, rarity = "common", equipped = False, description = "", owner = ""):
        super().__int__(name, rarity, description, owner)
        self.damage = damage
        self.type = type
        self.equipped = equipped
    def pick_up(self, ownership):
        weapon_name = self.name
        self.ownership = ownership
        print(f"{weapon_name} is now owned by {ownership}")

    def equip(self):
        try: 
            self.equipped = True
            owner = self.ownership
            print(f"{self.name} is equipped by {owner}")
        except: 
            return None

    def use(self):
        if self.rarity == "legendary":
            attack_modifier = 1.15
        else:
            attack_modifier = 1
        try: 
            if self.equipped == True and self.ownership != False:
                print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
            else:
                return None
        except:
            return None
    def throw_away(self):
        self.ownership = False
class Potion(Item):
    def __init__(self, name, value, time, type, rarity = "common", used = False, description = "", owner = ""):
        super().__int__(name, rarity, description, owner)
        self.value = value
        self.time = time
        self.type = type
        self.used = used
    @classmethod
    def from_ability(cls, name, type, value = 50, time = 30, rarity = "common", used = False, description = "", owner = ""):
        obj = cls.__new__(cls)
        super(Potion, obj).__init__()
        obj.value = value
        obj.name = name
        obj.type = type
        obj.time = time
        obj.rarity = rarity
        obj.used = used
        obj.description = description
        obj.owner = owner
        return obj
    def pick_up(self, ownership):
        weapon_name = self.name
        self.owner = ownership
        print(f"{weapon_name} is now owned by {ownership}")
    def use(self):
        if self.type == "attack" and self.used == False:
            print(f'{self.owner} used {self.name}, and attack increase {self.value} for {self.time}s')
            self.used = True
        elif self.type == "defense" and self.used == False:
            print(f'{self.owner} used {self.name}, and defense increase {self.value} for {self.time}s')
            self.used = True
        elif self.type == "hp" and self.used == False:
            print(f'{self.owner} used {self.name}, and HP increase {self.value}')
            self.used = True
        else:
            return None
    def throw_away(self):
        self.ownership = False
class Sheild(Item):
        def __init__(self, name, defense, rarity = "common", equipped = False, description = "", owner = "", broken = False):
            super().__int__(name, rarity, description, owner)
            self.defense = defense
            self.equipped = equipped
            self.broken = broken

        def pick_up(self, ownership):
            weapon_name = self.name
            self.ownership = ownership
            print(f"{weapon_name} is now owned by {ownership}")

        def equip(self):
            try: 
                self.equipped = True
                owner = self.ownership
                print(f"{self.name} is equipped by {owner}")
            except: 
                return None
        
        def use(self):
            if self.rarity == "legendary":
                defensive_modifier = 1.10
            else:
                defensive_modifier = 1
            if self.broken == True:
                broken_modifier = 0.5
            else:
                broken_modifier = 1
            try:
                if self.equipped == True and self.ownership != False:
                    print(f"{self.name} is used, blocking {self.defense * defensive_modifier * broken_modifier} damage")
                else:
                    return None
            except:
                return None
        def throw_away(self):
            self.ownership = False
class Cloths(Item):
    def __init__(self, name, type, rarity = "common", equipped = False, description = "", owner = ""):
        super().__int__(name, rarity, description, owner)
        self.type = type
        self.equipped = equipped
    def pick_up(self, ownership):
        weapon_name = self.name
        self.ownership = ownership
        print(f"{weapon_name} is now owned by {ownership}")

    def equip(self):
        try: 
            self.equipped = True
            owner = self.ownership
            print(f"{self.name} is equipped by {owner}")
        except: 
            return None
    def throw_away(self):
            self.ownership = False


#sheildy = Weapon(name='rusty', rarity='common', damage = 5, type = "bow")
potiony = Potion(name="bop", value= 50, description = "adds attack", owner = "cj", time = 30, type = "attack")
#weapony = Weapon(name= "long bow", rarity = "legandary", damage = 400, type = "bow")
#sheildy.pick_up("Cj")
#print(isinstance(sheildy, Item))
armor = Cloths(name = "Iron Armor", rarity = "cloths", type = "armor")
armor.pick_up("CJ")
armor.equip()
long_bow = Weapon(name='Belthronding', rarity='legendary', damage= 5000, type = 'bow')
long_bow.pick_up('Beleg') 
long_bow.equip()
long_bow.use()
broken_pot_lid = Sheild(name='wooden lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for ashield', defense = 5, broken = True)
broken_pot_lid.pick_up('Beleg')
broken_pot_lid.equip()
broken_pot_lid.use()
broken_pot_lid.throw_away()
broken_pot_lid.use()
attack_potion = Potion(value = 50, time = 30, name='atk potion temp', type='attack')
attack_potion.pick_up("cj")
attack_potion.use()
attack_potion.use()
print(isinstance(long_bow, Item))
print(isinstance(broken_pot_lid, Sheild))
print(isinstance(attack_potion, Weapon))