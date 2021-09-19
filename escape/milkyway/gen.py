"""
Circle is centered to the position
"""

import random

index = 0
NUMBERS = list(range(160))
random.shuffle(NUMBERS)
FONT_SIZE = 16
CIRCLE_RADIUS = 2
X_LABEL_SHIFT = CIRCLE_RADIUS
Y_LABEL_SHIFT = FONT_SIZE - (FONT_SIZE * .3)
CHAR_WIDTH = FONT_SIZE * 0.6
BORDER = 1


def intersect(l1, r1, l2, r2):
    return max(l1[0], l2[0]) <= min(r1[0], r2[0]) and \
           max(l1[1], l2[1]) <= min(r1[1], r2[1])


def collision(occupied, top_left, bottom_right):
    for tl, br in occupied:
        if intersect(tl, br, top_left, bottom_right):
            return True


def dot_bounding_box(x, y):
    return (x - CIRCLE_RADIUS, y - CIRCLE_RADIUS), (x + CIRCLE_RADIUS, y + CIRCLE_RADIUS)


def text_bounding_box(x, y, chars):
    return (x - CIRCLE_RADIUS - BORDER, y - CIRCLE_RADIUS - BORDER), (
        x + CIRCLE_RADIUS + (chars * CHAR_WIDTH) + BORDER, (y + FONT_SIZE - CIRCLE_RADIUS) + BORDER)


def dot(occupied, bound, pos=None, force_label=None):
    global index
    if pos is None:
        x = random.randint(CIRCLE_RADIUS + BORDER, bound[0] - FONT_SIZE - BORDER)
        y = random.randint(CIRCLE_RADIUS + BORDER, round(bound[1] - (CHAR_WIDTH * 3))) - BORDER  # max 3 chars (digits)
    else:
        x, y = pos
    labeled = False
    chars = 0
    if force_label is None:
        if random.random() < .025:
            labeled = True
    else:
        labeled = True

    if index >= len(NUMBERS):
        labeled = False

    if labeled:
        chars = len(str(NUMBERS[index]))
    opacity = min(1., random.random() + .2) if not labeled else 1

    if collision(occupied, *dot_bounding_box(x, y)) or (
            labeled and collision(occupied, *text_bounding_box(x, y, chars))):
        return dot(occupied, bound, pos=pos, force_label=force_label)

    r = f'<circle cx="{x}" cy="{y}" r="{CIRCLE_RADIUS}" style="fill: rgba(255, 255, 255, {opacity});"/>'
    occupied.append(dot_bounding_box(x, y))

    if labeled:
        label_str = f"{NUMBERS[index]}"
        r += f'<text x="{x}" y="{y}" dx="{X_LABEL_SHIFT}" dy="{Y_LABEL_SHIFT}">{label_str}</text>'
        occupied.append(text_bounding_box(x, y, chars))
        index += 1

    return r


def scale(pos, size):
    original_size = (50, 35)
    return round(pos[1] / original_size[0] * size[0]), round(pos[0] / original_size[1] * size[1])


def draw():
    size = (2970, 2010)  # A4 mm * 10
    occupied = []
    with open("milkyway.svg", "w") as img, open("path.txt", "w") as desc:
        img.write(
            f'<svg viewBox="0 0 {size[0]} {size[1]}" xmlns="http://www.w3.org/2000/svg" style="background-color: black;">')
        img.write(f'<style>text {{ font-size: {FONT_SIZE}px; font-family: "monospace"; fill: white; }}</style>')
        old_index = index
        for i in map(lambda x: scale(x, size),
                     [(15, 2), (23, 9), (29, 9), (29, 6), (24, 6), (15, 13), (8, 13), (3, 10), (3, 5), (8, 2), (13, 2),
                      (14, 6), (9, 6), (9, 10), (13, 10), (19, 5), (23, 2), (30, 2), (33, 5), (33, 10), (30, 13),
                      (24, 13), (19, 10), (16, 7)]):
            img.write(dot(occupied, size, pos=i, force_label=True))
        desc.write(f"8 is {', '.join(map(str, NUMBERS[old_index:index]))}\n")

        old_index = index
        for i in map(lambda x: scale(x, size),
                     [(18, 24), (24, 26), (29, 22), (29, 18), (33, 18), (33, 25), (26, 30), (18, 28), (14, 23), (6, 23),
                      (6, 29), (3, 29), (3, 20), (11, 18), (16, 18)]):
            img.write(dot(occupied, size, pos=i, force_label=True))
        desc.write(f"5 is {', '.join(map(str, NUMBERS[old_index:index]))}\n")

        old_index = index
        for i in map(lambda x: scale(x, size),
                     [(8, 47), (3, 47), (3, 36), (8, 36), (8, 44), (14, 41), (26, 36), (34, 33), (34, 38), (20, 43)]):
            img.write(dot(occupied, size, pos=i, force_label=True))
        desc.write(f"7 is {', '.join(map(str, NUMBERS[old_index:index]))}\n")

        for i in range(6000):
            img.write(dot(occupied, size))

        # for i in occupied:
        #     x, y = i[0][0], i[0][1]
        #     w, h = i[1][0] - x, i[1][1] - y
        #     f.write(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" style="fill: rgba(255, 255, 255, .25);" />')
        img.write('</svg>')


if __name__ == '__main__':
    draw()
