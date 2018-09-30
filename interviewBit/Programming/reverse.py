#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:59:31 2018

@author: renatobottermaiolopesrodrigues
"""

A=5
count = '00000000000000000000000000000000'
idx = 0 
while(A>0):
    if (A%2 != 0):
        count[idx] = '1'
    else:
        count[idx] = '0'
    A = A//2
    idx+=1
    
    