#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:21:31 2018

@author: renatobottermaiolopesrodrigues
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):                
        diff  = 0
        for i in range(len(A)-1):
            for j in range(i + 1, len(A)):
                aux  = abs(A[i] - A[j]) + abs(i-j)
                if (aux > diff):
                    diff = aux
        return diff        