#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:47:09 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        
        A.sort()
        aux = A[0]
        for it in range(1, len(A)):
            common = ''
            for i in range(0, len(aux)):
                if (aux[i] == A[it][i]):    
                    common += A[it][i]
                else:
                    break
            aux = common
        return aux
