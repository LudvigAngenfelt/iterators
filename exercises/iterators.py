"""Övningar på iterators."""


class Cubes():
    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        self.current += 1
        return self.current ** 3

    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """


class Primes():
#    def __iter__(self):
#        self.counter = 1
#        self.primes = []
#        self.y = 0
    pass



    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """



class Fibonacci():

    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        self.values = []

    def __iter__(self):
        return self

    def next(self):
        if len(self.values) < 2:
            self.values.append(1)
        else:
            self.values = [self.values[-1], self.values[-1] + self.values[-2]]
        return self.values[-1]


    #def __init__(self):
    #    self.a, self.b = 0,1
    #    self.numbers = self.a + self.b
#
#        return self
#
#    def next(self):
#        self.a, self.b = self.b, self.a + self.b
#
#        return
#
#    def __next__(self):
#        return self.next()
#
#    if __name__ == '__main__':
#        MY_FIBONACCI_NUMBERS = Fibonacci()
#        for fibonacci_number in MY_FIBONACCI_NUMBERS:
#            print(fibonacci_number)



class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """


class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """


class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    pass
