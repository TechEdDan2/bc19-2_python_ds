def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_lower = to_swap.lower()
    ltr_swap = ''
    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        ltr_swap += ltr
    return ltr_swap

