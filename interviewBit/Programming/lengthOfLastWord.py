#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:43:38 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        lst = A.split()
        if len(lst)>0:
            return len(lst[-1])
        return 0
