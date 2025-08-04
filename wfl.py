# WFL interpreter version α0.0.2

import os

dir = input("Enter folder path to execute: ")

def fileDate(file):
    return os.path.getctime(os.path.join(dir, file))

fList = os.listdir(dir)
for file in fList:
    if not os.path.isfile(os.path.join(dir, file)):
        fList.remove(file)

fList.sort(key=fileDate)

print(fList)