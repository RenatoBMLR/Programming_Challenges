#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:58:35 2018

@author: renatobottermaiolopesrodrigues
"""

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        
        countAndSay = '1'
        ans = ''
        i = 0
        while(i < A-1):
            
            if(len(countAndSay.split()[-1]) == 1):
                ans = str(len(countAndSay.split()[-1])) + countAndSay.split()[-1][-1]
            else:
                
                last = countAndSay.split()[-1]
                
                for idx in range(0, len(last)):
                    count = last[idx]
                    for it in range(idx+1, len(last)):
                        if(last[idx] == last[it]):
                            count += last[it]
                        else:
                            
                            break
                    if idx != len(set(last)):
                        ans += str(len(count)) + count[-1]
        
            countAndSay += ' ' + ans
            ans = ''
        
            i+=1
        return countAndSay.split()[-1]
    