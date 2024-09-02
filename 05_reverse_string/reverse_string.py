def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # Slice skip the start value, skip the step value, -1 step size means it will step back to front by 1
    return phrase[::-1]

    
 