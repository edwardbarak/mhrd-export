import codecs
import string
import re

file = codecs.open('savestate', 'r', encoding='utf-8', errors='ignore')
savestate = file.read()
file.close()

printable = set(string.printable)
savestate_cleaned = ''.join(filter(lambda x: x in printable, savestate))

re.findall(ptn, savestate_cleaned)

ptn = re.compile('(?s)([A-Z0-9]*?)sq~pt.*?(Inputs:.*?Wires:.*?;)') # Misses RAM4W16B
gates = re.findall(ptn, savestate_cleaned)

# for gate in gates:
    # create file named gate[0].txt
    # export gate[1] into gate[0].txt

# ETL: Extract & Transform gate RAM4W16B, and Load into RAM4W16B.txt. Do this because the main pattern misses the RAM4W16B gate due to savestate data structure irregularity. 


