# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:20:32 2020

@author: nifaullah

Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))

 """

from stack import stack

def is_match(cand,text):
    if cand == "{" and text == "}":
        return True
    elif cand == "(" and text == ")":
        return True
    elif cand == "[" and text == "]":
        return True
    else:
        return False

def is_paren_balanced(text):
    index = 0
    is_balanced = True
    s = Stack()
    
    while index < len(text):
        if text[index] in "{([":
            s.push(text[index])
        else:
            if s.is_empty():
                return False
            else:
                cand = s.pop()
                if not is_match(cand, text[index]):
                    return False
        index += 1
    return s.is_empty();

print(is_paren_balanced("(((({}))))"))

print(is_paren_balanced("[][]]]"))
print(is_paren_balanced("[][]"))
print(is_paren_balanced("[[[[["))