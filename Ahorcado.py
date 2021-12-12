# Programa del ahorcado

import random
import os

def run():
       
    DB = ["JAVA","PYTHON","LUA","RUST","C","BASH","PHP"]
    IMAGENES = ['''
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
    
    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6
    dibujo = 0

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(IMAGENES[dibujo])
        letter = input("Elige una letra: ").upper()
    
        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
            
        if not found:
            attemps -= 1
            dibujo += 1
        
        if "_" not in spaces:
            os.system("cls")
            print("\n\nYOU WIN !!!\n\n\n\n")
            break
            input()
        
        if attemps == 0:
            os.system("cls")
            print("\n\nYOU LOOSE !!!\n\n\n\n")
            break
            input()
        
if __name__ == '__main__':
      run()
    
