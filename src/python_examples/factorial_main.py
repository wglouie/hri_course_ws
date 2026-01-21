#!/usr/bin/env python

from Factorial import Factorial 

if __name__=='__main__':
  f = Factorial(5)
  g = Factorial()

  fact_val1 = f.compute()
  fact_val2 = g.compute()

  print("Factorial value 1: {}".format(fact_val1))
  print("Factorial value 2: {}".format(fact_val2))