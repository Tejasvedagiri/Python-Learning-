# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:51:16 2017

@author: Tejas
"""

file=open("Test.txt","r")

type(file)

content=file.read()

print(content)

#Resetting File Pointer
file.seek(0)

content=file.readline()

print(content)


#i.rstrip("\n") removes charecter \n

file.close()