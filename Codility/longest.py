#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:18:52 2018

@author: renatobottermaiolopesrodrigues
"""

def solution(A):
    
    # A = [6, 10, 6, 9, 7, 8]
    A.sort()
    # A = [6, 6, 7, 8, 9, 10]

    diff_counter = 0
    longest, aux = [], []
    for i in range(len(A)-1):
        diff_counter += A[i+1]-A[i]  # avoid negative
        aux.append(A[i])
        
        if diff_counter > 1:
            diff_counter = 0
            if len(longest) < len(aux):
                longest = aux
            aux = []
            
    return len(longest)

#print(solution([3, 1, 7, 8, 9, 2, 10] ))
#print(solution([1,7,6,2,6,4] )) #expected 3
print(solution([6, 10, 6, 9, 7, 8]))  #expected 3