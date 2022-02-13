import random
from helpers import lists,racestats,stats

def get_rand_character():
    race = racestats.get_rand_race()

    race['Str'] += stats.get_str()
    race['Dex'] += stats.get_dex()
    race['Con'] += stats.get_con()
    race['Int'] += stats.get_int()
    race['Wis'] += stats.get_wis()
    race['Cha'] += stats.get_cha()


    ###############################################

    race['Class'] = random.choice(lists.class_list)

    race['Sex'] = random.choice(lists.sex_list)

    race['Level'] = random.choice(lists.level_list)

    race['Eye_Color'] = random.choice(lists.eyecolor_list)

    race['Hair_Color'] = random.choice(lists.haircolor_list)

    race['Personality'] = random.choice(lists.personality_list)

    race['Mood'] = random.choice(lists.mood_list)

    race['Quest'] = random.choice(lists.quest_list)

    return race