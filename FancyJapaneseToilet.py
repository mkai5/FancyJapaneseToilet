import os

class FancyJapaneseToilet:


	def handle_input(all):
		seat = all[0]
		bidet = all[1]
		heat = all[2]
		print("_______________________________________________________________________________________\n")
		print("This is a fancy Japanese toilet...")
		if (seat):
			print("The seat is up.")
		if (bidet==1):
			print("The bidet is on:")
			print("squirt")
		elif (bidet==2):
			print("The bidet is on high:")
			print("squirtsquirtsquirtsquirtsquirtsquirtsquirtsquirtsquirtsquirtsquirtsquirtsquirtsquirt")
		if (heat):
			print("The seat is hot.")
		str_in = input()
		str_list = str_in.split()
		for s in str_list:
			if (s.isspace() or s==""):
				pass
			elif (s == "bidet"):
				bidet = bidet + 1
				if (bidet == 3):
					bidet = 0
			elif (s == "warmer" or s == "heat"):
				heat = not heat
			elif (s == "seat"):
				seat = not seat
			elif (s == "flush"):
				print("wooooooooooooooosh...")
			elif (s == "music"):
				print ("do do do do dooo dooo do do do! ding ding!")
			elif (s == "exit"):
				exit()
			else:
				print ("There's no %s button." % s)
		return [seat,bidet,heat]

	clear = lambda: os.system('cls')
	clear()
	n = handle_input([False, 0, False])
	while (True):
		n = handle_input(n)
