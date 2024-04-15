ERRORS_DICT = {
    "out": "You leave the system",
    "noaccess": "You have access to this part",
    "unknown": "Unknown mistake",
    "timeout": "System doesn't respond in time",
    "robot": "You act like a robot"
}


def get_errors(*errors):
    respond = []
    for error in errors:
        respond.append(ERRORS_DICT.get(error, "Unknown"))
    return respond


if __name__ == '__main__':
    print(get_errors("out", "unk,nown"))
