#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:34:30 2020
@author: Mukut Ranjan Kalita
Context 
Given a 6X6 2D Array,A :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices 
falling in this pattern in As graphical representation:
a b c
  d
e f g   
There are  hourglasses in A and an hourglass sum is the sum of an 
hourglass' values. 
Task 
Calculate the hourglass sum for every hourglass in A then print 
the maximum hourglass sum.
Input Format
There are 6 lines of input, where each line contains 6
space-separated integers describing 2D Array A every value in A  
will be in the inclusive range of  -9 to 9 .
"""


def get_hr_sum(matrix,row,col):
    sumtotal=0
    sumtotal+=matrix[row-1][col-1]
    sumtotal+=matrix[row-1][col]
    sumtotal+=matrix[row-1][col+1]
    sumtotal+=matrix[row][col]
    sumtotal+=matrix[row+1][col-1]
    sumtotal+=matrix[row+1][col]
    sumtotal+=matrix[row+1][col+1]
    return sumtotal
    
def hr_sum(arr):
    # remember minimum is -63, if all elements are -9
    max_hr_sum = -63     
    for i in range(1,5):
        for j in range(1,5):
            current_hr_sum = get_hr_sum(arr,i,j)
            if current_hr_sum >max_hr_sum:
                max_hr_sum = current_hr_sum
    print(max_hr_sum)            

if __name__ == '__main__':
    arr = []
# in the prompt enter 6 lines with 6 elements
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hr_sum(arr)
        
