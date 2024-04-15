def shift_encode(string):
    """
    Encodes string adding one to each letter ascis's code
    :param string:
    :return string:
    """
    final_string = ""
    for letter in string:
        final_string += chr(ord(letter)+1)
    return final_string


def shift_decode(string):
    """
    Decodes string subtracting one to each letter ascis's code
    :param string:
    :return string:
    """
    final_string = ""
    for letter in string:
        final_string += chr(ord(letter)-1)
    return final_string


if __name__ == '__main__':
    test_string = "Hello World!"
    print(test_string == shift_decode(shift_encode(test_string)))
