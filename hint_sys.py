from hints import hint1
from hints import hint2


def hintsys(dif, attempts, num):

	if dif == 1: # 10 Chances

		if attempts == 5:
			a = input("Do you need a hint? (Y/N) : ").lower()
			if a == "y":
				hint1(num)
			
		elif attempts == 2:
			b = input("Do you need a hint? (Y/N) : ").lower()
			if b == "y":
				hint2(num)
		

	elif dif == 2: # 5 Chances

		if attempts == 3:
			aone = input("Do you need a hint? (Y/N) : ").lower()
			if aone == "y":
				hint1(num)
		elif attempts == 1:
			bone = input("Do you need a hint? (Y/N) : ").lower()
			if bone == "y":
				hint2(num)

	elif dif == 3: # 3 Chances

		if attempts == 1:
			atwo = input("Do you need a hint? (Y/N) : ").lower()
			if atwo == "y":
				hint1(num)