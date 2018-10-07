#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:41:59 2018

@author: renatobottermaiolopesrodrigues
"""

def solution(X, A):
    

    head, tail = 0, len(A) -1

    while (head<=tail):
        
        mid = (tail+head)//2
        
        if A[mid] == X:
            return mid
        
        elif A[mid] > X:
            tail = mid -1
        else:
            head = mid - 1
        

    
    return -1


print(solution(3, [3, 1, 2, 5, 6, 9]))