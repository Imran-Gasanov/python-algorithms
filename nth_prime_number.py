def nth_prime_numbers(n):
    """
        >>> nth_prime_numbers(1) == 2
        True
        >>> nth_prime_numbers(6) == 13
        True
        >>> nth_prime_numbers(10001) == 104743
        True
        """
    list_of_prime_number = []
    curr = 2
    count = 0
    while count < n:
        curr_is_prime = 'yes'
        for elem in list_of_prime_number:
            if curr % elem == 0:
                curr_is_prime = 'no'
                break
        if curr_is_prime == 'yes':
            list_of_prime_number.append(curr)
            count += 1
        curr += 1
    return curr - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

