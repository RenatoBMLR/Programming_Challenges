#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:40:11 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        '''
            B = [0, 0, 0]
            for i in A:
                B[i] += 1
            return [0]*B[0] + [1]*B[1] * [2]*B[2]
        '''
        
        return self.bubbleSort(A)
    
    def bubbleSort(self, A):
        
        for i in range(len(A)-1):
            for j in range(i,  len(A)):
                if A[i]>A[j]:
                    A[i], A[j] = A[j], A[i]
        return A
    