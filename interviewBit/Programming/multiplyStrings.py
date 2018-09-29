#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:46:37 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        
        return self.atoi(A)*self.atoi(B)
        
    def atoi(self, n):
        
        negative_signal = False
        if (ord(n[0])<ord('0')):
            if n[0]=='-':
                negative_signal = True
            n = n[1:]
        res = 0
        for c in n:
            res = res*10 + ord(c) - ord('0')
        if negative_signal:
            res -= 2*res
        return res
