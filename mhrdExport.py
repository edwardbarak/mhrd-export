#!/usr/bin/python3

import codecs
import string
import re
from time import sleep

print('MAKE SURE THE savestate FILE IS IN THE SAME DIRECTORY AS THIS EXECUTABLE, OTHERWISE IT WON\'T WORK')
sleep(5)

# Read file using utf8, and ignoring errors due to savestate encoding being uknown.
file = codecs.open('savestate', 'r', encoding='utf-8', errors='ignore')
savestate = file.read()
file.close()

# Filter out extraneous characters
printable = set(string.printable)
savestate_filtered = ''.join(filter(lambda x: x in printable, savestate))

# Find name and code for each gate user has created
ptn = re.compile('(?s)([A-Z0-9]*?)sq~pt.*?(Inputs:.*?Wires:.*?;)') # Misses RAM4W16B
output = re.findall(ptn, savestate_filtered)

# ETL: Extract & Transform gate RAM4W16B, and Load into RAM4W16B.txt. Do this because the primary regex pattern misses the RAM4W16B gate, due to savestate data structure irregularity. 
ptn = re.compile('(?s)(RAM4W16B)sr.*?(Inputs:.*?Wires:.*?;)') 

# Append RAM4W16B to output
output.append(re.findall(ptn, savestate_filtered)[0])

# Transfer non-blank indicies from list(output) to list(gates)
gates = []
for idx, val in output:
    if idx != '':
        gates.append((idx, val))

for gate in gates:
    # create file named gate[0].txt
    file = open(gate[0] + '.txt', 'w')
    
    # export gate[1] into gate[0].txt, then close the file.
    file.write(gate[1])
    file.close()

print('EXTRACTION SUCCESSFUL.')
