#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:56:52 2018

@author: emilybean612
"""
s = input("s: ")
vowels = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
print(vowels)


s = input("s: ")
count = 0
for i in range(len(s) - 2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count += 1
print(count)
    
    

s = input("s: ")
count = 0
m_count = 0
end = 0
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        count += 1
        if count > m_count:
            m_count = count
            end = i + 1
    else:
        count = 0
start = end - m_count
print('Longest substring in alphabetical order is:', s[start:end + 1])






        
    
    

