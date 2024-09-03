def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count_dict = {}
    # Keeping my original idea for solving this problem for reference 
    # for ltr in set(phrase):
    #     frequency = phrase.count(ltr)
    #     letter_count_dict[ltr] = frequency

    # More efficient 
    for ltr in phrase:
        letter_count_dict[ltr] = letter_count_dict.get(ltr, 0) + 1

    return letter_count_dict