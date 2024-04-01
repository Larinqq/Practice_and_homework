from Config import WORDS_FILE_PATH, STATISTICS_FILE_PATH
from Utils import get_words, get_shuffled_word, get_statistics, save_scores


if __name__ == '__main__':
    users_score = 0
    print("Enter your name: ")
    user_name = input(">")
    content = get_words(WORDS_FILE_PATH)
    for word in content:
        shuffled_word = get_shuffled_word(word)
        print(f"Guess the word: {shuffled_word}")
        users_guess = input().lower()
        if users_guess == word.lower():
            users_score += 10
            print("Correct! You earn 10 points!\n")
        else:
            print(f"Wrong! The answer is {word}\n")

    save_scores(STATISTICS_FILE_PATH, user_name, users_score)
    games_played, max_score = get_statistics(STATISTICS_FILE_PATH)
    print(f"\nTotal games played: {games_played} \nHigh score: {max_score}")
