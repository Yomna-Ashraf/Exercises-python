# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:49:06 2021

@author: win10
"""
alph = "abcdefghijklmnopqrstuvwxyz"
def palindrome(str1):
    str2=""
    str3=""
    x=""
    for a in str1:
        if a.lower() in alph or type(a.lower())== int:
            x = a.lower()
            str3 = str3 + x
   
    print(str3) 
    for i in range(len(str1)-1,-1,-1):
        if str1[i].lower() in alph or type(str1[i].lower())==int :
            str2=str2+str1[i].lower()
    print(str2)
    
    if str2==str3:
        return True
    else:
        return False
        

print(palindrome("0 man, a plan, a canal. Panam0"))