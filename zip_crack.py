"""
This program only works with Legacy Zip Files
Developed by: @Pall1n
"""
import zipfile

def crack_password(password_list, obj):
    index = 0
    with open(password_list, 'rb') as file:
        for line in file: # read line by line
            for word in line.split():
                try:
                    index += 1
                    obj.extractall(pwd=word) # Try to extract all files with password
                    print("Password found at line", index)
                    print("Password is", word.decode())
                    return True # If password is found, return True
                except:
                    continue # If password is not found, continue to next line
    return False


password_list = "password.txt" #The name of the paswword list file
  
zip_file = "sample.zip" #The name of the zip file

obj = zipfile.ZipFile(zip_file) #Create an object of the zip file
  
if crack_password(password_list, obj) == False:
    print("Password not found in this file")
