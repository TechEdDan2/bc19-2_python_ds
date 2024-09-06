def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    if operation == 'add':
        if make_int:
            a = round(a)
            b = round(b)
        sum_val = a + b
        return f"{message} {sum_val}"

    elif operation == 'subtract':
        if make_int:
            a = round(a)
            b = round(b)
        dif_val = a - b
        return f"{message} {dif_val}"

    elif operation == 'multiply':
        if make_int:
            a = round(a)
            b = round(b)
        product_val = a * b
        return f"{message} {product_val}"

    elif operation == 'divide':
        if make_int:
            a = round(a)
            b = round(b)
        quotient_val = a * b
        return f"{message} {quotient_val}"
    
    else:
        return None
