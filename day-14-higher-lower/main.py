from game_data import data
from art import logo,vs
import random
from replit import clear



def randm_account():
	return random.choice(data)


def format_descp(account_data):
	name=account_data['name']
	des=account_data['description']
	country=account_data['country']
	return f"{name}, a {des}, from {country}"


def check_winner(a ,b):
	if a>b:
		return 'a'
	else:
		return 'b'




def game():
	print(logo)


	game_cont=True
	score=0
	while(game_cont):
		first_ac=randm_account()
		sec_ac=randm_account()


		followerA=first_ac["follower_count"]
		followerB=sec_ac["follower_count"]


		formated_fst=format_descp(first_ac)
		formated_seec=format_descp(sec_ac)

		print(f"Compare A: {formated_fst}")
		print(vs)
		print(f"Against B: {formated_seec}")
		

		get_input=(input("Who has more followers? Type 'A' or 'B':")).lower()
		get_winner=check_winner(followerA,followerB)
		clear()
		print(logo)
		if get_input==get_winner:
			score+=1
			print(f"You're right! Current score: {score}.")
		else:
			print(f"Sorry, that's wrong. Final score: {score}")
			game_cont=False
		

game()
