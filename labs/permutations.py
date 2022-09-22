import cProfile


def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n - 1) * n


# in a keyspace of all permutations, how long will it take to check
def counter(n):
    """
    simulates what you do for each key as part of an attack
    """
    cnt = 0

    for i in range(n):
        cnt += 1

    return cnt


# for i in range(15):
#     print(counter(faculty(i)))

cProfile.run("counter(faculty(13))")
