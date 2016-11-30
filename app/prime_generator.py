def prime_number(number):
	prime_number=[]
	divisibilty=True
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



        






