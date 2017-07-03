# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:51:14 2017

@author: Tejas
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:51:16 2017

@author: Tejas
"""
#For append Open using a
file=open("Test.txt","w")

type(file)

file.write("hello\n")

l=["line1", "line2", "line3"]

for i in l:
    file.writelines(i + "\n")

file.close()

