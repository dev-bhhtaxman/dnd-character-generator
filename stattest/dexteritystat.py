
import random
randomroll=[]

for i in range(4):
  randomroll.append(random.randrange(1,6))
result=sum(randomroll)-min(randomroll)
class Dexterity:
  def __init__(self,dexscore):
    self.dexscore = dexscore    
p2 = Dexterity(result)

print('DEX',p2.dexscore)