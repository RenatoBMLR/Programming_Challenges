#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:46:30 2018

@author: renatobottermaiolopesrodrigues
"""


def solution(A, K):

    if len(A) == K:
        return A
    
    count = 0
    while (count < K):
        aux = None
        for i in range(len(A)-1):
            if not aux:
                aux, A[i+1] = A[i+1], A[i]
            else:
                aux, A[i+1] = A[i+1], aux
        A[0] = aux
        count += 1
    return A

solution([], 3)