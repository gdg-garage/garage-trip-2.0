# x = 399
#
# for _ in range(5):
#     x = sum([int(d) for d in str(x)])
#     x *= 8
#     print(x)

x = 888

print(x)
for _ in range(5):
    x = sum([int(d) for d in str(x)])
    x *= 8
    print(x)