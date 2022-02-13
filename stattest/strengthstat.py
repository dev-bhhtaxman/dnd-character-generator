 
import random
randomroll=[]

def str():
  for i in range(4):
    randomroll.append(random.randrange(1,6))
  result=sum(randomroll)-min(randomroll)

  class Strength:
    def __init__(self,strscore):
      self.strscore = strscore
  p1 = Strength(result)

  print('STR',p1.strscore)