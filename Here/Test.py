import time
import os
import os.path
import urllib.parse

from os import walk

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


print('Hello!')
time.sleep(2)
print('')
print('To customise your experience, I need the name that has been allocated')
print('to this program...')
print('')
time.sleep(2)
print('What is the name of this program?')
program = input('')

time.sleep(1)
print('')
print('Move', program,'and survey files into a folder on your desktop...')
print('The folder should be named "Here", then move files into the folder')
print('named "PutReadeableFilesInHere".')


time.sleep(5)
print('')
print('Note: The program will allow you to read multiple files...')
time.sleep(0.5)
print('However, this is not recommended, as it will lead to issues')
time.sleep(0.5)
print("with Google's credentials. It will most likeley need a re-download")
time.sleep(0.5)
print("and setup of credentials, due to Google's security policy")
time.sleep(0.5)
print('If you do not wish to read another file, click enter 2x')
time.sleep(0.5)
print('and answer "yes" when prompted.')
time.sleep(0.5)
print('')
time.sleep(0.5)
print('It is NOT ADVISED - Unless you clear the spreadsheet and restart the program...')
time.sleep(4)
def main(num):
    print('')
    print('')
    print('')
    print('What is the username accociated with the computer?')
    name = input('')
    print('')
    
    
    print('Here are the file(s) you asked for:')
    root = r"C:\Users\%s\Desktop\Here\PutReadeableFilesInHere" % name
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('permissions.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('survey').sheet1
    repeat(root, sheet, 1)

def repeat(root, sheet, num):               
        index = 1
        call = 0
        for dirpath, dirnames, filenames in walk(root):
            for filename in filenames:
                address = os.path.splitext(filename)
                if address[1] =='.txt':
                    print(filename)
                    call=call+1
                if address[1] =='.csv':
                    print(filename)
                    call=call+1
                elif address[1] =='.tsv':
                    print(filename)
                    call=call+1
        if call == 0:
            print('There are no files with extension ".txt" or ".csv')
    


        
        

        #time.sleep(3)

        # File Objects

        ok = True
        while ok:
            print('')
            print('Type the name of the file you would like.') 
            print('(.txt, .csv and .tsv are the only files supported')
            print('in this version of the software),')
            print('or just type "list" to re-list the file names:')

            #print('or, just type "All" to do all of them...')
            file =  input('')
            if file =="list":
                repeat(root, sheet, 1)
            file = os.path.join(root, file)

            print('The file root is "%s" is that ok?' % file)
            check = input('')
            #check = input("you have chosen %s is that ok?" % file)
        
            #x_file = open(root+"\"+, "r")
             
            if check == "yes":
          
                if os.path.isfile(file) and os.access(file, os.R_OK):
                    print("File exists and is readable...")

                    address = os.path.splitext(file)
                    if address[1] =='.txt':
                        seperator = '='
                    if address[1] =='.csv':        
                        seperator = ','
                    if address[1] =='.tsv':
                        seperator = '"'

                    with open('output%d.txt' % num, 'w') as f2:
                        with open(file, 'r') as f:
                            for f_contents in f: 
                                f_contents = urllib.parse.unquote(f_contents)
                                f2.write(f_contents)
                                print(f_contents, end='')
                                row = f_contents.split(seperator)
                                sheet.insert_row(row, index)
                                index = index + 1
                else:
                    print('Either the file is missing or not readable!')
                    print('It could also be, however,') 
                    print('that you simply typed the name in incorrectly!')
        
            elif check == "":
                ok = False
                #urlsafe_b64decode
    
main(0)


#index = 1

#ok2 = True
#while ok2:    
    #if check == "All":
        #def All(num):
            #for dirpath, dirnames, filenames in walk(root):
                #if os.path.isfile(file) and os.access(file, os.R_OK):
                    #print("The Files exist and are readable...")
                        #with open('output%d.txt' % num, 'w') as f2:
                            #with open(file, 'r') as f:
                                #for f_contents in f: 
                                    #f_contents = urllib.parse.unquote(f_contents)
                                    #f2.write(f_contents)
                                    #print(f_contents, end='')
                                    #row = f_contents.split('=')
                                    #sheet.insert_row(row, index)
                                    #index = index + 1
                #else:
                    #print("Either the files are missing or they are not readable!")
      
    #elif check == "":
        #ok2 = False
        #urlsafe_b64decode
#main(0)


print('')
print('Have you completed all the files?')
repeat = input('')

if repeat == "no":
    #if __name__ == "__main__":
    print('')
    print('')
    main(1)

if repeat == 'yes':
    print('')
    print('Thank you for using the program...')
    
time.sleep(1)

print('')   
print('Goodbye!')
time.sleep(1)
#exit()

#where the code starts.
#main()