import random
word_list = ["python", "hangman", "programming", "developer", "algorithm"]
def choose_word():
    return random.choice(word_list)
def display_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])
def hangman():
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time. You have 6 attempts.\n")
    
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    while attempts > 0:

        print("\nWord:", display_progress(word, guessed_letters))
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

hangman()
