# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 00:06:39 2020

@author: nifaullah
"""


class Node():
    
    def __init__(self, info):
        self.info = info
        self.link = None
        
class SingleLinkedList():
    
    def __init__(self):
        self.start = None
        
    def print_list(self):
        p = self.start
        while p:
            print(p.info)
            p = p.link
    
    def append(self, info):
        node = Node(info)
        if self.start is None:
            self.start = node
        else:
            p = self.start
            while p.link is not None:
                p = p.link;
            p.link = node
            
    def prepend(self, info):
        node = Node(info)
        node.link = self.start
        self.start = node
    
    def insert_after(self, prev_node, info):
        if not prev_node:
            print("Invalid Node")
        node = Node(info)
        node.link = prev_node.link
        prev_node.link = node
    
    # Assumption - No duplicate
    def delete(self, key):
        is_key_avlbl = False
        if self.start.info == key:
            self.start = self.start.link
            return
        else:
            p = self.start
            while p.link:
                if p.link.info == key:
                    p.link = p.link.link
                    is_key_avlbl = True
                    return
                p = p.link
        if not is_key_avlbl:
            print("key not in list")
    
    def delete_at_position(self, pos):
        is_pos_avlbl = False
        if pos == 0:
            self.start = self.start.link
            return
        else:
            index = 1
            p = self.start
            while p.link:
                if index == pos:
                    p.link = p.link.link
                    return
                p = p.link
                index += 1
        if not is_key_avlbl:
            print("position not in list")
    
    def len_iterative(self):
        count = 0
        p = self.start
        
        while p:
            p = p.link
            count += 1
        return count
    
    def len_recursive(self, node):
        if not node:
            return 0
        return 1 + self.len_recursive(node.link)
    
    def swap_nodes(self, info_1, info_2):
        
        if info_1 == info_2:
            return
        
        prev_1 = None
        curr_1 = self.start
        while curr_1 and curr_1.info != info_1:
            prev_1 = curr_1
            curr_1 = curr_1.link
        
        prev_2 = None
        curr_2 = self.start
        while curr_2 and curr_2.info != info_2:
            prev_2 = curr_2
            curr_2 = curr_2.link
        
        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.link = curr_2
        else:
            self.start = curr_2
            
        if prev_2:
            prev_2.link = curr_1
        else:
            self.start = curr_1
        
        curr_1.link, curr_2.link = curr_2.link, curr_1.link
        
    def reverse_iterative(self):
        r = self.start
        p = r.link
        while p:
            q = p.link
            p.link = r
            r = p
            p = q
            
        self.start.link = None
        self.start = r
    
    def reverse_recursive(self):
        def _rev__rec(p,r):
            if not p:
                return r
            
            q = p.link
            p.link = r
            r = p
            p = q
            return _rev__rec(p,r)
        
        self.start = _rev__rec(p = self.start, r = None)
            
    def merge_sorted(self, lst1):
        p = self.start
        q = lst1.start
        
        if not p:
            self.start = q
            return
        
        if not q:
            return
            
        if p.info <= q.info:
            s = p
            p = p.link
        else:
            self.start = q
            s = q
            q = q.link
        
        while p and q:
            if p.info <= q.info:
                #print(p.info)
                s.link = p
                p = p.link
            else:
                #print(q.info)
                s.link = q
                q = q.link
            s = s.link
            
        if p:
            s.link = p
        elif q:
            s.link = q
      
    def remove_duplicates(self):
        p = self.start
        q = None
        val = {}
        
        while p:
            if p.info not in val:
                val[p.info] = True
                q = p
                p = p.link
            else:
                p = p.link
                q.link = p
    
    def  get_nth_element_from_last(self, n):
        if not self.start:
            return
        len = self.len_iterative()
        p = self.start
        
        while p:
            if len == n:
                return p.info
            len -= 1
            p = p.link
            
    def  get_nth_element_from_last2(self, n):
        if not self.start:
            return
        
        p = q = self.start
        count = 0
        while q and count < n:
            q = q.link
            count += 1
        
        if not q:
            print("n is greater than number of elements in list")
            return       
        while q:
            p = p.link
            q = q.link
        if not p:
            return
        return p.info

    def count_occurence_iterative(self, key):
        p = self.start
        count = 0
        
        while p:
            if p.info == key:
                count += 1
            p = p.link
        return count
    
    def count_occurence_recursive(self, key):
        count = 0
        p = self.start
        
        def _cnt_rec_(node):
            if not node:
                return 0
            else:
                if node.info == key:
                    return 1 + _cnt_rec_(node.link)
                else:
                    return _cnt_rec_(node.link)
        return _cnt_rec_(p)
    
    def rotate(self, pos):
        
        if not self.start:
            return
        
        p = self.start
        q =  self.start
        
        for i in range(pos-1):
            p = p.link
            q = q.link
        
        while q.link:
            q = q.link
        
        q.link = self.start
        self.start = p.link
        p.link = None
        
    def is_palindrome(self):
        txt = ""
        p = self.start
        
        while p:
            txt = f"{txt}{p.info}"
            p = p.link
        
        return txt == txt[::-1]
            
    def is_palindrome2(self):
        p = self.start
        lst = []
        
        while p:
            lst.append(p.info)
            p = p.link
            
        p = self.start
        while p:
            if p.info != lst.pop():
                return False
            p = p.link
        
        return True
    
    def move_tail_to_head(self):
        p = None
        q = self.start
        
        while q.link:
            p = q
            q = q.link
        
        q.link = self.start
        self.start = q
        p.link = None
    
    def sum_from_list(self, lst2):
        p = self.start
        q = lst2.start
        carry = 0
        while p.link and q.link:
            sum = p.info + q.info + carry
            p.info = sum % 10
            carry = sum // 10
            p = p.link
            q = q.link
        
        sum = p.info + q.info + carry
        p.info = sum % 10
        carry = sum // 10
        p = p.link
        q = q.link
        
        if q:
            p = q.link
        while p:
            sum = p.info + carry
            p.info = sum % 10
            carry = sum // 10
            p = p.link
        
sllist = SingleLinkedList()
sllist.append("B")
sllist.append("C")
sllist.append("D")
sllist.prepend("A")
sllist.insert_after(sllist.start.link, "E")
sllist.delete("A")
sllist.delete_at_position(2)
sllist.len_iterative()
sllist.len_recursive(sllist.start)
sllist.prepend("A")
sllist.insert_after(sllist.start.link, "C")
sllist.swap_nodes("D", "E")
sllist.swap_nodes("A", "E")
#sllist.print_list()
sllist.reverse_iterative()
#sllist.print_list()
sllist.reverse_recursive()
#sllist.print_list()

sllist = SingleLinkedList()

sllist.append(1)
sllist.append(5)
sllist.append(6)
sllist.append(10)
sllist.append(10)


new_list = SingleLinkedList()

new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(6)
new_list.append(10)

sllist.merge_sorted(new_list)
#sllist.print_list() 

sllist.remove_duplicates()
#sllist.print_list() 
#print(sllist.get_nth_element_from_last(2))
#print(sllist.get_nth_element_from_last2(6))

new_list.append(2)
new_list.append(2)
new_list.append(3)
new_list.append(3)
new_list.append(3)
#print(sllist.count_occurence_iterative(1111))
#print(sllist.count_occurence_recursive(3))

sllist = SingleLinkedList()
sllist.append(1)
sllist.append(2)
sllist.append(3)
sllist.append(4)
sllist.append(5)
sllist.append(6)

sllist.rotate(3)

sllist = SingleLinkedList()

sllist.append("R")
sllist.append("A")
sllist.append("D")
sllist.append("A")
sllist.append("R")


new_list = SingleLinkedList()

new_list.append("R")
new_list.append("A")
new_list.append("D")
new_list.append("R")
new_list.append("I")

#print(sllist.is_palindrome())
#print(new_list.is_palindrome())


#print(sllist.is_palindrome2())
#print(new_list.is_palindrome2())


sllist = SingleLinkedList()
sllist.append(1)
sllist.append(2)
sllist.append(3)
sllist.append(4)
sllist.append(5)
sllist.append(6)
sllist.move_tail_to_head()

sllist = SingleLinkedList()
sllist.append(5)
sllist.append(6)
sllist.append(3)
#sllist.append(1)
#sllist.append(10)


new_list = SingleLinkedList()
new_list.append(8)
new_list.append(4)
new_list.append(2)
new_list.append(1)
#new_list.append(1)

sllist.sum_from_list(new_list)