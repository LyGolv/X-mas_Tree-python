def draw_tree_on_card(height: int, interval: int, coord_x, coord_y, card):
    height *= 2
    card[coord_y][coord_x] = 'X'
    card[coord_y + 1][coord_x] = "^"
    count = 0
    for i in range(3, height + 1, 2):
        card[coord_y + i // 2 + 1][coord_x - i // 2] = "/"
        for k in range(-i // 2 + 2, i // 2):
            if (k + i // 2) % 2 == 0:
                count += 1
                card[coord_y + i // 2 + 1][coord_x + k] = "O" if count % interval == 1 or interval == 1 else "*"
            else:
                card[coord_y + i // 2 + 1][coord_x + k] = "*"
        card[coord_y + i // 2 + 1][coord_x + i // 2] = "\\"
    card[coord_y + (height // 2 + 1)][coord_x - 1] = '|'
    card[coord_y + (height // 2 + 1)][coord_x + 1] = '|'


def create_card(width: int, height: int, width_symbol: str = '-', height_symbol: str = '|', pattern: str = ' '):
    card = [[]]
    card[0] += [width_symbol] * width
    for _ in range(height - 2):
        line = [height_symbol] + [pattern] * (width - 2) + [height_symbol]
        card += [line]
    card += [[width_symbol] * width]
    return card


def display_card(card):
    for line in card:
        print(''.join(line))


def draw_postcard_tree(arg, width=50, height=30, on_card=True):
    card = create_card(width, height)
    if len(arg) < 4:
        on_card = False
        card = create_card(int(arg[0]) * 2, int(arg[0]) + 4, '', '')
        arg += [0] * (len(arg) % 4)
        arg[2] = 1
        arg[3] = int(arg[0])

    for elem in range(0, len(arg), 4):
        h, i, y, x = map(int, arg[elem:elem + 4])
        draw_tree_on_card(h, i, x, y, card)

    if on_card:
        line = "Merry Xmas"
        for i in range(-len(line) // 2, len(line) // 2):
            card[height - 3][width // 2 + i] = line[i + len(line) // 2]
    else:
        del card[0]
        del card[len(card) - 1]

    display_card(card)


def main():
    info = input()
    if not info.replace(' ', '').isdigit():
        return
    draw_postcard_tree(info.split())


if __name__ == "__main__":
    main()
