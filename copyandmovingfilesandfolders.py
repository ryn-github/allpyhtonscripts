import shutil,os

# shutil.copy(arg1, arg2) 
# arg one is file to be copied
# arg two is the destination at which it should be copied

shutil.copy(r'C:\Users\Rayyan Malik\Pictures\spidwagon.png',r'C:\Users\Rayyan Malik\Pictures\speedwagon.png')

# using a different file name in the second argument renames the file

# shutil.move(arg1, arg2)
# works as a cut paste command
# can also be used to rename files like shutil.copy() 

# folder can be moved and copied
# shutil.copytree/movetree(arg1, arg2) is used  

# os.unlink() will delete a file.
# os.rmdir() will delete a folder (but the folder must be empty).
# shutil.rmtree() will delete a folder and all its contents.
# Deleting can be dangerous, so do a "dry run" first.
# send2trash.send2trash() will send a file or folder to the recycling bin.

os.unlink(r'c:\users\rayyan malik\pictures\speedwagon.png')