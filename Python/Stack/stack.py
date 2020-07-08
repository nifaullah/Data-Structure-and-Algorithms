# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:47:00 2020

@author: nifaullah
"""


class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    
    def get_stack(self):
        return self.items


s = Stack()

s.push("A")
s.push("B")
s.push("C")
print(s.get_stack())

s.pop()
print(s.get_stack())

s.pop()
s.pop()
print(s.is_empty())
print(s.get_stack())

s.push("C")
s.push("B")
s.push("A")
print(s.is_empty())
print(s.get_stack())

print(s.peek())

def reverse_string(stk, text):
    for i in range(len(text)):
        stk.push(text[i])
    out_str = ""
    while not stk.is_empty():
        out_str += stk.pop()
    return out_str
s = Stack()
print(reverse_string(s, "Heelo"))