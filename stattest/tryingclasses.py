
import random
randomroll=[]

for i in range(4):
  randomroll.append(random.randrange(1,6))
result=sum(randomroll)-min(randomroll)
#print(randomroll)
#print(result)

class Strength:
  def __init__(self,strscore):
    self.strscore = strscore
p1 = Strength(result)

class Dexterity:
  def __init__(self,dexscore):
    self.dexscore = dexscore    
p2 = Dexterity(result)

class Constitution:
  def __init__(self,conscore):
    self.conscore = conscore    
p3 = Constitution(result)

class Intelligence:
  def __init__(self,intscore):
    self.intscore = intscore    
p4 = Intelligence(result)

class Wisdom:
  def __init__(self,wisscore):
    self.wisscore = wisscore    
p5 = Wisdom(result)

class Charisma:
  def __init__(self,chascore):
    self.chascore = chascore    
p6 = Charisma(result)


print('STR:',p1.strscore)
print('DEX',p2.dexscore)
print('CON',p3.conscore)
print('INT',p4.intscore)
print('WIS',p5.wisscore)
print('CHA',p6.chascore)

