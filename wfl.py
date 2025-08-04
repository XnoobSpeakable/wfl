# WFL interpreter version α0.0.4

# INITIALIZE
import os

debug = int(input("Debug mode? (1 for yes, 0 for no): "))
dir = input("Enter folder path to execute: ")

def fileDate(file):
    return os.path.getctime(os.path.join(dir, file))

fList = os.listdir(dir)
for file in fList:
    if not os.path.isfile(os.path.join(dir, file)):
        fList.remove(file)

fList.sort(key=fileDate)

if debug:
    print(fList)

# INSTRUCTION LOOP
for inst in fList:
    print(inst)