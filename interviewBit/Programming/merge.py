#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:04:28 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        
        '''
        # example
        # A : [ -4, -3, 0 ]
        # B : [ 2 ]
        
        A += B
        A.sort()
        print(" ".join(map(str, A)) + " ")
        '''
        

        sorted_list = []
        while (A and B):
            if (A[0] <= B[0]):
                item = A.pop(0)
                sorted_list.append(item)
            else:
                item = B.pop(0)
                sorted_list.append(item)
        sorted_list.extend(A if A else B)
        A = sorted_list
    
        print(" ".join(map(str, A)) + " ")

