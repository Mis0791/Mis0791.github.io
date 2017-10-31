import random 

def cointoss(num):
	heads = 0;
	tails = 0;

	for x in range(1, num + 1): 
		rnum = random.randint(1, 2)
		if rnum == 1:
			heads += 1
			print "Attempt #", x, ": Throwing a coin... It's a head! ... Got " , heads , "head(s) so far and " , tails , "tail(s) so far"
		else: 
			tails += 1
			print "Attempt #", x , ": Throwing a coin... It's a tail! ... Got " , heads , "head(s) so far and " , tails, "tail(s) so far"

cointoss(3)