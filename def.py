def hello():
    print("Привет")


hello()


def hello1(name: str):
    print("Привет,", name)


hello1("Rumi")


def multiply(a: float, b: float) -> float:
    res = a * b
    return res


res = multiply(2, 4)
print(res)
