import os

for root, dirs, files in os.walk("C:\\Users\\Documents\\CV"):
    for filename in files:
        print(filename)
        
