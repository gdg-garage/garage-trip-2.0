def main():
    input_text = "29 3b 3b -a 4f 45 4b -a 37 4a -a 1d 37 48 37 3d 3b -a 2a 48 3f 46 -a 8 4 6 -9"
    ints = [int(i, 16) for i in input_text.split()]
    for shift in range(-128, 128):
        try:
            print(''.join((chr(i + shift) for i in ints)))
        except Exception:
            pass


if __name__ == '__main__':
    main()
