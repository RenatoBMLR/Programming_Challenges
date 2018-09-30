#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:23:40 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):

        
        idx = 0
        while(idx<len(A) - 1):
            if A[idx] != A[idx + 1]:
                idx +=1
            else:
                A.pop(idx)
        return len(A)
