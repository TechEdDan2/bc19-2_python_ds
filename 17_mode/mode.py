def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # create a dictionary to hold the num key and count value
    mode_count = {}
    for num in nums:
        mode_count[num] = mode_count.get(num, 0) + 1

    # Find the highest repeated number
    max_mode = 0
    for val in mode_count.values():
        if val > max_mode:
            max_mode = val

    # Use the max_mode value to match the key
    for (num_key, mode_val) in mode_count.items():
        if mode_val == max_mode:
            return num_key

