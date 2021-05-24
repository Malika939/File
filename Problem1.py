
d = {"login": "qwer", "password": 1234}
while True:
	a = input('login:')
	b = input('password:')	
	d["login"] = a
	d["password"] = b
	print(d)
	with open("example.txt", 'a') as f:
		f.write(str(d))
