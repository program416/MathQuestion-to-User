from functools import wraps
import time
import random

class rank:
  def __init__(self,name,minELO,maxELO):
    self.name = name
    self.minELO = minELO
    self.maxELO = maxELO
  def __lt__(self,other):
    return self.minELQ > other.minELQ
  def __le__(self,other):
    return self.minELQ >= other.minELQ
  def __eq__(self,other):
    return self.minELQ == other.minELQ
  def __repr__(self):
    return f"rank {self.name}"

bronze = rank("Bronze",0,199)
silver = rank("Silver",200,399)
gold = rank("Gold",400,599)
def a_quiz_logic():
  a = random.randint(10,99)
  b = random.randint(10,99)
  answer = a + b
  return [f'{a} + {b} = ?',answer]

def a_quiz_logic_2():
  a = random.randint(1,10)
  b = random.randint(1,10)
  answer = a * b
  return [f'{a} * {b} = ?',answer]

def a_quiz_logic_3():
  a = random.randint(5,16)
  b = random.randint(1,9)
  answer = a * b
  return [f'{a} * {b} = ?',answer]

a_logics = [
  a_quiz_logic,
  a_quiz_logic_2,
  a_quiz_logic_3
]
