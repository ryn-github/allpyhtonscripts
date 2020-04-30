# list data type is like an array in java
#    0 1 2 3   4
ar =[1,2,3,4,'adfa']

# they are versatile and can any basic data type(string,int....)
# first element is in zeroth position second in 1st and so on
# .index(value) can be used to find out the element's postion

for i in range(len(ar)):
    print(ar[i])
print('')

#you can have a list inside a list

ar1 = [[1,2,3,4],['a','b','c','d','e','f']]

#[1,2,3,4] are in the zeroth postion
#[a,b,c....] are in the 1st postion

#elements inside the sublists can accesed like this:
# var[m][n]
print(ar1[1][0])
print('')

# negative numbers can also be used to get the position of elements inside the list
# -1 being the last element -2 being the last second.....
print(ar[-2])
print('')

# elements can also be called in this manner
# var[m:n]
# this includes elements from mth postion uptill nth position, not including n

print(ar[1:3])

# in and not in opertors can be used to check whether the element in question is in the list or not 

person = ['binary','friendly','cool']
gender, nature, stats = person


# .append(value) and .insert(index,value) can be used to add items to lists
# .append() adds the value to the end of the list
# .remove(value) removes the value from the list
# del list(index) is used to delete elements at that index postions
ar = ar.append(5)
ar = ar.insert(2,'sixnine')
ar = ar.remove(5)
del ar[2]

# .sort() can be used to sort lists
# it sorts items in ascending order by default
# .sort(reverse = true) can be used to sort items in decsending order
# list that contain both numerical values and strings cannot be sorted



# lists are immutable data types
# that just means that when it is copied to a different variable
# it is not copied, the new variable only points at the original list variable
# if you do want to copy a list to a new variable
# import the module copy
# .deepcopy(list)
# lists dont follow indentation rules
