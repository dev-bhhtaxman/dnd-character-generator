import random

# get str stat


def get_str():
    randomroll = []
    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    class Strength:
        def __init__(self, strscore):
            self.strscore = strscore
    p1 = Strength(result)

    return p1.strscore


# get dex stat
def get_dex():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    class Dexterity:
        def __init__(self, dexscore):
            self.dexscore = dexscore
    p2 = Dexterity(result)

    return p2.dexscore


# get con stat
def get_con():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    class Constitution:
        def __init__(self, conscore):
            self.conscore = conscore

    p3 = Constitution(result)

    return p3.conscore

# get int stat


def get_int():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    class Intelligence:
        def __init__(self, intscore):
            self.intscore = intscore

    p4 = Intelligence(result)

    return p4.intscore

# get wis stat


def get_wis():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    class Wisdom:

        def __init__(self, wisscore):
            self.wisscore = wisscore
    p5 = Wisdom(result)

    return p5.wisscore

# get cha stat


def get_cha():


    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)


    class Charisma:
        def __init__(self, chascore):
            self.chascore = chascore


    p6 = Charisma(result)

    return p6.chascore
