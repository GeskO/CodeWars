"""Возвращем Yes если True и No если False"""
"""Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false."""


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


def bool_to_word_v2(boolean):
    return "Yes" if boolean else "No"


bool_to_word(True)
bool_to_word(False)
