import streamlit as st
import random

# List of words for the game
words = ["python", "streamlit", "hangman", "programming", "development"]
word_to_guess = random.choice(words)
guessed_letters = []
attempts = 6

# Streamlit app layout
st.title("Hangman Game")
st.write("Guess the word!")

# Display the current state of the word
display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
st.write(display_word)

# Input for guessing a letter
guess = st.text_input("Enter a letter:", max_chars=1).lower()

if guess:
    if guess in guessed_letters:
        st.warning("You've already guessed that letter!")
    elif guess in word_to_guess:
        guessed_letters.append(guess)
        st.success("Good guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        st.error("Wrong guess! Attempts left: {}".format(attempts))

# Check for win or loss
if all(letter in guessed_letters for letter in word_to_guess):
    st.success("Congratulations! You've guessed the word: {}".format(word_to_guess))
elif attempts <= 0:
    st.error("Game Over! The word was: {}".format(word_to_guess))

# Display guessed letters
st.write("Guessed letters: ", ' '.join(guessed_letters))
