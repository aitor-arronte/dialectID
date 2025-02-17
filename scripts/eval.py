#!/usr/bin/python -tt

from __future__ import division
import sys  
reload(sys)
import codecs
import collections
import re
from subprocess import call
import itertools


sys.setdefaultencoding('utf8')

langList=['EGY', 'GLF', 'LAV', 'MSA','NOR']
_len=len(langList)

if len(sys.argv) != 3   :
    print 'usage: eval.py  test.feats prediction file'
    sys.exit (1)
    
testFeatFile = sys.argv[1]
predFile = sys.argv[2]

truth =[] 
with open(testFeatFile) as f:
    content = f.readlines()
    for line in content: truth.append (line.split ( )[1]);
f.close()

claasifier =[]
with open(predFile) as f:
    content = f.readlines()
    for line in content: claasifier.append (line.split ( )[1]);
f.close()

results=[[0 for x in xrange(_len)] for y in xrange(_len)]
for _t, _g in zip(truth, claasifier):
    _truthIdx=int(_t)-1
    _claasifierIdx=int(_g)-1
    results[_truthIdx][_claasifierIdx]+=1


total_accuracy = [0 for x in xrange(_len)]
total_i = total_accuracy [:]
total_j = total_accuracy [:]


for i in range(_len):
    for j in range(_len):
        if (i == j ): total_accuracy[i]=results[i][j]
        total_i[i]+=results[i][j]
        total_j[i]+=results[j][i]



recall=[]
prec=[]
for _acc, _pre, _rec in itertools.izip(total_accuracy, total_i, total_j):
    recall.append('%0.2f' % (_acc/_pre*100))
    prec.append('%0.2f' % (_acc/_rec*100))

print 'Overal Accuracy  : %0.2f' % (sum(total_accuracy)/sum(total_i)*100)+'%'
print 'Average Precision: %0.2f' % (sum(float(item) for item in prec)/_len)+'%'
print 'Avergae Recall   : %0.2f' % (sum(float(item) for item in recall)/_len)+'%'




print "\t\t  ", "Predicted dialects", "\t\t\tTotalTruth Precision:"
for i in range(_len):
    print langList[i], "\t\t",
    for j in range(_len):
        print results[i][j], "\t",
    print '||',total_i[i], "\t",
    print '%s' % (prec[i])+'%'
    


print "\ntotalClass:\t",
for item in total_j:
    print item,"\t",
print ''

print "Recall:\t\t",
for item in recall:
    print '%s' % (item)+'%',
print '\n\n'
