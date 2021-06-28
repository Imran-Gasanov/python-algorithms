def lengthOfLongestSubstring(s):
    """
    >>> lengthOfLongestSubstring("abcabcbb") == 3
    True
    >>> lengthOfLongestSubstring("bbbbb") == 1
    True
    >>> lengthOfLongestSubstring("pwwkew") == 3
    True
    >>> lengthOfLongestSubstring("") == 0
    True
    """
    it_was = []
    max_it_was = []
    for elem in s:
        if elem in it_was:
            if len(max_it_was) < len(it_was):
                max_it_was = it_was
                it_was = [elem]
            else:
                it_was = [elem]
        else:
            it_was.append(elem)
    return len(max_it_was)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
