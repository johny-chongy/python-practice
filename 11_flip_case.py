def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_phrase = ''
    for char in list(phrase):
        if char.lower() == to_swap.lower():
            flipped_phrase += char.swapcase()
        else:
            flipped_phrase += char

    return flipped_phrase