#!/usr/bin/python3

import simerr

def Collatz(n):
  cnt=0
  if(simerr.simerror("Collatz",8)):
    return -1
  while(n>1):
    cnt=cnt+1
    if(n % 2):
      n=n*3+1
    else:
      n/=2
  return cnt

def retry():
  if(simerr.simerror("retry",5)):
    return -1
  ret=Collatz(500)
  while(ret<0):
    simerr.simfix("If at first you don't succeed, try again.")
    ret=Collatz(500)
  return ret

simerr.siminit("teamjoe.log")
print("Collatz conjecture at 500 satisfied after step {0}\n".format(retry()))
simerr.simdone()

