import codecs
import string
# import re

file = codecs.open('savestate', 'r', encoding='utf-8', errors='ignore')
savestate = file.read()
file.close()

printable = set(string.printable)
ssClean = ''.join(filter(lambda x: x in printable, savestate))

ptn = re.compile('ppt\t?(.*?)sq~')
re.findall(ptn, ssClean)

fa = re.compile('ppt.*?^[A-Z]([A-Z]*?)sq~pt'); re.findall(fa, ssClean)



