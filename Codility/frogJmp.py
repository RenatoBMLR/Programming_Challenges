#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:44:42 2018

@author: renatobottermaiolopesrodrigues
"""

'''
Timeout solution :(

def solution(X, Y, D):
    
    if X<=Y:
        step = 0
        pos = X
        while(pos<Y):
            step += 1
            pos = X + step*D
        return step
    
    else:
        return -1
'''

def solution(X, Y, D):
    
    if (X<=Y):
        
        distance = Y-X
        if ((distance//D)*D == distance):
            return distance//D
        else:
            return distance//D + 1
    else:
        return -1
    
print(solution(2, 11, 3))