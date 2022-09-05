""" 5th sep 2022 monday """
# ''' lists and list methods'''

# a=[]
# print(type(a))

# b=[10,20,30]
# print(type(b))
# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])

# c=[2,3,'hello']
# print(type(c))
# c[2]='hi'
# print(c)

# ''' append'''  # adds only 1 element that to on last of the list

# # a=[10,20,30]
# # a.append(40)
# # a.append('hello')
# # print(a)

# ''' clear '''  # used to clear all the elements in the list

# # a=[20,30,40]
# # a.clear()
# # print(a)

# ''' remove '''  # used when index no is not known. directly removes value from the list

# # a=[10,20,30,40]
# # # a.remove(20)
# # # print(a)
# # a.remove(200)
# # print(a)

# # ''' pop ''' # used to remove last element in the list.

# # a=[10,20,30,40]
# # a.pop()
# # print(a)

# ''' extend '''  # used to merge to lists and adds elements in the last.

# # a=[10,20,30]
# # b=[40,50,60]
# # a.extend(b)
# # print(a)
# # b.extend(a)
# # print(b)

# # ''' insert ''' # used to insert an element atany pakce of the list using index number.

# a=[10,20,30]
# a.insert(3,40)
# print(a)
# a.insert(0,5)
# print(a)
# a.insert(10,50)
# print(a)
# a.insert(1,(60,70))
# a.insert(10,(60,70))
# print(a)

''' count '''# to know how many times the element got repeated in list

# a=[10,20,30,'hello','hi',20]
# print(a.count(10))
# print(a.count(20))
# print(a.count(30))
# print(a.count('hi'))
# print(a.count('hello'))

''' index '''  # to know the index no of the element in the list

# a=[10,20,'hi','hello',30,40]
# print(a.index(10))
# print(a.index(20))
# print(a.index('hi'))
# print(a.index('hello'))
# print(a.index(70))

''' reverse ''' # to reverse the list

# a=[10,20,30,40]
# a.reverse()
# print(a)

''' sort ''' # to make ASC order or DSC order of the list.

# a=[10,20,30,15,5,25]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

print(dir(list))
