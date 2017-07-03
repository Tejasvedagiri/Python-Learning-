# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:35:51 2017

@author: Tejas
"""

#for Loop

Name = ('a', 'b', 'c')
i=0
for x in Name:
    print(Name[i])
    i=i+1
    
    
Email = ('me@gmail.com', 'you@yahoo.com', 'they@rocketmail.com')

for x in Email:
    if "gmail" in x:
        print(x)
