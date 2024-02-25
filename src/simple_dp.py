'''
{
    ...
    number: set_id
    ...
}
set_id: 1: the number is pythagoren triples of set 1
set_id: 2: the number is pythagoren triples of set 2
set_id: 3: the number is pythagoren triples of set 1 and 2 at the same time
'''
import argparse

def generate_pair(end=0, start=0):
    count = start
    square = start ** 2
    while True:
        if end > 0 and count == end:
            return
        square += count + count + 1
        count += 1
        yield count, square

def init_map(limit=0):
    n_to_s = {}
    s_to_n = {}
    for n, s in generate_pair(end=limit):
        n_to_s[n] = s
        s_to_n[s] = n
    return n_to_s, s_to_n

def step(number: int, number_to_square: dict, square_to_number: dict, note: dict):
    _note = note.copy()
    if number not in note:
        _note[number] = 0
    set_1, set_2 = {**_note, number: _note[number] | 1}, {**_note, number: _note[number] | 2}

    ret = []
    for next_note in set_1, set_2:
        # check the number is c
        if number in note and note[number] == 3:
            continue

        # find c with the number as b
        b = number
        square_b = number_to_square[number]
        for a in sorted(note):
            if a >= b:
                break
            square_a = number_to_square[a]
            square_c = square_a + square_b
            if square_c in square_to_number:
                c = square_to_number[square_c]
                if c not in next_note:
                    next_note[c] = 0
                next_note[c] |= next_note[a] & next_note[b]
        if next_note[number] != 3:
            ret += [next_note]
    return ret

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('limit', type=int, default=0)

    args = parser.parse_args()

    map_number_to_square, map_square_to_number = init_map(args.limit)

    notes = [{1: 1}]
    next_notes = []
    for number in range(2, args.limit + 1):
        print('number:', number, 'len(notes):', len(notes))
        for note in notes:
            next_notes += step(number, map_number_to_square, map_square_to_number, note)
        notes = next_notes
        next_notes = []
