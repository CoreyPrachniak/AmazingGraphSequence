import matplotlib.pyplot as plt


def calculate_gcd(x, y):
    if x > y:
        calculate_gcd(y, x)

    for i in range(1, x + 1)[::-1]:
        if x % i == y % i == 0:
            return i


def init_len_n(n):
    seq = [None]*n
    seq[0] = 1
    seq[1] = 1

    for i in range(2, n):
        gcd = calculate_gcd(seq[i - 1], i)
        seq[i] = seq[i - 1] + i + 1 if gcd == 1 else int(seq[i - 1]/gcd)

    return seq

print("Input how far you would like to graph the sequence.", end=" ")
print("It should be noted that the author of the sequence is in the YouTube video titled Amazing Graphs - Numberphile.")

n = int(input())
x = list(range(1, n + 1))
y = init_len_n(n)

plt.scatter(x, y)
plt.xlabel("input value")
plt.ylabel("sequence value")
plt.show()
