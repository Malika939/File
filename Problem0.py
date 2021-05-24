dir = open('/Users/mac/Desktop/derictories.txt', 'w')
dir.write('''Applications       Volumes         etc             sbin
Library         bin             home            tmp
System          cores           opt             usr
Users           dev             private         var''')
dir.close()