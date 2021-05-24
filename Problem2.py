a = open('text.txt', 'w')
a.write("qerqr st sery sery sety esry st srty sty srtys rty srty sr")
a.close()
b = open('text.txt', 'r')
if 'w' in b.read():
	print("Da")
else:
	print("Net")