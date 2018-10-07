#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:44:53 2018

@author: renatobottermaiolopesrodrigues
"""
def solution(A):
    
    A.sort()
    count = 1
    for i in range(len(A)):
        if (A[i] != count):
            return 0
        count += 1
    return 1