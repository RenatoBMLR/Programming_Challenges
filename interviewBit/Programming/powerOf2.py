#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:17:25 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):

        number = int(A)
        if number == 1:
            return 0
        while((number > 1.0) & (number%2 == 0)):
            number = number/2
        if number == 1:
            return 1
        return 0
    