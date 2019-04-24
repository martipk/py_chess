
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
			8-i, l[i][0][0], l[i][1][0], l[i][2][0], l[i][3][0], l[i][4][0], l[i][5][0], l[i][6][0], l[i][7][0]))
		print("      +---+---+---+---+---+---+---+---+")
	print("        A   B   C   D   E   F   G   H\n")



def init_grid():

	lst1 = ["R2", "H2", "B2", "K2", "Q2", "H2", "K2", "R2"]
	lst2 = ["P2", "P2", "P2", "P2", "P2", "P2", "P2", "P2"]
	lst3 = [" ", " ", " ", " ", " ", " ", " ", " "]
	lst4 = [" ", " ", " ", " ", " ", " ", " ", " "]
	lst5 = [" ", " ", " ", " ", " ", " ", " ", " "]
	lst6 = [" ", " ", " ", " ", " ", " ", " ", " "]
	lst7 = ["P1", "P1", "P1", "P1", "P1", "P1", "P1", "P1"]
	lst8 = ["R1", "H1", "B1", "Q1", "K1", "B1", "H1", "R1"]

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


def move_piece(move_tpls, lst, player):

	src_piece = lst[move_tpls[0][0]][move_tpls[0][1]][:]
	# dest_piece = lst[move_tpls[1][0]][move_tpls[1][1]]
	print(move_tpls)

	if (src_piece != ' ') and is_your_piece(src_piece[1], player) \
	and is_legal_move(src_piece, move_tpls):
		print("Moving Piece: " + src_piece[0])
		lst[move_tpls[1][0]][move_tpls[1][1]] = src_piece
		lst[move_tpls[0][0]][move_tpls[0][1]] = ' '
		return 0
	return -1


def is_your_piece(turn, player):
	return (int(turn) == player)


def is_legal_move(piece, tuples):
	if piece[0] == 'R':
		if (tuples[0][0] == tuples[1][0]) or (tuples[0][1] == tuples[1][1]):
			# check if anything is in the way
			return True

	elif piece[0] == 'H':
		if ((abs(tuples[0][0] - tuples[1][0]) == 2) and (abs(tuples[0][1] - tuples[1][1]) == 1)) or \
		((abs(tuples[0][0] - tuples[1][0]) == 1) and (abs(tuples[0][1] - tuples[1][1]) == 2)):
			return True

	elif piece[0] == 'P':
		if piece[1] == '1':
			if (tuples[0][1] == tuples[1][1]): # check if verticle movement
				if (tuples[1][0] == tuples[0][0] - 1): # check if move by one
					return True
				else:
					if (tuples[0][0] == 6) and (tuples[1][0] == (tuples[0][0] - 2)):
						return True

		else:
			if (tuples[0][1] == tuples[1][1]): # check if verticle movement
				if (tuples[1][0] == tuples[0][0] + 1): # check if move by one
					return True
				else:
					if (tuples[0][0] == 1) and (tuples[1][0] == (tuples[0][0] + 2)):
						return True
		# make diagonal taking



	print("Illegal Move")
	return False


def play_game(board_lst):

	player = 1

	while 1:
		print_board(board_lst)
		print("PLAYER {}'S TURN:\n".format(player))

		move = check_format_and_get_index(input("Enter Move (format: 'D2 D4'):")) 
		if move == -1:
			print("Wrong format, try again.")
			continue
		if move_piece(move, board_lst, player) == -1:
			print("Piece '{}' cannot be moved, or does not exits.".format(board_lst[move[0][0]][move[0][1]][0]))
			continue

		if player == 1:
			player = 2
		else:
			player = 1


if __name__ == '__main__':

	print_init()
	play_game(init_grid())

