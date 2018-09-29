#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:09:12 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        
        if ((len(A) == 0) | (len(B)==0) | (len(B)>len(A))):
            return -1
        if (A==B):
            return 0
            
        for i in range(0, len(A) - len(B)):
            if (A[i:i+len(B)] == B):
                return i
        return -1

                