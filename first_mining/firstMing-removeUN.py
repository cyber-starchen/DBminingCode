# -*- coding: utf-8 -*-


import pyfpgrowth
import csv
import math


file='first_mining_sample.csv'
output=open(file+'_outputWithNoUN.txt',"w")
counter=0
# per=0.5

with open(file) as f:
    f_csv=csv.reader(f)
    resultSet=[]
    header=[]
    for row in f_csv:
        result=[]
        if f_csv.line_num==1:
            header=row
            continue
        else:
            counter=counter+1
            for i in range(len(row)):
                if ('-1'!=row[i] and  not('Unknown'.lower() in row[i].lower())):
                    result.append(row[i])
                # if('-1' == row[i]):
                #     result.append(header[i]+'=-1')
                    
                # elif('Unknown'.lower() in row[i].lower()):
                    
                #     result.append(header[i]+row[i])
                # else:
                #     result.append(row[i])
        resultSet.append(result)
                
per=float(input("enter %\n"))

pattern=pyfpgrowth.find_frequent_patterns(resultSet,math.ceil(counter*per))

p1= sorted(pattern.items(),key = lambda x:x[1],reverse = True)
output.write("Mining patterns from "+file+"\n")
output.write("Frequent patterns: \n")
for x in range(0,len(p1)):
    output.write(str(p1[x])+"\n")

f.close
output.close




    
    
    
    
    
    
    