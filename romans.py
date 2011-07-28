class NotRomanNumber (Exception):
	pass

def romans(number):
	"""
	>>> romans('I')
	1
	>>> romans('II')
	2
	>>> romans('III')
	3
	>>> romans('IV')
	4
	>>> romans('V')
	5
	>>> romans('C')
	100
	>>> romans('VI')
	6
	>>> romans('X')
	10
	>>> romans('L')
	50
	>>> romans('IX')
	9
	>>> romans('XIV')
	14
	>>> romans('XC')
	90
	>>> romans('XL')
	40
	>>> romans('')
	Traceback (most recent call last):
        ...
	NotRomanNumber
	"""
	if not number:
		raise NotRomanNumber()
		
	look_up = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100
	}

	if len(number) == 1:
		return look_up[number]
	elif romans(number[0]) < romans(number[1]) :
		return romans (number[1:]) - romans(number[0])
	return romans(number[0]) + romans(number[1:])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.master.summarize() 
