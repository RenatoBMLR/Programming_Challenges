#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:34:39 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):

        count = 0
        while(A>0):
            if (A%2 != 0):
                count+=1
            A = A//2
        return count