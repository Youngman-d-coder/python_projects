#!/usr/bin/python3

def number():
    num = int(input("Enter a number:  "))
    return num

def count(num):
    for i in range(1, num + 1):
        print(i)

def main():
    num = number()
    count(num)

main()