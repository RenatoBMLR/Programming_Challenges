#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:05:42 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):

        idx = 0
        common = []
        for i in range(len(A)):
            while (idx < len(B)):
                if A[i] < B[idx]:
                    break
                elif (A[i] == B[idx]):
                    common.append(B[idx])
                    idx += 1
                    break
                idx += 1
        return common
                