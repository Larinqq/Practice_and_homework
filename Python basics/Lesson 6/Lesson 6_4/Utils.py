import random


def get_words(data_file):
    """
    Reads given file with words and returns a list of words
    :param data_file: file path
    :return: list of words
    """
    with open(data_file, "r") as data:
        file_content = data.read().rstrip("\n").split("\n")
        random.shuffle(file_content)
        return file_content


def get_shuffled_word(word_to_shuffle):
    """
    Shuffles letters in given word
    :param word_to_shuffle: string
    :return: shuffled word
    """
    letter_list = list(word_to_shuffle)
    random.shuffle(letter_list)
    result = "".join(letter_list)
    return result


def get_statistics(file_to_read):
    """
    Reads a file with stats, counts played games and high score
    :return: a tuple game_played (int), high_score (int)
    """
    game_played = 0
    high_score = 0
    with open(file_to_read, "r") as data:
        for line in data:
            game_played += 1
            score = int(line.split(":")[1])
            if score > high_score:
                high_score = score

    return game_played, high_score


def save_scores(file_to_write, name, score):
    """
    Writes statistics to file.
    :param file_to_write: path to file
    :param name: user's name
    :param score: user's score
    :return: nothing
    """
    with open(file_to_write, "a") as data:
        data.write(f"{name}:{score}\n")
