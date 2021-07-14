# 100-Days-of-Code
___

## Day1

### PROJECT-1 Band Generator name 

```python

print("Welcome to band generator\n")
city =input("Enter the city you grew up\n")
pet_name = input("Enter your pet name\n")
print(city+" "+ pet_name)
```
#### run
##### https://band-name-generator-end.appbrewery.repl.run/
___

## Day2

### PROJECT-2 TIP CALCULATOR
```python
print("welcome to tipcalculator")
bill=int(input("What was total bill$ ?\n"))
tip_percent=float(input("What percentage tip would you like to give 10%, 12% or 15% ?  \n"))
distribution=int(input("How many people to split the bill?\n"))
tip=(bill/distribution)*(1+(tip_percent/100))
ftip= round(tip,2)
print(f"Each person should pay ${ftip}")
```
#### run
###### https://replit.com/@Aristo00071/tip-calculator-start#main.py
___

## Day3

### PROJECT-3 Treasure-ISLAND

```python

                    print('''
                    *******************************************************************************
                              |                   |                  |                     |
                     _________|________________.=""_;=.______________|_____________________|_______
                    |                   |  ,-"_,=""     `"=.|                  |
                    |___________________|__"=._o`"-._        `"=.______________|___________________
                              |                `"=._o`"=._      _`"=._                     |
                     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                    /______/______/______/______/______/______/______/______/______/______/_____ /
                    *******************************************************************************
                    ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
  ```
  #### run
  ##### https://replit.com/@Aristo00071/treasure-island-end#main.py
  ___
  ## Day4

### PROJECT-4 ROCK PAPER SCISSORS
```python
import random

                                        rock = '''
                                            _______
                                        ---'   ____)
                                              (_____)
                                              (_____)
                                              (____)
                                        ---.__(___)
                                        '''

                                        paper = '''
                                            _______
                                        ---'   ____)____
                                                  ______)
                                                  _______)
                                                 _______)
                                        ---.__________)
                                        '''

                                        scissors = '''
                                            _______
                                        ---'   ____)____
                                                  ______)
                                               __________)
                                              (____)
                                        ---.__(___)
                                        '''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
  
```
#### run
##### https://replit.com/@Aristo00071/rock-paper-scissors-start#main.py
___
  ## Day5

### PROJECT-5 Password Generator Project

```python

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)


random.shuffle(password_list)


password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
```
Run
##### https://replit.com/@Aristo00071/password-generator-end#main.py

___
  ## Day6

### PROJECT-6 Automating Robot

>automating robot to find way to reach destination.  
>Please go through https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
___
  ## Day7

### PROJECT-7 Hangman


```python
                               _                                             
                              | |                                            
                              | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                              | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                              | | | | (_| | | | | (_| | | | | | | (_| | | | |
                              |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                                  __/ |                      
                                                 |___/    '''

#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
   
    
```
 ##### https://replit.com/@Aristo00071/Day-7-Hangman-5-End#hangman_art.py
    ___
## Day 8

### PROJECT-8 PASSWORD ENCRYPTER DECRYPTER

```python

                    logo = """           
                     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
                    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
                    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
                    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
                     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                                88             88                                 
                               ""             88                                 
                                              88                                 
                     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
                    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
                    8b         88 88       d8 88       88 8PP""""""" 88          
                    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
                     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                  88                                             
                                  88           
                    """

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""
	if cipher_direction == "decode":
		shift_amount *= -1
	for char in start_text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift_amount
			end_text += alphabet[new_position]
		else:
			end_text += char
	print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)
end=False
while not end:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	shift=shift%26
	caesar(start_text=text, shift_amount=shift,cipher_direction=direction)
	restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
	if restart == "no":
		end=True
		print("Goodbye")
    
```
##### https://replit.com/@Aristo00071/caesar-cipher-4-start#main.py
___
    


