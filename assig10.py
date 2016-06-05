name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time=dict()
for line in handle:
	if line.startswith("From") and not line.startswith("From:") :
		pos=line.find(":")
		#print line
		hr=line[pos-2:pos]
		#print hr
		time[hr]=(time.get(hr,0))+1
		
lst = list()
for key, val in time.items():
        lst.append((key,val))
lst.sort()
for val,key in lst:
        print val,key