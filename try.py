# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname,'r')
count=0
avg=0.0
cal=0.00 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :        
        continue
    else:
		count=count+1
		pos = line.find(':')
		num=float(line[pos+1:])
		cal=cal+num
		print cal,count
avg=float(cal/count)
print "Average spam confidence : ",avg
