my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))

#taking inputs from user in form of tuple

tup = input("enter 5 numbers with one space between them")
a = tuple(tup.split())
print(a)
print(type(a))