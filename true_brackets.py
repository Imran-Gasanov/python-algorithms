def is_balanced(exp):
    """
    Time Complexity: O(n)
    Space complexity: O(n)
    >>> is_balanced('(((((((') == False
    True
    >>> is_balanced('()') == True
    True
    >>> is_balanced('{}}}{{()') == False
    True
    """
    if len(exp) % 2 != 0:
        return False
    round_brackets = []
    curly_brackets = []
    square_brackets = []
    for elem in exp:
        if elem == '(':
            round_brackets.append(elem)
        elif elem == '{':
            curly_brackets.append(elem)
        elif elem == '[':
            square_brackets.append(elem)
        elif elem == ')':
            try:
                round_brackets.remove('(')
            except:
                return False
        elif elem == '}':
            try:
                curly_brackets.remove('{')
            except:
                return False
        elif elem == ']':
            try:
                square_brackets.remove('[')
            except:
                return False
    if len(round_brackets) != 0 or len(curly_brackets) != 0 or len(square_brackets) != 0:
        return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
