import logging,os,shutil

logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
print('Do you want to backup files or do you want a list of files and their locations?\nenter list for list and bkp for backup')
bkp_or_list = input()
logging.debug(bkp_or_list)
    
def filetype():
    print('enter the file type \nexample input : py, jpg, psd   etc')
    filetype = input()
    return filetype

def pathos():
    # creates backup folder or file
    bkpfold =''
    bkppath =''
    if bkp_or_list == 'bkp':
        print('where do you want your files to be backed up')
        fold = input() 
        foldname = filetype+'_backup'
        path = os.path.join(bkpfold, foldname) # stores backup directory
        logging.debug('folder path is %s' % path)

        if os.path.isdir(bkppath) == False :
            os.makedirs(path)
        return path

    else:
        print('where do you want your list to be')
        fold = input()
        if fold == '':
            fold = 'c:\\'
        fold = r"{}".format(fold)
        filename = fileType+'_FliesList.txt'
        path = os.path.join(fold, filename) # full path leading to file
        logging.debug('folder path %s' % path)
        
        if os.path.isfile(path) == False:
            temp = open(path, 'w+')
            temp.close()
        return path

def Serch():
    print('enter the file path where you want your files to be searched:\nexample input  c:\\users\\etc\nsearches whole drive by default')
    wertosearch = input() #location to search for filetype
    logging.debug(wertosearch)
    if wertosearch == '':
        return 'c:\\'
    else:
        wertosearch = r"{}".format(wertosearch) # converts it into a raw string
        logging.debug(wertosearch)
        return wertosearch

fileType = filetype()
path = pathos()
serchPath = Serch()


logging.debug('Start of for loop')

if bkp_or_list =='bkp':
    for fold, subf, file in os.walk(serchPath):

            file[:] = [f for f in file if not f.startswith('.')]
            subf[:] = [s for s in subf if not s.startswith('.')] #skips hidden folders
            for i in range(len(file)): # iterating over the list of files 

                try:
                    if file[i].endswith('.'+fileType):
                        if os.path.isfile(os.path.join(path, file[i])) == False: #checks if file is already present in backup folder
                            shutil.copy(os.path.join(fold, file[i]), path)

                except FileNotFoundError:
                    logging.error('NoT eXiSt')

else:
    
    bffr = '' # stores raw file data
    bffr2= '' # stores stripped file data
    
    for fold, subf, file in os.walk(serchPath):
        for j in range(len(file)):
            if file[j].endswith('.'+fileType):
                temp = open(path, 'r+')
                bffr = temp.readlines()

                for i in range(len(bffr)):
                    bffr2 = bffr[i].rstrip()
                    logging.warning(bffr2)
                    if bffr != os.path.join(fold, subf, file[j]):
                        temp.write("{} in {}\n".format(file[j],fold))
temp.close()