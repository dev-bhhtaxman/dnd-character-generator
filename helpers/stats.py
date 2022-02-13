import random

# get str stat
def get_str():
    randomroll = []
    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    return result


# get dex stat
def get_dex():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    return result


# get con stat
def get_con():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    return result

# get int stat
def get_int():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    return result

# get wis stat
def get_wis():
    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    return result

# get cha stat
def get_cha():

    randomroll = []

    for i in range(4):
        randomroll.append(random.randrange(1, 6))
    result = sum(randomroll)-min(randomroll)

    return result
