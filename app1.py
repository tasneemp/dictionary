# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:08:32 2019

@author: Tasneem
"""
import json 
from difflib import get_close_matches

data=json.load(open('data.json')) 
   

def getMeaning(key):
    
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    elif len(get_close_matches(key,data.keys(),3,0.8))>0:
        yn=input("Did you mean %s instead?(Enter y or n)" % get_close_matches(key,data.keys(),3,0.8)[0])
        if yn.lower() == 'y':
            return data[get_close_matches(key,data.keys(),3,0.8)[0]]
        elif yn.lower()=='n':
            return "Kindly input the right spelling"
        else:
            return "Invalid choice"
    else:
        return "Not a word. Please check"

while(True):
    word=input("enter a word or E to exit:")
    if word=='E':
        break
    #print("The meaning is:\n")
    list1=getMeaning(word.lower())
    if isinstance(list1,list):
        for m in list1:
            print(m)
    else:
        print(list1)