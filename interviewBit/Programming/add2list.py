#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:09:44 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def plusOne(self, A):
        aux  = int(''.join(map(str,  A))) + 1
        return list(map(int, list(str(aux))))
        
        
	    
	    
	    
