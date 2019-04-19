

def print_init():

	print("\n")
	print("&&&&&&& &&   && &&&&&&& &&&&&&& &&&&&&&")
	print("&&      &&   && &&      &&      &&     ")
	print("&&      &&&&&&& &&&&&   &&&&&&& &&&&&&&")
	print("&&      &&   && &&           &&      &&")
	print("&&&&&&& &&   && &&&&&&& &&&&&&& &&&&&&&")
	print("                                    by martipk on GitHub\n")


def print_board(l):

	print("      +---+---+---+---+---+---+---+---+")
	for i in range(0,8):
		print("    {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(\
			8-i, l[i][0], l[i][1], l[i][2], l[i][3], l[i][4], l[i][5], l[i][6], l[i][7]))
		print("      +---+---+---+---+---+---+---+---+")
	print("        A   B   C   D   E   F   G   H\n")



def init_grid():

	lst1 = ["R", "K", "B", "K", "Q", "B", "K", "R"]
	lst2 = ["P", "P", "P", "P", "P", "P", "P", "P"]
	lst3 = [" ", " ", " ", " ", " ", " ", " ", " "]
	lst4 = lst3[:]
	lst5 = lst3[:]
	lst6 = lst3[:]
	lst7 = lst2[:]
	lst8 = ["R", "K", "B", "Q", "K", "B", "K", "R"]

	lst = [lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8]

	return lst

# def check_format_move(s):



def play_game(lst):

	player = 1
	# while 1:
		# move = check_format_move(input("Enter Move (format: 'D2 D4'):")) 
		# if move == -1:
		# 	print("Wrong format, try again.")
		# 	continue



if __name__ == '__main__':
	print_init()
	print_board(init_grid())
	play_game(init_grid())

