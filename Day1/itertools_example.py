import sys 
from itertools import groupby

data = sys.argv[1]

groups = []
for k, g in groupby(data, None):
    groups.append(list(g))      # Store group iterator as a list

output = []
for lst in groups:
	tpl = (len(lst),int(lst[0]))
	output.append(tpl)

print (str(output).strip('[]'))