#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:23:37 2018

@author: renatobottermaiolopesrodrigues
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        
        minimum, maximum = 0, len(A)-1
        
        while(minimum<maximum):
            middle = minimum + (maximum - minimum)//2
            
            if (A[middle] == B):
                return middle
            elif (A[middle] < B):
                minimum = middle + 1
            elif (A[middle] > B):
                maximum = middle - 1
        
        if A[maximum] < B: 
            return maximum + 1
        return maximum
            
