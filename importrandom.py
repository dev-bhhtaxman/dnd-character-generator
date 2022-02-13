
import random
stats = ['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma']
randomroll=[]
for Abilitystat in stats:
    for i in range(4):
        randomroll.append(random.randrange(1,6))
        result=sum(randomroll)-min(randomroll)
    print(Abilitystat,result)
    randomroll.clear()

# above is for the random roll and print for stats

#from lists.race import race_list
#print('Race:',random.choice(race_list))
race = ['human', 'elf', 'halfelf', 'halfling','halforc','dwarf','gnome']
print('Race:', random.choice(race))

from lists.classes import class_list
print('Class:',random.choice(class_list))

from lists.sex import sex_list
print('Sex:',random.choice(sex_list))

from lists.level import level_list
print('Level:',random.choice(level_list))

from lists.eyecolor import eyecolor_list
print('Eye Color:',random.choice(eyecolor_list))

from lists.haircolor import haircolor_list
print('Hair Color:',random.choice(haircolor_list))

from lists.personality import personality_list
print('Personality:',random.choice(personality_list))

from lists.mood import mood_list
print('Mood:',random.choice(mood_list))

from lists.quest import quest_list
print('Quest?',random.choice(quest_list))

#above is for random character

# python App013022.py  (to run)