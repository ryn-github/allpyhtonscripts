# open(filename) opens the file
# it can be saved to a filedatatype(filevar)
# if file is not present at location, a new file is created
readmefile = open(r'C:\Users\Rayyan Malik\Downloads\softwares\mysql-8.0.19-winx64\README','a')


# filevar.readlines() displays the strings in a list

# readmefile.close()
# closes the file

# open() can take two arguments
# first argument is the file path
# 2nd arg is the mode in which .write() operates
# open('','a') runs the .write() in append mode
# open('','w') run the .write() in overwrite mode

readmefile.write('Bruh \nBruhsoundeffect.mp4 ')
# .write() puts the file into write mode and the file cannot be read
readmefile.close()
readmefile = open(r'C:\Users\Rayyan Malik\Downloads\softwares\mysql-8.0.19-winx64\README')
store2 = readmefile.read()
print(store2)
