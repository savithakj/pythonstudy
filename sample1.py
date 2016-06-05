fhand = raw_input('Enter the file name: ')
while True:
    try:
        var_text = open('C:\Users\Savitha\Desktop\%s' % (fhand), 'r')
        for line in var_text:
            line = line.rstrip()
            if not '@uct.ac.za' in line:
                continue
            print line
            
    except:
        print 'Not Found'
        fhand = raw_input('Enter the file name: ')
        continue
        
    quit()