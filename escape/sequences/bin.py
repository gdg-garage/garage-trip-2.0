# x = 6
x = 8
print(x, bin(x))

# for _ in range(6):
#     x ^= (x * 2)
#     # print(x)
#     x += 1
#     print(x, bin(x))

for _ in range(6):
    x ^= (x * 2)
    # print(x)
    # x += 1
    print(x, bin(x))
