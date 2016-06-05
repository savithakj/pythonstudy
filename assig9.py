name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender=dict();
dir(sender)
word=list();
for line in handle:
	if line.startswith("From"):
		word=line.split()
		print word[1] 
		#print sender.get(word[1],0)
		sender[word[1]]=(sender.get(word[1],0))+1
		#print sender.get(word[1],0)

print sender.items()
        
maxval = None
maxkey = None
for key,val in sender.items() :
#   if maxval == None : maxval = val
  if val > maxval:
      maxval = val
      maxkey = key   

print maxkey, maxval
#print max(sender, key=sender.get)
#print max(sender)
	