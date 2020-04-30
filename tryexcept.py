def inp():
    print('pls enter the number of cats you have')
    inpt = input()
    return inpt

try:
    call = int(inp())
    if call >=5 and call > 1 :
        print('thats a lotta cats')

    elif call<=0:
        print('i dont know about this one')

    else:
        print('you can surely accomadate a few more')

except ValueError:#if the specified error occurs in the block
                  #the try except statement acts like an if else block
                  #if the error occurs then the programs skips to the except block
    print('bruh, you have to enter a number')
    
test