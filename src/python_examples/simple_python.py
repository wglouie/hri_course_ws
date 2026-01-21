#!/usr/bin/env python

import sys

if __name__=='__main__':

  #Print total arguments passed
  n = len(sys.argv)
  print("Total arguments passed: {}".format(n))

  #Print python  script name
  print("\nName of the python script: {}".format(sys.argv[0]))

  #Print all arguments passed
  print("\nArguements passed:")

  for i in range(1,n):
    print(sys.argv[i])

  #Print the sum of the numbers
  sum = 0

  for i in range(1,n):
    sum += int(sys.argv[i])
  
  print("\nResult: {}".format(sum))
