#!/usr/bin/env python

class Factorial:
  def __init__(self, n=3):
    self.n = n

  def compute(self):
    result = 1

    for i in range(0,self.n):
      result = self.__mult(result,self.n-i)

    return result
  
  def __mult(self,a,b):
    return a*b