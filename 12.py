""" Write a program to sort an array in descending order
Program should accept and array, sort the array values in descending order and display it
"""

size=int(input("enter the size of array"))
list=[]
print("enter the elements of array ")
for i in range(size):
    element=int(input())
    list.append(element)
print("list = "+str(list))
list.sort(reverse=True)
print("list after sorting = "+str(list))