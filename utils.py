from functions import wraps
import time

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
