# dictionary data types are like list data types(immutable)
#     keys   values
dic = {1:'uno'' one',2:'des',3:'tres'}
print(dic[1])


# .keys() returns all the keys in a dictionary
# .value() returns all the values in a dictionary
# .items() returns all the contents of the dictionary
# .get() check if a key is present in a dictonary
dic.get(1,0)
# if the key 1 is present, returns the value of the key
# if absent reurns 0

# .setdefault() assigns a key value pair to a dictionary if the key is not present

dic.setdefault(4,'quadro')
print(dic)


# type(value) telles us the datatype of the value
