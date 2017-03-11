#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 22:48:56 2017

@author: christophergreen

Pandigital Fibonacci ends
Problem 104
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for 
which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not 
necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci 
number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the 
last nine digits are 1-9 pandigital, find k.
"""

elems=['1','2','3','4','5','6','7','8','9'];

def is_pandigital(num):
    i=0;
    while i<9:
        if elems[i] in str(num):
            i+=1;
        else:
            return False;
    return True;
    
fib=[1,1,2];

def assemble(maximum):
    i=4
    while i<maximum:
        if i%100==0:
            print("passing through Fibo#",i,"so there'a another hundred")  
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
        a=str(fib[len(fib)-1])
        if is_pandigital(a[(len(a)-9):]):
            print("the last nine digits of Fibo#",i,"are pandigital")
            if is_pandigital(a[:9]):
                print("found it! Fibo#",i,"=",a,"has both first nine and last nine digits pandigital")
                return i
        if is_pandigital(a[:9]):
            print("Fibo#",i,"=","has first nine digits pandigital")
        i+=1
    return
    
assemble(10**6); #329468 CORRECT




