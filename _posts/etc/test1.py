def fill3(tmps: list[float | None]) -> None:
    good = [t for t in tmps if t]
    print(good)
    avg = sum(good) / len(good)
    for i, t in enumerate(tmps):
        tmps[i] = t or avg
    print(tmps)


def fill4(tmps: list[float | None]) -> None:
    good = [t for t in tmps if t is not None]
    avg = sum(good) / len(good)
    tmps = [t or avg for t in tmps]
    print(tmps)


def fill5(tmps: list[float | None]) -> None:
    good = [t for t in tmps if t is not None]
    avg = sum(good) / len(good)
    tmps = [t if t is not None else avg for t in tmps]
    print(tmps)


fill3([2, 3, None, 4, 5, 6, 0])
fill4([2, 3, None, 4, 5, 6, 0])
fill5([2, 3, None, 4, 5, 6, 0])

print(2 ^ 3)
