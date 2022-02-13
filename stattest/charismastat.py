
import random
randomroll=[]

for i in range(4):
  randomroll.append(random.randrange(1,6))
result=sum(randomroll)-min(randomroll)
class Charisma:
  def __init__(self,chascore):
    self.chascore = chascore    
p6 = Charisma(result)

print('CHA',p6.chascore)