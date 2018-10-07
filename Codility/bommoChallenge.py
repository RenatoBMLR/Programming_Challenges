#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:32:33 2018

@author: renatobottermaiolopesrodrigues
"""

def check_equals(bucket_dict, Q):
    
    for k in bucket_dict.keys():
        if (len(bucket_dict[k]) - len(set(bucket_dict[k])) >= Q-1):
            return True
    return False

def solution(N, Q, B, C):
    # write your code in Python 3.6
    
    bucket_dict = {}
    for i in range(len(C)):
        if B[i] not in bucket_dict.keys():
            bucket_dict[B[i]] = []
        bucket_dict[B[i]].append(C[i])
        
        if check_equals(bucket_dict, Q):
            return i
    return -1