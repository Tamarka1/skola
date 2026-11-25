import random

class Zviera:
    def __init__(self, meno: str):
        self.meno: str = meno
        self.vek: int = random.randint(1, 100)
        self.zvuky: list[str] = ["BAF", "MEOW", "BRUM", "SSSS"]
        self.predstavenie()
        self.__zjedenych_ludi: int = random.randint(0, 10)

    def predstavenie(self):
        print(f"ja som {self.meno}, mam {self.vek} rokov a idem ta vystrasit")
        self.vystras()

    def vystras(self):
        print(self.zvuky[random.randint(0, 3)])

    def zjedz_cloveka(self):
        self.__zjedenych_ludi += 1


class Kniha:
    def __init__(self, autor, meno):
        self.__autor: str = autor
        self.__meno: str = meno
        self.__rok: int = random.randint(1600, 2026)

    def info(self):
        return [self.__autor, self.__meno, self.__rok]


class Kniznica():
    def __init__(self):
        self.__knihy: list[list[int | str]] = []

    def dodaj(self, kniha: list[int | str]):
        self.__knihy.append(kniha)

    def vypis_knihy(self):
        for kniha in self.__knihy:
            print(kniha)

kniznica = Kniznica()
knihy = [["ja", "ahoj svet"], ["ty", "hello world"]]
for k in knihy:
    kniznica.dodaj(k)
kniznica.vypis_knihy()
