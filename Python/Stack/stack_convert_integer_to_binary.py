# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:40:06 2020

@author: nifaullah
"""




from stack import Stack

def get_binary(num):
    s = Stack()
    
    while num > 0:
        s.push(num % 2)
        num = num // 2
        
    bin_val = ""
    while not s.is_empty():
        bin_val = f"{bin_val}{s.pop()}"
    
    return bin_val

print(get_binary(2))