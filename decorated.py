#!/usr/bin/env python3

# variables:
user_phrase=''
decor_char=''

def user_input():
    user_phrase=input('Enter a word or phrase: ')
    decor_char=input('Enter a decorator character: ')
    return user_phrase,decor_char

def decor_len_calc(u_phrase):
    d_len=len(u_phrase)
    return d_len

def print_phrase(phrase):
    print(phrase)

def print_decorated(d_char,d_len,phrase):
    print(d_char*d_len)
    print_phrase(phrase)
    print(d_char*d_len)

user_input=user_input()
user_phrase=user_input[0]
decor_char=user_input[1]

print(user_phrase)
print(decor_char)

decor_len=decor_len_calc(user_phrase)
print(decor_len)

print_decorated(decor_char,decor_len,user_phrase)

print('program finished executing')
