try:
	at = 10
	in = 15
	wo = 20
	for e in range(-at, at):
		print(wo / e)
	if at > '5':
		print("at > 5")
except SyntaxError:
	print("Syntax Error")
except ZeroDivisionError:
	print("Zero Division Error")