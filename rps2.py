from random import choice 

computer_score = 0
human_score = 0

print "Hello challenger, I am the champion of RPS, Let's Play. Press r for rock, p for paper, and s for scissors"

def rock_paper_scissors(s, computer_score, human_score): 
	
	x = choice("rps")

	if move == "r" and x == "p":
		print "I play paper!"
		print "I win!"
		return computer_score + 1, human_score

	elif move == "r" and x == "r":
		print "I play rock!"
		print "We draw!"
		return computer_score, human_score

	elif move == "r" and x == "s":
		print "I play scissors!"
		print "You win!"
		return computer_score, human_score + 1

	elif move == "p" and x == "p":
		print "I play paper!"
		print "We draw!"
		return computer_score, human_score

	elif move == "p" and x == "r":
		print "I play rock!"
		print "You win!"
		return computer_score, human_score + 1

	elif move == "p" and x == "s":
		print "I play scissors!"
		print "I win!"
		return computer_score + 1, human_score

 	elif move == "s" and x == "s":
		print "I play scissors!"
		print "We draw!"
		return computer_score, human_score

	elif move == "s" and x == "p":
		print "I play scissors!"
		print "You win!"
		return computer_score, human_score + 1

	elif move == "s" and x == "r":
		print "I play scissors!"
		print "I win!"
		return computer_score + 1, human_score

	else:
		return "shouldn't be here"

move = raw_input ("Make your move (r,p,s) or q to quit: ")
	

while move != "q":
	human_score, computer_score = rock_paper_scissors(move, human_score, computer_score)
	print human_score, computer_score
	move = raw_input("Make your move (r, p, s) or q to quit: ")

print "Final Score is Computer: %d, You %d" % (computer_score, human_score)

print "Good Game"