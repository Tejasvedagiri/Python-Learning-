# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:06:52 2017

@author: Tejas
"""

#Functions

def Conv_currency(Money):
    Conv=Money*64.85
    Conv=float(Conv)
    return(Conv)
    
x = input("Enter USD")
x=float(x)
y = Conv_currency(x)
print(str(y)+"INR")