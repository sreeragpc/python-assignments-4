""" Write a program to find the number of even numbers in an array
Program should accept an array and display the number of even numbers contained in that array
"""
size=int(input("enter the size of array"))
list=[]
print("enter the elements of array 1")
for i in range(size):
    element=int(input())
    list.append(element)
print("list = "+str(list))

count=0
for i in range(size):
    if list[i]%2==0:
        count=count+1
print('number of even numbers = ' + str(count))