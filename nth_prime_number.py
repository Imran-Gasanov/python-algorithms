def nth_prime_numbers(n):
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


print(nth_prime_numbers(10001))
