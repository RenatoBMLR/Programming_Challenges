#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:17:41 2018

@author: renatobottermaiolopesrodrigues
"""
def getNumStu(A, max_page):
    cur_page = 0
    num_stu = 1
    for p in A:
        cur_page += p
        if cur_page > max_page:
            cur_page = p
            num_stu += 1
    return num_stu

A = [12, 34, 67, 90]
B = 2
start = max(A)
end = sum(A)

while start + 1 < end:
    mid = start + (end-start)/2
    num_student = getNumStu(A, mid)
    print (mid)
    print (num_student)
    print ("-------")
    if num_student <= B:
        end = mid
    else:
        start = mid + 1
if getNumStu(A, start) <= B:
    print(start)
else:
    print( end)


