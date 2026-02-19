import os

source = "lamb.test"
destination = "C:\\Users\\User\\Desktop\\copy.test"

try:
    if os.path.exists(destination):
        print("There is a file already")
    else:
        os.replace(source,destination)
        print(source+" was moved")
        
except FileNotFoundError:
    print("Source was not file")