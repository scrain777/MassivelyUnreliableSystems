#!/usr/bin/env python3

"""
This program creates simulated votes taht have tallies similar to the real
tallies from the Alameda County, CA 2016 presidential election.

MIT License

Copyright (c) 2016 Steven P. Crain, SUNY Plattsburgh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import collections
import random

random.seed()

def f3(x):
    """Evaluate the estimate x**3+x**2+x."""
    return x*(x*x+x)+x

def f4(x):
    """Evaluate the estimate x**4+x**3+x**2+x."""
    return x*(x*(x*x+x)+x)+x

def d3(x):
    """Evaluate the estimate 3*x**2+2*x+1."""
    return (3*x+2)*x+1

def d4(x):
    """Evaluate the estimate 4*x**3+3*x**2+2*x+1."""
    return ((4*x+3)*x+2)*x+1

def newton(x,g,f,d):
    """Find x such that f(x) is within 1% of g."""
    fx=f(x)
    while(fx<.99*g or fx>1.01*g):
        x+=(g-fx)/d(x)
        fx=f(x)
    return x

def ratio(limit, votes, voters):
    limit=int(limit)
    goal=float(votes)/(limit*float(voters))
    if(limit==1):
        return goal
    guess=(goal+.25)**.5-.5
    if(limit==2):
        return guess
    if(limit==3):
        return newton(guess, goal, f3, d3) 
    if(limit==4):
        return newton(guess, goal, f4, d4) 
    raise IndexError("Unsupported vote limit {}".format(limit))

"""First, read in the office stats.
STATS	Office	Precincts	VoteLimit	Votes	Voters
STATS   Lammersville Joint USD Governing Board Members  1       3       150    50
Office	Candidate	Votes	Percent
President and Vice President    Write-in        10881   1.65
"""
stats=dict()
candidates=collections.defaultdict(list)
fstats=open("offices.tsv","r")
for line in fstats:
    if line[-1]=="\n":
        line=line[:-1]
    line=line.split("\t")
    if(line[0]=="STATS"):
        line[2]=int(line[2])
        line[3]=int(line[3])
        line[4]=int(line[4])
        line[5]=float(line[5])
        line.append(0)
        stats[line[1]]=line[1:]
    else:
        line[2]=int(line[2])
        line[3]=float(line[3])
        candidates[line[0]].append(line)
fstats.close()

fin=open("precincts.tsv", "r")

"""Read the header line containing the names of the offices."""
line=fin.readline()
if(line[-1]=='\n'):
    line=line[:-1]
offices=line.split("\t")

voters=0
precincts=[]
"""Read the office assignments for each precinct."""
for line in fin:
    if line[-1]=="\n":
        line=line[:-1]
    line=line.split("\t")
    line[0]=int(line[0])
    precincts.append(line)
    voters+=int(line[0])
    for i in range(1,len(line)):
        if line[i]:
            """This precinct votes for this office, so tally the number of
               voters that we have available.
            """
            stats[offices[i]][5]+=int(line[0])
fin.close()

"""Calculate the turnout factor for each office."""
for office in offices[1:]:
    s=stats[office]
    s.append(ratio(s[2], s[3], s[5]))

def makeVoter(factor=1):
    """Generate a random voter."""
    print("VOTER")
    count=0
    
    """First pick a random precint."""
    #i=random.randrange(int(voters*factor))
    i=0
    for p in precincts:
        if i<p[0]:
            """Voter is from this precinct."""
            break
        i-=p[0]
    
    """Now look through the offices."""
    for i in range(1,len(p)):
        if p[i]:
            office=offices[i]
            s=stats[office]
            """Copy the list so we can remove candidates once voted for."""
            cands=list(candidates[office])
            """Divide the number of votes by the choose-to-vote factor, so
               as to account for the number of voters who do not vote.
            """
            votes=s[3]/s[6]
            for v in range(s[2]):
                """For the number of times the voter is allowed to vote for this
                   office.
                """
                i=random.randrange(int(votes))
                for c in cands:
                    if i<c[2]:
                        """Voter votes for this candidate."""
                        print("VOTE\t{}\t{}".format(office,c[1]))
                        """If the voter can vote again, remove the number of
                           votes this candidate had recieved from the pool of
                           options and then make it even more likely the
                           user will not vote for another candidate.
                        """
                        votes=(votes-c[2])/s[6]
                        cands.remove(c)
                        count+=1
                        break
                    i-=c[2]
    
    """Now that the voter has had a chance on all the offices, see if the voter
       abandons or casts.
    """
    if random.random()<.85:
        print("CAST")
        return count
    return 0

count=0
#while count<1150000:
for i in range(580):
    count+=makeVoter(1)
