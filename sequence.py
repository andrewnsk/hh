def knuth_morris_pratt(sequence):
    """
    Knuth-Morris-Pratt string matching
    :param sequence:
    :return: position
    """
    shift = get_shift(sequence)
    start_pos = 0
    match_len = 0
    pattern_len = len(sequence)
    for c in get_sequence():
        while match_len >= 0 and sequence[match_len] != c:
            start_pos += shift[match_len]
            match_len -= shift[match_len]
        match_len += 1
        if match_len == pattern_len:
            return start_pos + 1


def get_sequence():
    integer = 1
    while True:
        str_int = str(integer)
        for char in str_int:
            yield char
        integer += 1


def get_shift(sequence):
    shifts = [None] * (len(sequence) + 1)
    shift = 1
    for pos in range(len(sequence) + 1):
        while shift < pos and sequence[pos-1] != sequence[pos-shift-1]:
            shift += shifts[pos-shift-1]
        shifts[pos] = shift
    return shifts


def find_sequence(sequence):
    return knuth_morris_pratt(str(sequence))


if __name__ == '__main__':
    print(find_sequence(4896))
