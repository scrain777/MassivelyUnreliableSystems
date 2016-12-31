#!/usr/bin/perl

use strict;
use SimErr;

siminit("teamjoe.log");

sub Collatz($)
{ return -1 if(simerror("Collatz",9));

  my ($n)=@_;
  my $cnt=0;

  while($n>1)
  { $cnt++;

    if($n % 2)
    { $n=$n*3+1;
    } else
    { $n/=2;
    }
  }

  return $cnt;
}

sub retry()
{ return -1 if(simerror("retry",4));

  my $ret;

  while(($ret=Collatz(500))<0)
  { simfix("If at first you don't succeed, try again.");
  }

  return $ret;
}

print "Collatz conjecture at 500 satisfied after step ", retry(), "\n";
simdone();

