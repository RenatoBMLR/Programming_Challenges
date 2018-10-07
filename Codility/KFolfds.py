#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:43:54 2018

@author: renatobottermaiolopesrodrigues
"""

import random
def solution(indices, K):
    
    train_size = (K-1)*len(indices)//K
    valid_size = len(indices)//K
    
    res = []
    for f in range(K):
    
        train_set = indices[f::K]
        valid_set = [idx for idx in indices if idx not in train_set]
    
        res.append(train_set)
        res.append(valid_set)
    return res

print(solution([1,2,3,2,32,1,4,3], 2))