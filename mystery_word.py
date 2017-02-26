import random


def word_picker(difficulty_input):
    dictionary = open("/usr/share/dict/words")
    dictionary_list = []
    dictionary_list = dictionary.readlines()
    count = 0
    for word in dictionary_list:
        dictionary_list[count] = word[:-1]
        dictionary_list[count] = dictionary_list[count].lower()
        count += 1
    four_to_six = []
    six_to_eight = []
    eight_plus = []
    if difficulty_input == "1" or "":
        for word in dictionary_list:
            if len(word) >= 4 and len(word.lower()) <= 6:
                four_to_six.append(word)
        return(four_to_six[random.randrange(0, len(four_to_six))])
    elif difficulty_input == "2":
        for word in dictionary_list:
            if len(word) >= 6 and len(word) <= 8:
                six_to_eight.append(word.lower())
                count += 1
            else:
                count += 1
        return(six_to_eight[random.randrange(0, len(six_to_eight))])
    elif difficulty_input == "3":
        for word in dictionary_list:
            if len(word) >= 8:
                eight_plus.append(word.lower())
        return(eight_plus[random.randrange(0, len(eight_plus))])
    else:
        return word_picker(input("Maybe I should be more clear: '1' = EASY '2' = HARD '3' = IMPOSSIBLE: "))


def guessing(secret_word, display_data, bad_guesses, all_guesses):
    guess = input("Guess a letter: ")
    while guess in all_guesses:
        guess = input("You guessed that already, try again: ")
    all_guesses.append(guess)
    count = 0
    found_it = 0
    while count < len(secret_word):
        if (guess == secret_word[count]) and (((count, guess)) not in display_data):
            display_data[count] = ((count, guess))
            count += 1
            found_it = 1
        else:
            count += 1
    if found_it == 0:
        bad_guesses += 1
    return ((display_data, bad_guesses, all_guesses))


def display(display_data, count, display_str, length_secret):
    while count < length_secret:
        display_str += (display_data[count][1] + " ")
        count += 1
    return display_str


def main():
    good_guesses = 0
    bad_guesses = 0
    display_data = []
    all_guesses = []
    playing = True
    while playing:
        good_guesses = 0
        if bad_guesses == 0 and display_data == []:
            secret_word = word_picker(input("1 for easy, 2 for normal, 3 for hard: "))
        # print(secret_word)
        count = 1
        while count <= len(secret_word):
            display_data.append((count, "*"))
            count += 1
        display_data = guessing(secret_word, display_data, bad_guesses, all_guesses)
        bad_guesses = display_data[1]
        all_guesses = display_data[2]
        display_data = display_data[0]
        print("The word so far: " + display(display_data, 0, "", len(secret_word)))
        print("Your Guesses so far: " + str(all_guesses))
        for item in display_data:
            if item[1] != "*":
                good_guesses += 1
        if good_guesses == len(secret_word):
            user_input = input("You win! Play again?(Y,N): ")
            user_input = user_input.lower()
            if user_input == "y":
                main()
            else:
                break
        elif bad_guesses == 8:
            user_input = input("You lose! The secret word was " + secret_word + " Play again(Y,N): ")
            user_input = user_input.lower()
            if user_input == "y":
                main()
            else:
                break


main()
