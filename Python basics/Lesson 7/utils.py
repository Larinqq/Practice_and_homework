import json


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
