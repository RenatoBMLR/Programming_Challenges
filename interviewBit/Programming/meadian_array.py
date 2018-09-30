#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:22:48 2018

@author: renatobottermaiolopesrodrigues
"""

A = [ -37, -9, 10, 19 ]
B = [ -29, 18, 46 ]

C = A+B
C.sort()

n = len(C)
if (n%2 ==0):
    print( (C[(n//2)-1] + C[(n//2)])/2.0)
else:
    
    start, end = 0, n-1
    mean = (C[start]+C[end])/2.0
    
    while(start<end):
        
        mid = (start + end)//2
        
        if(mid > start):
            start = mid+1
        else:
            end = mid-1
    print(C[mid])
        
            
            
    
    
    