#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:40:54 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        
        intervals = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
        lst = [item for sublist in intervals for item in sublist]
        lst.sort()
        
        aux = []
        k = 0
        while(k<len(lst)-1):
            for j in range(k+1, len(lst)):
                if (lst[j]-lst[j-1]>1):
                    aux.append([lst[k], lst[j]])
                    k = j+1
                    break
            if len(aux) == 0:
                aux.append([lst[0], lst[-1]])
                break
        return aux