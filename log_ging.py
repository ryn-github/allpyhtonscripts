import logging
logging.basicConfig(level = logging.Debug, format = '%(asctime)s - %(levelname)s - %(message))
# to save log messeges to a file, use this syntax:  
# logging.basicConfig(filename = 'filepath', level = logging.Debug, format = '%(asctime)s - %(levelname)s - %(message)) 

loggin.disable(logging.CRITCAL)
#disables all the logging output


# logging.debug()
# acts like a print function in a way


# logging function has 5 levels, priority is in ascending order
# .debug
# .info
# .warning
# .error
# .critical