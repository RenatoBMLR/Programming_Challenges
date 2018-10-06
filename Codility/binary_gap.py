#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 12:16:07 2018

@author: renatobottermaiolopesrodrigues
"""

def solution(N):
    # write your code in Python 3.6

    
    binnary = ''
    while(N>=1): 
        binnary += str(N%2)
        N = N//2
    binnary = binnary[::-1]
    
    aux = []
    zero_counter = 0
    count = 0
    for i in range(len(binnary) - 1):
        if count == 0:
            if binnary[i] != binnary[i+1] and binnary[i]=='1':
                count += 1
        else:
            zero_counter += 1
            if binnary[i] != binnary[i+1] and binnary[i]== '0':
                aux.append(zero_counter)
                zero_counter = 0
                count = 0
                
    if len(aux) > 0:
        return max(aux)
    return 0 
