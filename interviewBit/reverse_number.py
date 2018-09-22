#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:08:07 2018

@author: renatobottermaiolopesrodrigues
"""


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        x = abs(A)
        aux = ''
        while(x > 0):
            aux+=str(x%10)
            x=x//10
        if (A+abs(A)==0):
            aux = '-' + aux
        aux = int(aux)
        
        if(-2147483648 > aux):
            return 0
        elif(2147483647 < aux):
            return 0
        return aux

