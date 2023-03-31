# * -> unlimited params
def add(*nums):
    print(nums[-1])
    total = 0
    for n in nums:
        total += n
    return total


# print(add(2, 3, 5, 8, 0, 299, 200))


def calculate(n, **kwargs):
    # for key, val in kwargs.items():
    #     print(key)
    # print(kwargs["sub"])
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)


# calculate(10, add=20, mult=100)


class Bike:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.color = kw.get("color")


sus = Bike(make = "ktm", color = "nord")
# print(sus.color)
