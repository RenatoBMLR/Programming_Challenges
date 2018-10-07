#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:11:07 2018

@author: renatobottermaiolopesrodrigues
"""

def solution(A):
    
    if len(A)>=2:
        abs_diff = abs(sum(A[0:1]) - sum(A[1:]))
        for i in range(2, len(A)):
            aux  = abs(sum(A[0:i]) - sum(A[i:]))
            if abs_diff > aux:
                abs_diff = aux
        return abs_diff
    else:
        return 0
    