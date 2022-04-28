"""Write a program to identify whether a string is a palindrome or not
A string is a palindrome if it reads the same backward or forward eg: MALAYALAM
Program should accept a string and display whether the string is a palindrome or not
"""

a=input("enter a word")
reva=a[::-1]
if a==reva:
    print("entered word is a palindrome")
else:
    print("entered word is not a palindrome")