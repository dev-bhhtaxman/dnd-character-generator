
#race_list = ['Gnome','Halfing','Human','Elf','Dwarf','Half-elf','Half-orc',]
import random

elf = {
    'race':'elf',
    "str":0,
    "dex":2,
    "con":-2,
    "int":0,
    "wis":0,
    "cha":0,
    "weight":random.randint(95,135),
    "height":random.uniform(4.5,5.5),
    "age":random.randint(50,700),
}
gnome = {
    'race':'gnome',
    "str":-2,
    "dex":0,
    "con":2,
    "int":0,
    "wis":0,
    "cha":0,
    "weight":random.randint(40,45),
    "height":random.uniform(3.0,3.5),
    "age":random.randint(40,400),
}
dwarf = {
    'race':'dwarf',
    "str":0,
    "dex":0,
    "con":2,
    "int":0,
    "wis":0,
    "cha":-2,
    "weight":random.randint(110,200),
    "height":random.uniform(4.0,4.5),
    "age":random.randint(30,400),
}
halfling = {
    'race':'halfling',
    "str":-2,
    "dex":2,
    "con":0,
    "int":0,
    "wis":0,
    "cha":0,
    "weight":random.randint(30,35),
    "height":random.uniform(2.8,3.2),
    "age":random.randint(20,150),
}
halforc = {
    'race':'halforc',
    "str":2,
    "dex":0,
    "con":0,
    "int":-2,
    "wis":0,
    "cha":-2,
    "weight":random.randint(180,250),
    "height":random.uniform(6.0,7.2),
    "age":random.randint(14,75),
}
human = {
    'race':'human',
    "str":0,
    "dex":0,
    "con":0,
    "int":0,
    "wis":0,
    "cha":0,
    "weight":random.randint(105,250),
    "height":random.uniform(5.0,6.2),
    "age":random.randint(16,75),
}
halfelf = {
    'race':'halfelf',
    "str":0,
    "dex":0,
    "con":0,
    "int":0,
    "wis":0,
    "cha":0,
    "weight":random.randint(90,180),
    "height":random.uniform(5.0,6.0),
    "age":random.randint(20,180),
}

def get_rand_race():

    race = random.randint(0, 6)
    

    if race == 0:
        return halfelf,
    elif race == 1:
        return human,
    elif race == 2:
        return halforc
    elif race == 3:
        return halfling
    elif race == 4:
        return dwarf
    elif race == 5:
        return gnome
    elif race == 6:
        return elf

