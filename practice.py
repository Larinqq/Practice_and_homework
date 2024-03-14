import random


def morse_encode(sentense):
    encoded_word = ""
    morse_table = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }

    for letter in sentense:
        encoded_word += morse_table[letter]

    return encoded_word


def get_word():
    words = ["cat", "dog", "boy", "margo"]
    random_word = random.choice(words)
    return random_word


def print_statistics(data:list):
    answers_counter = len(data)
    right_answers = 0
    for elem in data:
        if elem:
            right_answers += 1
    wrong_answers = answers_counter - right_answers
    print(f"All task: {answers_counter}\n Right answers: {right_answers}\n Wrong answers {wrong_answers}")


if __name__ == '__main__':
    greating = " Today we gonna practice to encode morse code\n Press Enter to continue\n"
    total_questions = 5
    question = 0
    print(greating)
    input()
    answers_list = []

    while question < total_questions:
        question +=1
        current_word = get_word()
        morse_code = morse_encode(current_word)
        print(f"Word {question}: {morse_code}\n User's answer >>>")
        users_answer = input().lower()
        if users_answer == current_word:
            print(f"Rihgt, {current_word}")
            answers_list.append(True)
        else:
            print(f"Wrong, {current_word}")
            answers_list.append(False)

    print_statistics(answers_list)