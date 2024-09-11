def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = set("aeiou")

    reverse_aeiou = list(s)

    v1_pos = 0
    v2_pos = len(s) - 1

    while v1_pos < v2_pos:
        if reverse_aeiou[v1_pos].lower() not in vowels:
            v1_pos += 1
        elif reverse_aeiou[v2_pos].lower() not in vowels:
            v2_pos -= 1
        else:
            reverse_aeiou[v1_pos], reverse_aeiou[v2_pos] = reverse_aeiou[v2_pos], reverse_aeiou[v1_pos]
            v1_pos += 1
            v2_pos -= 1

    return "".join(reverse_aeiou)