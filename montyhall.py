import sys
import stdio
import random

n = int(sys.argv[1])
c = 0
stay = 0
change = 0

while c < n:

	player = random.randrange(3)
	game = random.randrange(3)
	reveal = random.randrange(3)
	while reveal == player or reveal == game:
		reveal = random.randrange(3)
	switch = 3 - reveal - player

	if game == switch:
		change = change + 1
	else:
		stay = stay + 1
	
	c = c + 1

stayAve = stay / c
changeAve = change / c
stdio.write("Stay   -- ")
stdio.writeln(stayAve)
stdio.write("Change -- ")
stdio.writeln(changeAve)