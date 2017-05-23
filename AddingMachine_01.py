import datetime

print("Type 'clear' to clear memory and start over, and 'end' to quit.\n\n")

sumthing = 0

def catchUpCheckbook():
	global sumthing
	x = input('>> ')
	if x == 'end':
		Goodbye()
	elif x == 'clear':
		ClearAll()
	else:
		x = eval(x)
		x = float(x)
		badass = x
		badass = float(badass)
		hotass = sumthing
		hotass = float(hotass)
		yogiBear = open('AddingMachineTape.txt','a')
		sumthing = x + sumthing
		print('{:.2f}'.format(sumthing))
		yogiBear.write('{:.2f} + ({:.2f}) = {:.2f}\n'.format(hotass, badass, sumthing))
		yogiBear.close()
		solidLoop()

def solidLoop():
	catchUpCheckbook()

def Goodbye():
	f = open('AddingMachineTape.txt','a')
	hhh = '***** {:%Y%m%d%H%M} '.format(datetime.datetime.today())
	separator = (25 * '*') + '\n'
	f.write(hhh + separator)
	f.close()
	print('bye!')

def ClearAll():
	global sumthing
	sumthing = 0
	f = open('AddingMachineTape.txt','a')
	hhh = '***** {:%Y%m%d%H%M} '.format(datetime.datetime.today())
	separator = (25 * '*') + '\n'
	f.write(hhh + separator)
	f.close()
	catchUpCheckbook()

solidLoop()
