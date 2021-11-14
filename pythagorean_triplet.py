from math import sqrt

def find_pythag_triplet(n: int):
    # Finds the pythagorean triplets that sum up to n
    a = 1
    triplets = []

    while a < n:
        b = a + 1
        while a + b < n:
            c = sqrt(a**2 + b**2)
            if a + b + c == n:
                triplets.append((a, b, int(c)))
            b += 1
        a += 1
    return triplets

print(find_pythag_triplet(1500))
