
LETTERS = "ABCDEFGH  abcdefgh"
DIGITS = "123456789"

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


def check_format_and_get_index(s):

	src = -1
	dest = -1

	try:
	    s1, s2 = s.split(" ")
	except ValueError:
	    return -1

	if (s1 == "") or (s2 == ""):
		return -1

	if (s1[0] in LETTERS and s1[1] in DIGITS) and (s2[0] in LETTERS and s2[1] in DIGITS):

		tpl = (s1, s2)

		for i in range(len(LETTERS)):
			if tpl[0][0] == LETTERS[i]:
				src = (8 - int(tpl[0][1]), i % 10)

		for j in range(len(LETTERS)):
			if tpl[1][0] == LETTERS[j]:
				dest = (8 - int(tpl[1][1]), j % 10)

	if src == -1 or dest == -1:
		return -1
	return (src, dest)


def move_piece(move_tpls, lst):

	src_piece = lst[move_tpls[0][0]][move_tpls[0][1]][:]
	# dest_piece = lst[move_tpls[1][0]][move_tpls[1][1]]
	
	if (src_piece != ' '):
		print("Moving Piece: " + src_piece)
		lst[move_tpls[1][0]][move_tpls[1][1]] = src_piece
		lst[move_tpls[0][0]][move_tpls[0][1]] = ' '
		return 0
		
	return -1


def play_game(board_lst):

	player = 1

	while 1:
		print_board(board_lst)

		move = check_format_and_get_index(input("Enter Move (format: 'D2 D4'):")) 
		if move == -1:
			print("Wrong format, try again.")
			continue
		if move_piece(move, board_lst) == -1:
			print("Piece '{}' cannot be moved there, or does not exits.".format(board_lst[move[0][0]][move[0][1]]))




if __name__ == '__main__':

	print_init()
	play_game(init_grid())

