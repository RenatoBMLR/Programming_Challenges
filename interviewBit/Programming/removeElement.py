#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:18:39 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        
        j = 0
        for i in range(0, len(A)):
            if A[i] != B:
                A[j] = A[i]
                j+=1
        A = A[:j]
        return len(A)