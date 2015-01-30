#Import dependencies
#Load OS functions from the standard library
import os

#Change path for the current directory
os.chdir('/home/israel/Development/Python_Exercises/python-octo-wookie/head1stpython/Chapter3')

#Start our program
try:
    
    #Load the text file into 'data' variable
    data = open('sketch.txt')

    #Start iteration over the text file
    for each_line in data:
    #We use try/except to handle errors that can occur with bad input
                try:
                    (role, line_spoken) = each_line.split(':', 1)
                    print(role, end = '')
                    print(' said: ', end = '')
                    print(line_spoken, end = '')
                except:
                    pass

    #After all the iteration and printing, we close the file
    data.close()

#If file doesn't exist we simply quit and display an error for the user/dev
except:
    print('The data file is missing!')
        
