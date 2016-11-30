def prime_number(number):
	prime_number=[]
	divisibilty=True
	if (isinstance(number, complex)):
                return 'Invalid Argument'
        if (isinstance(number, tuple)):
                return 'Invalid Argument'
        if (isinstance(number, float)):
                return 'Invalid Argument'
	if (isinstance(number, list)):
                return 'Invalid Argument'
        if (isinstance(number, dict)):
                return 'Invalid Argument'
        if (isinstance(number, str)):
                return 'Invalid Argument'
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



        






