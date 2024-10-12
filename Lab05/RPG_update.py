from abc import abstractmethod

class Item:
    def __int__(self, name, rarity, description, owner):
        self.name = name
        self.rarity = rarity
        self.description = description
        self.owner = owner
    @abstractmethod
    def pick_up(self):
        pass
    def equip(self):
        pass
class Weapon(Item):
    def __init__(self, name, damage, type, rarity = "common", equipped = False, description = "", owner = ""):
        super().__int__(name, rarity, description, owner)
        self.damage = damage
        self.type = type
        self.equipped = equipped

    def equip(self):
        pass

    def use(self):
       pass
class Single_handed(Weapon):
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
                if self.rarity == "legendary":
                    if self.rarity == "legendary":
                        print(f"{self.owner.upper()} IS USING A LEGENDARY ITEM!!!!!")
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
                    else:
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
            else:
                return None
        except:
            return None
    @classmethod
    def _slash(cls, name, type, rarity = "common", damage = 500, equipped = False, description = "", owner = "", string = "The special move slash is used"):
        obj = cls.__new__(cls)
        super(Weapon, obj).__init__()
        obj.name = name
        obj.damage = damage
        obj.type = type
        obj.rarity = rarity
        obj.equipped = equipped
        obj.description = description
        obj.owner = owner
        obj.string = string
        return obj
class Doubled_handed(Weapon):    
    @classmethod
    def _spin(cls, name, type, rarity = "common", damage = 300 , equipped = False, description = "", owner = ""):
        obj = cls.__new__(cls)
        super(Weapon, obj).__init__()
        obj.name = name
        obj.damage = damage
        obj.type = type
        obj.rarity = rarity
        obj.equipped = equipped
        obj.description = description
        obj.owner = owner
        return obj
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
                if self.rarity == "legendary":
                    if self.rarity == "legendary":
                        print(f"{self.owner.upper()} IS USING A LEGENDARY ITEM!!!!!")
                        print(cls.string)
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
                    else:
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
            else:
                return None
        except:
            return None
class Pike(Weapon):
    @classmethod
    def _thrust(cls, name, type, rarity = "common", damage = 750 , equipped = False, description = "", owner = ""):
        obj = cls.__new__(cls)
        super(Weapon, obj).__init__()
        obj.name = name
        obj.damage = damage
        obj.type = type
        obj.rarity = rarity
        obj.equipped = equipped
        obj.description = description
        obj.owner = owner
        return obj
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
                if self.rarity == "legendary":
                    if self.rarity == "legendary":
                        print(f"{self.owner.upper()} IS USING A LEGENDARY ITEM!!!!!")
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
                    else:
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
            else:
                return None
        except:
            return None
class Ranged_weapon(Weapon):
    @classmethod
    def _shoot(cls, name, type, rarity = "common", damage = 150 , equipped = False, description = "", owner = ""):
        obj = cls.__new__(cls)
        super(Weapon, obj).__init__()
        obj.name = name
        obj.damage = damage
        obj.type = type
        obj.rarity = rarity
        obj.equipped = equipped
        obj.description = description
        obj.owner = owner
        return obj
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
                if self.rarity == "legendary":
                    if self.rarity == "legendary":
                        print(f"{self.owner.upper()} IS USING A LEGENDARY ITEM!!!!!")
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
                    else:
                        print(f"{self.name} is used, dealing {self.damage * attack_modifier} damage")
            else:
                return None
        except:
            return None
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
        if self.rarity == "legendary":
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
            if self.type == "attack" and self.used == False:
                print(f'{self.owner} used {self.name}, and attack increase {self.value} for {self.time}s')
                self.used = True
            elif self.type == "defense" and self.used == False:
                print(f'{self.owner} used {self.name}, and defense increase {self.value} for {self.time}s')
                self.used = True
            elif self.type == "hp" and self.used == False:
                print(f'{self.owner} used {self.name}, and HP increase {self.value}')
                self.used = True
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
            if self.rarity == "legendary":
                print(f"{self.owner.upper()} IS USING A LEGENDARY ITEM!!!!!")
                print(f"{self.name} is equipped by {owner}")
            else:
                print(f"{self.name} is equipped by {owner}")
        except: 
            return None
class Inventory:
    def __init__(self, owner, inventory = [], names = [], descriptions = []):
        self.owner = owner
        self.inventory = inventory
        self.names = names
        self.descriptions = descriptions
    def add_item(self, item):
        self.item = item
        if self.item not in self.inventory:
            self.inventory.append(self.item)
            self.item.owner = self.owner
            self.item.ownership = self.owner
        if self.item.name not in self.names:
            self.names.append(self.item.name)
        if self.item.description not in self.descriptions:
            self.descriptions.append(self.item.description)
    def view(self, type = None, item = None):
        self.type = type
        self.item = item
        return_list = []
        count = 0
        for item in self.inventory:
                if self.item == self.names[count]:   
                    return_list.append(self.item + ":" + self.descriptions[count] + ".")
                    count += 1
                else:
                    count+= 1
        return_string = ""
        for item in return_list:
            return_string = return_string + item
        print(return_string)
        if type == "weapon":
            return_list = []
            for item in self.inventory:
                if isinstance(item, Weapon) == True:   
                    return_list.append(item)
            return_string = ""
            for item in return_list:
                return_string = return_string + item + ". "
            print(return_string)
        elif type == "shield":
            return_list = []
            for items in self.inventory:
                if isinstance(item, Sheild) == True:   
                    return_list.append(f'{self.names}: {self.descriptions[count]}')
            return_string = ""
            for item in return_list:
                return_string = return_string + item + ". "
            print(return_string)
        elif type == "potion":
            return_list = []
            for items in self.inventory:
                if isinstance(item, Potion) == True:   
                    return_list.append(f'{self.item.name}: {self.descriptions[count]}')
            return_string = ""
            for item in return_list:
                return_string = return_string + item + ". "
            print(return_string)
        elif type == "cloths":
            return_list = []
            for items in self.inventory:
                if isinstance(item, Cloths) == True:   
                    return_list.append(f'{self.item.name}: {self.descriptions[count]}')
            return_string = ""
            for item in return_list:
                return_string = return_string + item + ". "
            print(return_string)
        elif type == None and item == None:
            return_list = []
            count = 0
            for items in self.inventory:
                return_list.append(f'{self.names[count]}: {self.descriptions[count]}')
                count += 1
            return_string = ""
            for item in return_list:
                return_string = return_string + item + ". "
            print(return_string)
        
    def remove(self, item):
        self.item = item
        self.inventory.remove(self.item)
        self.item.owner = None
        self.names.remove(self.item.name)

        

broken_pot_lid = Sheild(name='wooden lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense = 5, broken = True)
long_bow = Single_handed._slash(name='Belthronding', description= "A long and very powerful sword", rarity='legendary', type = 'bow', owner = "CJ")
cjs_backpack = Inventory("cj")
cjs_backpack.add_item(long_bow)
cjs_backpack.add_item(broken_pot_lid)
long_bow.equip()
long_bow.use()
cjs_backpack.view(item = "wooden lid")