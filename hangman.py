import random
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
magic_word= random.choice(words)
magic_word=magic_word.split()
game_set=["_" for i in range(len(magic_word))]
gameon=True
while gameon:



