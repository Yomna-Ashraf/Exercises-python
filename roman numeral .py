# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 08:35:23 2021

@author: win10
"""

numeral = [["I","IV","IX"],["X","XL","XC"],["C","CD","CM"]]

def roman_numeral(num):
    x=""
    roman=""
    num = str(num)
    ids=len(num)-1

    
    #--------------define the value-----------------#
    for  i in num:
       i = int(i)
       if i == 1:
           x=numeral[ids][0]
           roman = roman + x
       elif i > 1 and i <=3:
           x = i * numeral[ids][0]
           roman = roman + x
       elif i == 4:
           x = numeral[ids][1]
           roman = roman + x
          
       elif i == 5:
           x= numeral[ids][1][1]
           roman = roman + x
           

    return roman
print(roman_numeral(523))
print("DXXIII")