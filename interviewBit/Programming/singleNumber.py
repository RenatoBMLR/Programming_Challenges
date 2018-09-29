#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:55:07 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        A = list(A)
        A.sort() # need to improve this
        
        for i in range(0, len(A)-1, 2):
            if A[i] != A[i+1]:
                return A[i]
        return A[-1]