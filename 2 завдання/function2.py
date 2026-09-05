def numbers():
    result = []

    for i in range(30, 61):
        if i % 3 == 0:
            result.append(i)

    return result