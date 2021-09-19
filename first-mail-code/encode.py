def main():
    text = "See you at Garage Trip 2.0!"
    ascii_codes = (ord(i) for i in text)
    shift = -42
    shifted = (i + shift for i in ascii_codes)
    hexed = (hex(i).replace("0x", "") for i in shifted)
    print(' '.join(hexed))


if __name__ == '__main__':
    main()
