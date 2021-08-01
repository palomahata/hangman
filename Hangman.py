import random
def get_word():
lista_palavras = ['gata', 'cão', 'lagarto', 'centopéia', 'boi']
word = random.choice(lista_palavras)
return word.upper()

def play(word):
word_completion = "_" * len(word)
guessed = False
guessed_letters = []
guessed_words = []
tries = 6
print(f"JOGO DA FORCA!\nDica: {len(word)} letras!")
print(display_hangman(tries))
print(word_completion)
print("\n")
while not guessed and tries > 0:
guess = input("Adivinhe uma letra ou palavra: ").upper()
if len(guess) == 1 and guess.isalpha():
if guess in guessed_letters:
print("Você já tentou ", guess)
elif guess not in word:
print(guess, "Não.")
tries -= 1
guessed_letters.append(guess)
else:
print(guess, "está na palavra!")
guessed_letters.append(guess)
word_as_list = list(word_completion)
indices = [i for i, letter in enumerate(word) if letter == guess]
for index in indices:
word_as_list[index] = guess
word_completion = "".join(word_as_list)
if "_" not in word_completion:
guessed = True
elif len(guess) == len(word) and guess.isalpha():
    if guess in guessed_words:
print("Você já tentou a palavra", guess)
elif guess != word:
print(guess, "não é a palavra.")
tries -= 1
guessed_words.append(guess)
else:
guessed = True
word_completion = word
else:
print("Inválido.")
print(display_hangman(tries))
print(word_completion)
print("\n")
if guessed:
print("Parabéns, você adivinhou a palavra! Você venceu!")
else:
print("Você perdeu!. A palavra era " + word + ".")
def display_hangman(tries):
stages = [ # cabeça, tronco e braços e pernas: morte.
"""
--------
| |
| O
| \|/
| |
| / \
-
""",
# cabeça, tronco e braços, perna
"""
--------
| |
| O
| \|/
| |
| /
-
""",
# cabeça, tronco e braços

"""
--------
| |
| O
| \|
| |
|
-
""",
# cabeça e tronco
"""
--------
| |
| O
| |
| |
|
-
""",
# cabeça
"""
--------
| |
| O
|
|
|
-
""",
# vazio
"""
--------
| |
|
|
|
|
-
"""
]
return stages[tries]

def main():
word = get_word()
play(word)
while input("Jogar de novo? (S/N) ").upper() == "S":
word = get_word()
play(word)
if __name__ == "__main__":
main()
JOGO DA FORCA!
Dica: 7 letras!
--------
| |
|
|
|
|
-
_______
Adivinhe uma letra ou palavra: a
A está na palavra!
--------
| |
|
|
|
|
-
_A_A___
Adivinhe uma letra ou palavra: c
C Não.
--------
| |
| O
|
|
|
-
_A_A___
Adivinhe uma letra ou palavra: z
Z Não.
--------
| |
| O
| |
| |
|
-
_A_A___
Adivinhe uma letra ou palavra: t
T está na palavra!
--------
| |
| O
| |
| |
|
-
_A_A_T_
Adivinhe uma letra ou palavra: o
O está na palavra!
--------
| |
| O
| |
| |
|
-
_A_A_TO
Adivinhe uma letra ou palavra: h
H Não.
--------
| |
| O
| \|
| |
|
-
Análise de Dados: overview
-
_A_A_TO
Adivinhe uma letra ou palavra: d
D Não.
--------
| |
| O
| \|/
| |
|
-
_A_A_TO
Adivinhe uma letra ou palavra: lagarto
--------
| |
| O
| \|/
| |
|
-
LAGARTO
Parabéns, você adivinhou a palavra! Você venceu!
Jogar de novo? (S/N) n
