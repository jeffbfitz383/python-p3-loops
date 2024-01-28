#!/usr/bin/env python3

def happy_new_year():
        start = 10
        while start > 0:
            print(start)
            start = start -1
        print("Happy New Year!")

def square_integers(int_list):
    all =[]
    for i in range(len(int_list)):
        j = (int_list[i]) ** 2
        all.append(j)
    return all

def fizzbuzz():
    for i in range(1,101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz()





