#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:13:57 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):

        if(n==0):
            return 1 % d;
        
        res = 1
        while(n>0):
            
            if(n%2==1):
                res = res * x % d
                n-=1
            else:
                x = x*x % d
                n/=2
        return res

    