class Chef:
    def __init__(self):
        self.xp = 20

    def tea(self):
        print("grenn tea with cinammon")


class HomeCook(Chef):
    def __init__(self):
        super().__init__()

    def rice(self):
        print("noooo")

    def tea(self):
        super().tea()
        print("also ginger and peper")


sali = Chef()
sali.tea()

past = HomeCook()
past.tea()

print(past.xp)

alph = ["a", "b", "c", "d"]

print(alph[1:2])
