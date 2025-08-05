# WFL interpreter version α1.1.0

# INITIALIZE
import os

debug = int(input("Debug mode? (1 for yes, 0 for no): "))
varOpcodes = int(input("Allow opcodes to be variables (not recommended)? (1 for yes, 0 for no): "))
dir = input("Enter folder path to execute: ")

def fileDate(file):
    return os.path.getctime(os.path.join(dir, file))

fList = os.listdir(dir)
for file in fList:
    if not os.path.isfile(os.path.join(dir, file)):
        fList.remove(file)

if debug: print("DEBUG: fList " + str(fList))

fList.sort(key=fileDate)

if debug: print("DEBUG: sorted fList " + str(fList))


#VARIABLE HANDLING
vars = {}

def variableDecode(splitInst, varSplit):
    if varSplit == 1:
        if debug: print("DEBUG: variableDecode vars " + str(vars))
        return vars[splitInst]["val"]
    else:
        return splitInst

# EXECUTION FUNCTIONS
def BinaryLogic(a, b, gate, notGate=False):
    if gate == "AND":
        result = int(a) & int(b)
    elif gate == "OR":
        result = int(a) | int(b)
    elif gate == "XOR":
        result = int(a) ^ int(b)
def AndFunction(a, b):
    return int(a) & int(b)
def OrFunction(a, b):
    return int(a) | int(b)

# INSTRUCTION LOOP
for inst in fList:
    splitInst = inst.split(" ")
    if debug: print("DEBUG: splitInst pre split loop " + str(splitInst))
    varSplit = []
    loopList = splitInst
    loops = 0
    for string in loopList:
        varSplit.append(0)
        if string == "":
            varSplit[loops-1] = 1
            splitInst.remove(string)
        loops += 1

    if debug:
        print("DEBUG: inst, splitInst, varSplit")
        print(inst)
        print(splitInst)
        print(varSplit)
    
    if varOpcodes:
        opcode = variableDecode(splitInst[0], varSplit[0])
    else:
        opcode = splitInst[0]

    if int(opcode) in range(0, 30) or int(opcode) in range(32, 34):
        in1 = variableDecode(splitInst[1], varSplit[1])
    if int(opcode) in range(1, 4) or int(opcode) in range(5, 11) or int(opcode) in range(18, 25):
        in2 = variableDecode(splitInst[2], varSplit[2])
    if int(opcode) in range(9, 11):
        in3 = variableDecode(splitInst[3], varSplit[3])

    if int(opcode) in range(30, 32):
        out1 = splitInst[1]
    if opcode == "4" or int(opcode) in range(16, 18) or opcode == "25":
        out1 = splitInst[2]
    if int(opcode) in range(1, 4) or int(opcode) in range(5, 8) or int(opcode) in range(18, 25):
        out1 = splitInst[3]

    if opcode == "0":
        print("INTERPRETER MESSAGE: PROGRAM HAS HALTED. EXIT CODE: " + str(in1))
        print("PRESS CTRL+C TO EXIT.")
        while True:
            pass
    elif opcode == "1":
        vars[out1]["val"] = AndFunction(in1, in2)
    elif opcode == "2":
        vars[out1]["val"] = OrFunction(in1, in2)
    elif opcode == "13":
        if in1 in vars:
            "INTERPRETER WARNING: Variable '" + in1 + "' already exists. Overwriting."
        vars[in1] = {'val': None, 'type': 'INT'}
    elif opcode == "33":
        print(in1)
        
print("INTERPRETER WARNING: EXECUTION FINISHED WITH NO HALT INSTRUCTION.")
print("PRESS CTRL+C TO EXIT.")
while True:
    pass