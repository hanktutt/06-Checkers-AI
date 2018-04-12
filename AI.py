#!/usr/bin/python
import random
class AI:
	def __init__(self, player):
		self.player = player

	def choose_piece(self, board, pieces, opponents):
		'''
		By whatever criteria you choose, select a piece to move. You will need to return the piece and its available jumps
		'''
		squares = board.get_squares()
		for p in pieces:
			if p.alive:
				jumps = p.check_jump(pieces + opponents, squares)
				if len(jumps):
					return (p, jumps)
		can_move = []
		for p in pieces:
			if p.alive:
				jumps = p.get_valid_possibilities(squares, pieces + opponents)
				if len(jumps):
					can_move.append(p)
		if len(can_move):
			p= random.choice(can_move)
			jumps = p.get_valid_possibilities(squares, pieces + opponents)
			return (p, jumps)
		return (p, [])

	def move_piece(self, piece, board, pieces, opponents):
		'''
		Move the piece to its new location
		'''
		squares = board.get_squares()
		jumps = piece.check_jump(pieces + opponents, squares)
		print(piece.position)
		print(jumps)
		if len(jumps):
			j = random.choice(jumps)
			j['piece'].alive = False
			(row, column) = j['position']
			piece.move(row, column)
			jumps = []
		else:
			jumps = piece.get_valid_possibilities(squares, pieces + opponents)
			# move the piece
			if len(jumps):
				(row, column) = jumps[0]
				piece.move(row, column)
				jumps = []
				# get any new jumps (i.e., double-jumps)

		return (piece, jumps, pieces, opponents)