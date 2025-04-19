# Assisting system: Guesser v1.1

def hint1(num):
    if num % 2 == 0:

        print("First Hint : The number is even.")

    else:

        print("First Hint : The number is odd.")



def hint2(num):
	if len(str(num)) == 1:
		print("Second Hint : The number is 1 digit long.")

	elif len(str(num)) == 2:
		print("Second Hint : The number is 2 digits long.")

	

