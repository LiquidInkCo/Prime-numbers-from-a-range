#!/usr/bin/env python
# coding=utf-8
import os
import re
import math
import shutil
import subprocess
import sys



def prime_numbers(start,end):
    if start < 1:
        print("The entered range must consist of positive natural numbers only\n")
        user_input()
    if end > 9999:
        print("The entered range is too large\n")
        user_input()
    if end <= start:
        print("Not a valid range\n")
        user_input()

    list1 = range(start,end+1)
    list2 = [1]
    mylist = []
    for x in range (start,end+1):
        var = x / 2
        h = int(round(var)) + 1
            
        for y in range(1,h+1):
            if y != 1:
                q = float(float(x) / y)
            else:
                q = 0.5
                
            i, d = divmod(q, 1)
                
            if d == 0:
                mylist.append(x)


    filtered = [item for item in list1 if item not in mylist]
    filtered = [item for item in filtered if item not in list2]
    
    if start <=2:
        z = 2
        filtered = [z] + filtered

    print("\nPrime numbers in that range:  \n")
    print(filtered)
    print("\n")
    user_input()


def user_input():
   a = "Hello"
   try:
       a = int(input("Enter the starting number of the range (press enter to exit): "))
   except NameError:
        print("Not an integer value...")
        user_input()
   except:
        print("Have a nice day!")
        sys.exit()


   b = "Hello"
   try:
       b = int(input("Enter the ending number of the range (press enter to exit): "))
   except NameError:
        print("Not an integer value...")
        user_input()
   except:
        print("Have a nice day!")
        sys.exit()

   prime_numbers(a,b)


user_input()