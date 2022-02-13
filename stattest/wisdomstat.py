import random
randomroll=[]

for i in range(4):
  randomroll.append(random.randrange(1,6))
result=sum(randomroll)-min(randomroll)
class Wisdom:
  def __init__(self,wisscore):
    self.wisscore = wisscore    
p5 = Wisdom(result)

print('WIS',p5.wisscore)