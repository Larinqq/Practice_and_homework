import json
from config import MAX_CATEGORY_TITTLE_LEN, MAX_CATEGORY_POINTS_LEN, SPACES_BETWEEN_POINTS


def questions_load(question_path):
    """
    Loads questions from given json file
    :param question_path: path to file
    :return: dict of questions
    """
    with open(question_path, 'r') as file:
        raw_json = file.read()
        questions = json.loads(raw_json)

    return questions


def draw_gamescreen(questions):
    """
    Draws gamescreen based on given question. Divides data on categories and point
    :param questions: dict
    :return: pretty string
    """
    game_field = ''
    for category, category_data in questions.items():
        game_field += f"{str(category).ljust(MAX_CATEGORY_TITTLE_LEN)}"

        for category_price, category_question in category_data.items():
            if not category_question["asked"]:
                game_field += f"{str(category_price).ljust(MAX_CATEGORY_POINTS_LEN + SPACES_BETWEEN_POINTS)}"
            else:
                game_field += f"{str('').ljust(MAX_CATEGORY_POINTS_LEN + SPACES_BETWEEN_POINTS)}"

        game_field += "\n"

    return game_field


def get_question(verified_data, questions_dict):
    """
    Gets question text from verified data
    :param verified_data: tuple (category, price)
    :param questions_dict: dict questions
    :return: string, question text
    """
    selected_category, selected_price = verified_data
    questions_dict[selected_category][selected_price]["asked"] = True
    return questions_dict[selected_category][selected_price]["question"]


def get_answer(verified_data, questions_dict):
    """
    Gets answer text from verified data
    :param verified_data: tuple (category, price)
    :param questions_dict: dict questions
    :return: string, answer text
    """
    selected_category, selected_price = verified_data
    return questions_dict[selected_category][selected_price]["answer"]


def split_user_input(raw_input):
    """
    splits given string separated with space
    :param raw_input: string
    :return: tuple
    """
    return tuple(raw_input.split())


def verify_user_data(user_data, questions_dict):
    """
    Verifies given data tuple, checks: len, presents in the dict and legitimate
    :param user_data: tuple with category and price
    :param questions_dict: dict questions
    :return: bool: True/False
    """
    if len(user_data) != 2:
        return False

    if user_data[0] not in questions_dict:
        return False

    if user_data[1] not in questions_dict[user_data[0]]:
        return False

    if questions_dict[user_data[0]][user_data[1]]["asked"]:
        return False

    return True
