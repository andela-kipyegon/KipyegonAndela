def prime_number(number):
	prime_number=[]
	divisibilty=True
        if (isinstance(number, tuple)):
                return 'Invalid tuple Argument'
        if (isinstance(number, float)):
                return 'Invalid Float Argument'
	if (isinstance(number, list)):
                return 'Invalid list Argument'
        if (isinstance(number, dict)):
                return 'Invalid dict Argument'
        if (isinstance(number, str)):
                return 'Invalid string Argument'
        if number > 0:
                for  i in range(2,(number+1)):
                        divisibilty=True
                        for j in range (2,i):
                                if (i%j==0):
                                        divisibilty =False
                        if divisibilty:
                                prime_number.append(i)
                return prime_number
        else:
                return 'Only positive numbers'







