import random
randomroll=[]

for i in range(4):
  randomroll.append(random.randrange(1,6))
result=sum(randomroll)-min(randomroll)
class Intelligence:
  def __init__(self,intscore):
    self.intscore = intscore    
p4 = Intelligence(result)

print('INT',p4.intscore)