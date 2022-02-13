from flask import Flask
import random
from stattest import stats
from lists import racestats

# import stats.py

race = racestats.get_rand_race()


race['str'] += stats.get_str()
race['dex'] += stats.get_dex()
race['con'] += stats.get_con()
race['int'] += stats.get_int()
race['wis'] += stats.get_wis()
race['cha'] += stats.get_cha()

print(race)
###############################################
#from lists.classes import class_list
#print('Class:',random.choice(class_list))

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
#print(race/n,weight)