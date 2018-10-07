#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:43:17 2018

@author: renatobottermaiolopesrodrigues
"""

def solution(A):
    
    
    if len(A) == 0:
        return 1
        
    A.sort()
    for i in range(1, len(A) + 1):
        if A[i-1] != i:
            return i
    return A[-1] + 1