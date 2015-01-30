#Import dependencies
#Load OS functions from the standard library
import os

os.chdir('/home/israel/Development/Python_Exercises/python-octo-wookie/head1stpython/Chapter3')
#Change path for the current directory

data = open('sketch.txt')


#Start iteration over the text file
for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                print(role, end = '')
                print(' said: ', end = '')
                print(line_spoken, end = '')
            except:
                pass

data.close()
        
