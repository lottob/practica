import os
import random
from urllib import request

if not os.path.isfile('sgb-words.txt'):
    request.urlretrieve(
        "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt", "sgb-words.txt"
    )

with open("sgb-words.txt") as word_list:
    five_letter_words = word_list.readlines()

word = random.choice(five_letter_words)
total_chances_left = 5

while True:
    if total_chances_left == 0:
        print("Suerte para la proxima!")
        print(f"La palabra era: {word}")
        break
    j = 0
    guess = input("Ingrese una palabra de 5 caracteres: ")
    if guess == word:
        print('π©π©π©π©π©')
        print('Ganaste!!!')
        break
    elif len(guess) == 5:
        grid = {i: 'β¬' for i in range(5)}
        count = {i: 0 for i in set(guess)}
        for i in guess:
            count[i] += 1
            if i == word[j]:
                grid[j] = 'π©'
            elif i in word and word.count(i) >= count[i]:
                grid[j] = 'π¨'
            j += 1
        print("".join(grid.values()))
        total_chances_left -= 1
    else:
        print("Ingrese una palabra vΓ‘lida de 5 letras o que no lleve numeros.")
    print(f"Total de intentos: {total_chances_left}")
