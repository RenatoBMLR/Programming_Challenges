#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 11:25:54 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        
        lst = []
        for i in range(1, A + 1):
            aux = ''
            if(i%3==0):
                aux += 'Fizz'
            if(i%5==0):
                aux += 'Buzz'
            if(aux == ''):
                aux = str(i)
            lst.append(aux)
        return lst