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
            if category_question["asked"] == "False":
                game_field += f"{str(category_price).ljust(MAX_CATEGORY_POINTS_LEN+SPACES_BETWEEN_POINTS)}"
            else:
                game_field += f"{str('').ljust(MAX_CATEGORY_POINTS_LEN + SPACES_BETWEEN_POINTS)}"

        game_field += "\n"

    return game_field
