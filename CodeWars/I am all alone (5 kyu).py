from collections import deque


def to_map(rows: list[str]):
    m = [None] * len(rows)

    for y in range(len(rows)):
        m[y] = [''] * len(rows[y])

        for x in range(len(rows[y])):
            m[y][x] = rows[y][x]
    
    return m


def find_target(house: list[list[str]]) -> tuple[int, int]:
    for y in range(len(house)):
        for x in range(len(house[0])):
            if house[y][x] == 'X':
                return y, x
    
    raise Exception('Traget is not finded')

def all_alone(house: list[list[str]]) -> bool:
    '''
    Повертає `True`, якщо ціль вдома одна, інакше `False`.

    `X` - ціль

    `o` - стороння людина

    `#` - стіна
    '''

    target = find_target(house)
    house[target[0]][target[1]] = '#'
    positions = deque([target])

    shifts = ((1,0), (-1,0), (0,1), (0,-1))

    while positions:
        curr_y, curr_x = positions.pop()

        for shift_y, shift_x in shifts:
            y = curr_y + shift_y
            x = curr_x + shift_x

            if house[y][x] == 'o':
                return False

            if house[y][x] == ' ':
                positions.appendleft((y,x))
                house[y][x] = '#'
    
    return True


print(all_alone(to_map([
    '  o                o        #######',
    '###############             #     #',
    '#             #        o    #     #',
    '#  X          ###############     #',
    '#                                 #',
    '###################################'
]))) # -> True

print(all_alone(to_map([
    '#################             ',
    '#     o         #   o         ',
    '#          ######        o    ',
    '####       #                  ',
    '   #       ###################',
    '   #                         #',
    '   #                  X      #',
    '   ###########################'
]))) # -> False