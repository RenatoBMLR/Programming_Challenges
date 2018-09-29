#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:19:50 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        
        stringNumber = A.split()[0]

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        negative_sign = False
        if(ord(stringNumber[0]) < ord('0')):
            if (stringNumber[0] == '-'):
                negative_sign = True
            stringNumber = stringNumber[1:]
        
        res = 0
        for char in stringNumber:
            if (ord(char)<=57):
                res = res*10 + ord(char) - ord('0')
            else:
                break
            
        if negative_sign:
            res -= 2*res
        if res > INT_MAX:
            res = INT_MAX
        if res < INT_MIN:
            res = INT_MIN
        return res