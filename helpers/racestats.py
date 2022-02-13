import random

elf = {
    'Race':'Elf',
    "Str":0,
    "Dex":2,
    "Con":-2,
    "Int":0,
    "Wis":0,
    "Cha":0,
    "Weight":random.randint(95,135),
    "Height":round(random.uniform(4.5,5.5),2),
    "Age":random.randint(50,700),
}
gnome = {
    'Race':'Gnome',
    "Str":-2,
    "Dex":0,
    "Con":2,
    "Int":0,
    "Wis":0,
    "Cha":0,
    "Weight":random.randint(40,45),
    "Height":round(random.uniform(3.0,3.5),2),
    "Age":random.randint(40,400),
}
dwarf = {
    'Race':'Dwarf',
    "Str":0,
    "Dex":0,
    "Con":2,
    "Int":0,
    "Wis":0,
    "Cha":-2,
    "Weight":random.randint(110,200),
    "Height":round(random.uniform(4.0,4.5),2),
    "Age":random.randint(30,400),
}
halfling = {
    'Race':'Halfling',
    "Str":-2,
    "Dex":2,
    "Con":0,
    "Int":0,
    "Wis":0,
    "Cha":0,
    "Weight":random.randint(30,35),
    "Height":round(random.uniform(2.8,3.2),2),
    "Age":random.randint(20,150),
}
halforc = {
    'Race':'Halforc',
    "Str":2,
    "Dex":0,
    "Con":0,
    "Int":-2,
    "Wis":0,
    "Cha":-2,
    "Weight":random.randint(180,250),
    "Height":round(random.uniform(6.0,7.2),2),
    "Age":random.randint(14,75),
}
human = {
    'Race':'Human',
    "Str":0,
    "Dex":0,
    "Con":0,
    "Int":0,
    "Wis":0,
    "Cha":0,
    "Weight":random.randint(105,250),
    "Height":round(random.uniform(5.0,6.2),2),
    "Age":random.randint(16,75),
}
halfelf = {
    'Race':'Halfelf',
    "Str":0,
    "Dex":0,
    "Con":0,
    "Int":0,
    "Wis":0,
    "Cha":0,
    "Weight":random.randint(90,180),
    "Height":round(random.uniform(5.0,6.0),2),
    "Age":random.randint(20,180),
}

def get_rand_race():

    race = random.randint(0, 6)
    

    if race == 0:
        return halfelf
    elif race == 1:
        return human
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


