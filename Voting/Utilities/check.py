#!/usr/bin/env python3

"""
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

"""First, read in the office stats.
STATS	Office	Precincts	VoteLimit	Votes	Voters
STATS   Lammersville Joint USD Governing Board Members  1       3       150    50
"""
stats=dict()
fstats=open("offices.stats","r")
for line in fstats:
    if line[-1]=="\n":
        line=line[:-1]
    line=line.split("\t")
    stats[line[1]]=line[1:]+[0,]
fstats.close()

fin=open("precincts.tsv", "r")

"""Read the header line containing the names of the offices."""
line=fin.readline()
if(line[-1]=='\n'):
    line=line[:-1]
offices=line.split("\t")

"""Read the office assignments for each precinct."""
for line in fin:
    if line[-1]=="\n":
        line=line[:-1]
    line=line.split("\t")
    for i in range(1,len(line)):
        if line[i]:
            """This precinct votes for this office, so tally the number of
               voters that we have available.
            """
            stats[offices[i]][5]+=int(line[0])
fin.close()

for office in offices[1:]:
    if float(stats[office][4])>stats[office][5]:
        print(stats[office])
