import turtle
import random
from turtle import Turtle 
def start_game():

	turtle.goto(0,0)
	turtle.left(90)
	turtle.shape("triangle")
	turtle.shapesize(10)
	turtle.hideturtle()

def play_game():

	player_1="Q"
	player_2="C"
	player_3="N"
	player_4="P"

	#wait random time
	turtle.showturtle()
	#loop thrue all players if they win
	i=0
	while RUNNUNG:
		if turtle.onkeypress(Q):
			player_1.score=i+1
			player_1.score=i
		if turtle.onkeypress(C):
			player_2.score=i+1
			player_2.score=i
		if turtle.onkeypress(N):
			player_3.score=i+1
			player_3.score=i
		if turtle.onkeypress(P):
			player_4.score=i+1
			player_4.score=i
		#turtle.listen()
	return winner

start_game()
turtle.mainloop()




# pygame.event.pump()
#     keys = pygame.key.get_pressed()
  
#     if keys[pygame.K_p]:
#         player_1.score=i+1
# 		player_1.score=i

#     if keys[pygame.K_c]:
#         player_2.score=i+1
# 		player_2.score=i

#     if keys[pygame.K_n]:
#         player_3.score=i+1
# 		player_3.score=i

#     if keys[pygame.K_p]:
#         player_4.score=i+1
# 		player_4.score=i