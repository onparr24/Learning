# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:32:59 2022

@author: Justin
"""
import sys
import random
import time

def pass_generator(): #asks for required password length and generates a random password at that length.
    global char_list
    char_list = "1234567890!@#$%^&*()-=_+qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    global newpassword
    newpassword = ""    
    length = int(input("What length do you want your password?\n"))
    if(length<1):
        print("password must be more than 0 characters long\n")
        length = int(input("What length do you want your password?\n"))
    if(length>100):
        print("password should be less than 100 characters long\n")
        length = int(input("What length do you want your password?\n"))
    while(len(newpassword)<length):
        newpassword += random.choice(char_list)
    return(newpassword)

def brute_force_password(): #randomly generates a password and compares it to your password. 
    global char_list
    char_list = "1234567890!@#$%^&*()-=_+qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    comparator = ""
    print("Calculating\n")
    print("This could take awhile...\n")
    start_time = time.time()
    while(comparator != newpassword):
        comparator = ""
        number = random.randint(1,100)
        while(len(comparator)<number):
            comparator +=random.choice(char_list)
    print(comparator)
    end_time = time.time()
    time_len = end_time - start_time
    print(str(time_len) + " seconds\n") 

global char_list
char_list = "1234567890!@#$%^&*()-=_+qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" 
answer1 = input("Do you want to test a custom password?(y/n)\n")
answer2 = "n"
if(answer1=="y"):
    newpassword = input("enter your password\n")
    i = 0
    while(i<len(newpassword)):
        if(newpassword[i] not in char_list):
            print(newpassword[i] + " is not a valid character. Exiting")
            sys.exit()
        i += 1
    brute_force_password()
if(answer1=="n"):
    answer2 = input("Do you want to generate a new password?(y/n)\n")
if(answer2=="y"):
    pass_generator()
    print(newpassword + " is your new password.\n")
    print("Testing new password \n")
    brute_force_password()
else:
    print("Exiting")
    sys.exit()


    