# A monochrome screen is stored as a single array of bytes, allowing eight consecutive
# pixels to be stored in one byte. The screen has width w, where w is divisible by 8
# (that is, no byte will be split across rows). The height of the screen, of course,
# can be derived from the length of the array and the width. Implement a function
# drawHorizontalLine(byte[] screen,intwidth,intxl,intx2,inty) which draws a horizontal
# line from (x1, y) to (x2, y).

def draw_line(screen, width, x1, x2, y):
    start_offset = x1 % 8
    first_full_byte = x1 // 8
    if start_offset != 0:
        first_full_byte += 1
    end_offset = x2 % 8
    last_full_byte = x2 // 8
    if end_offset != 7:
        last_full_byte -= 1
    for b in range(first_full_byte, last_full_byte + 1):
        screen[y * (width / 8) + b] = int('0xff', 16)
    start_mask = int('0xff', 16) >> start_offset
    end_mask = ~(int('0xff', 16) >> (end_offset + 1))
    if first_full_byte == last_full_byte:
        screen[y * (width / 8) + first_full_byte] |= (start_mask & end_mask)
    else:
        if start_offset != 0:
            screen[y * (width / 8) + first_full_byte - 1] |= start_mask
        if end_offset != 7:
            screen[y * (width / 8) + last_full_byte + 1] |= end_mask

# if __name__ == "__main__":
#     print(draw_line(screen, width, x1, x2, y))