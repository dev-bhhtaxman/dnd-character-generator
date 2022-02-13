import random
randomroll=[]

for i in range(4):
  randomroll.append(random.randrange(1,6))
result=sum(randomroll)-min(randomroll)
class Constitution:
  def __init__(self,conscore):
    self.conscore = conscore    
p3 = Constitution(result)

print('CON',p3.conscore)