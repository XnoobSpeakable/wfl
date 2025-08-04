# WFL interpreter version α0.1.1

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

# EXECUTION FUNCTIONS
# Currently empty

#VARIABLE HANDLING
vars = {}

# INSTRUCTION LOOP
for inst in fList:
    splitInst = inst.split()
    opcode = splitInst[0]
    if opcode == "0":
        out1 = splitInst[1]
        print("PROGRAM HALTED. EXIT CODE " + out1)
    elif opcode == "1":
        in1 = splitInst[1]
        in2 = splitInst[2]
        # NOT COMPLETE
    elif opcode == "13":
        in1 = splitInst[1]
        if in1 in vars:
            "INTERPRETER WARNING: Variable '" + in1 + "' already exists. Overwriting."
        vars[in1] = {'val': None, 'type': 'INT'}
