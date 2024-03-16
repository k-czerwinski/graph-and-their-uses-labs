def is_graphic_sequence(sequence):
    sequence = sorted(sequence, reverse=True)
    while sequence:
        if sequence[0] < 0:
            return False
        if sequence[0] == 0:
            sequence = sequence[1:]
            continue
        for i in range(1, sequence[0] + 1):
            sequence[i] -= 1
        sequence = sorted(sequence[1:], reverse=True)
    return True