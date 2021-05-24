# a = open('python.txt', 'w')
# a.write('''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java''')
# a.close()
d = open('/Users/mac/python.txt', 'r')
t_words =[]
s = (d.read().split())
for x in s:
	if "t" in x:
		t_words.append(x)
	if "T" in x:
		t_words.append(x)
print(t_words)
d.close()