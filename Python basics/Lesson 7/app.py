from config import QUESTIONS_FILE_PATH, STAT_FILE_PATH, GREETING_MESSAGE, WRONG_INPUT_MESSAGE, RIGHT_ANSWER_MESSAGE, WRONG_ANSWER_MESSAGE, TOTAL_QUESTIONS, QUESTION_MESSAGE, REAL_ANSWER_MESSAGE, CURRENT_SCORE_MESSAGE, CONTINUE_MESSAGE, FINISH_MESSAGE, CORRECT_ANSWER_COUNTER_MESSAGE, INCORRECT_ANSWER_COUNTER_MESSAGE, SCORE_MESSAGE
from utils import questions_load, draw_gamescreen, get_question, get_answer, split_user_input, verify_user_data, save_statistics, get_points


def main():

    questions_dict = questions_load(QUESTIONS_FILE_PATH)
    user_points = 0
    correct_answer = 0
    incorrect_answer = 0

    for _ in range(TOTAL_QUESTIONS):
        while True:
            print(GREETING_MESSAGE)
            print(draw_gamescreen(questions_dict))
            user_input = split_user_input(input())
            if not verify_user_data(user_input, questions_dict):
                print(f"{WRONG_INPUT_MESSAGE} {CONTINUE_MESSAGE}")
                input()
                print("\033[H\033[J", end="")
            else:
                break

        question_asked = get_question(user_input, questions_dict)
        question_answer = get_answer(user_input, questions_dict)
        print(f"{QUESTION_MESSAGE}{question_asked}")
        user_answer = input().lower()
        question_points = get_points(user_input)

        print("\033[H\033[J", end="")

        if user_answer == question_answer:
            user_points += question_points
            correct_answer += 1
            print(f"{RIGHT_ANSWER_MESSAGE}{question_points}")
            print(f"{CURRENT_SCORE_MESSAGE}{user_points}")
        else:
            user_points -= question_points
            incorrect_answer += 1
            print(f"{WRONG_ANSWER_MESSAGE}{question_points} {REAL_ANSWER_MESSAGE} {question_answer}")
            print(f"{CURRENT_SCORE_MESSAGE}{user_points}")

        input(CONTINUE_MESSAGE)
        print("\033[H\033[J", end="")

    save_statistics(user_points, correct_answer, incorrect_answer, STAT_FILE_PATH)

    print(FINISH_MESSAGE)
    print(f"{SCORE_MESSAGE}{user_points}")
    print(f"{CORRECT_ANSWER_COUNTER_MESSAGE}{correct_answer}")
    print(f"{INCORRECT_ANSWER_COUNTER_MESSAGE}{incorrect_answer}")


if __name__ == '__main__':
    main()
