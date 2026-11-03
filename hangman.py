import random

# Step 1: Create word list and select a word
words = ["srinu", "padma", "mounika", "dileep", "python"]
word = random.choice(words)

# Step 2: Display hidden letters
display = ["_"] * len(word)
print(" ".join(display))

wrong_guesses = 0
guessed_letter = []

stages =["""
        +---+
        |   |  
            |
            |
            |
      =========     
        """
           ,
        """
       +---+
       |   |
       o   |
           |
           |
      =========  
        """
           ,
        """
       +---+
       |   |
       O   |
       |   |
           |
      =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
      =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\ |
           |
      =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\ |
      /    |
      =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\ |
      / \\ |
      =========
    """
]        
    

while "_" in display and wrong_guesses<6:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letter:
        print("You already guessed this letter!")
        continue

    guessed_letter.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("wrong guess!")
        print("attempts used:",wrong_guesses)
        print(stages[wrong_guesses])

    for i in range(len(word)):
        if word[i] == guess:
           display[i] = guess

    print(" ".join(display))

if "_" not in display:
    print("congratulation! you won!")
else:
    print("Game over! and loss game")
    print("the word was:",word)

