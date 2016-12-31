#include <stdio.h>

#include "simerr.h"

int Collatz(int n);
int retry();

int main()
{ siminit("teamjoe.log");
  printf("Collatz conjecture at 500 satisfied after step %d\n", retry());
  return simdone();
}

int Collatz(int n)
{ int cnt=0;

  if(simerror("Collatz",8))
    return -1;

  while(n>1)
  { cnt++;

    if(n % 2)
    { n=n*3+1;
    } else
    { n/=2;
    }
  }

  return cnt;
}

int retry()
{ int ret;

  if(simerror("retry",4))
    return -1;

  while((ret=Collatz(500))<0)
  { simfix("If at first you don't succeed, try again.");
  }

  return ret;
}


