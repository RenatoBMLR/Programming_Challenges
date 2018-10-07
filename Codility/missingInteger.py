#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:54:51 2018

@author: renatobottermaiolopesrodrigues
"""

def solution(A):
    # write your code in Python 3.6
    #pass
    
    A.sort()
    for i in range(0, len(A)-1):
        if A[i] != A[i+1] and A[i]+1 != A[i+1]:
            if A[i]>0:
                return A[i] + 1
            return 1
    return A[-1] + 1