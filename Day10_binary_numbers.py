#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:01:16 2020
Task 
Given a base 10 integer,convert it to binary (base 2). 
Then find and print the base 10 integer denoting the 
maximum number of consecutive '1s in 'ns binary representation.
Input Format
A single integer,n
Constraints1<n<10**6
Output Format
Print a single base 10 integer denoting the maximum number of 
consecutive 1s in the binary representation of n
"""



def one_count(n):
    max_one_count = 0
    one_count = 0
    while n != 0:
        factor = n // 2
        remainder = n - 2 * factor
        n = factor
        print(n)
        if remainder == 1:
            one_count += 1
            max_one_count = max(max_one_count, one_count)
        else:
            one_count = 0
    print(max_one_count) 



if __name__ == '__main__':
    n = int(input())
    one_count(n)
    print(bin(n))
