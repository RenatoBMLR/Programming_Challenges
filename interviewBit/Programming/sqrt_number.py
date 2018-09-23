#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:23:31 2018

@author: renatobottermaiolopesrodrigues
"""


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        return self.binnary_search(A)
        
    def binnary_search(self, A):
    
        start, end = 1, A
        while(start<=end):
            mid = (start + end)//2
            if A - mid*mid == 0:
                return mid
            elif A > mid*mid:
                start = mid + 1
            else:
                end = mid - 1
        return end