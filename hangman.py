import random
from termcolor import colored

print(colored('''
      ___           ___           ___           ___           ___           ___           ___     
     /\  \         /\  \         /\  \         /\__\         /\  \         /\  \         /\  \    
     \:\  \       /::\  \        \:\  \       /:/ _/_       |::\  \       /::\  \        \:\  \   
      \:\  \     /:/\:\  \        \:\  \     /:/ /\  \      |:|:\  \     /:/\:\  \        \:\  \  
  ___ /::\  \   /:/ /::\  \   _____\:\  \   /:/ /::\  \   __|:|\:\  \   /:/ /::\  \   _____\:\  \ 
 /\  /:/\:\__\ /:/_/:/\:\__\ /::::::::\__\ /:/__\/\:\__\ /::::|_\:\__\ /:/_/:/\:\__\ /::::::::\__\
 \:\/:/  \/__/ \:\/:/  \/__/ \:\~~\~~\/__/ \:\  \ /:/  / \:\~~\  \/__/ \:\/:/  \/__/ \:\~~\~~\/__/
  \::/__/       \::/__/       \:\  \        \:\  /:/  /   \:\  \        \::/__/       \:\  \      
   \:\  \        \:\  \        \:\  \        \:\/:/  /     \:\  \        \:\  \        \:\  \     
    \:\__\        \:\__\        \:\__\        \::/  /       \:\__\        \:\__\        \:\__\    
     \/__/         \/__/         \/__/         \/__/         \/__/         \/__/         \/__/    
''',"green"))

words = ["dictionary", "refrigerator", "javascript", "beautiful", "excellent", "programming", "difficult", "impossible",
         "champion", "amazing", "extraordinary", "wonderful", "fantastic", "marvelous", "spectacular", "magnificent",
         "splendid", "remarkable", "superb", "delightful", "terrific", "glorious", "impressive", "stupendous",
         "outstanding", "sensational", "extraordinary", "superlative", "formidable", "enchanting", "captivating",
         "engrossing", "absorbing", "riveting", "gripping", "thrilling", "exciting", "mesmerizing", "hypnotizing",
         "bewitching", "spellbinding", "beguiling", "alluring", "entrancing", "glamorous", "gorgeous", "handsome",
         "lovely", "pleasant", "pleasing"]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
key = random.choice(words)
magic_word = list(key)

game_set = ["_" for i in range(len(magic_word))]
print(game_set)
gameon = True
count = 0
while gameon:
    if count == 7:
        print("Game Over")
        print(f"The Word was {key}")
        break

    letter = input("Guess a letter to play:: ")
    if letter in magic_word:
        if letter in game_set:
            print(HANGMANPICS[count])
            count += 1

        for i in magic_word:
            if i == letter:
                index = magic_word.index(i)
                game_set[index]=letter
                print(game_set)
        if "_" not in game_set:
            print("Congratulations! You have won the game.")
            print(f"The word was {key}")
            gameon = False
        else:
            print("".join(game_set))
    else:
        print(HANGMANPICS[count])
        count += 1
