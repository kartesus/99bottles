class BottleVerse:
    def __init__(self, number):
        self._bottle_number = BottleNumber.forVerse(number)

    def lyrics(self):
        return (
            f"{str(self._bottle_number).capitalize()} of beer on the wall, {self._bottle_number} of beer.\n"
            f"{self._bottle_number.action()}, {self._bottle_number.successor()} of beer on the wall.\n"
        )


class Bottles:
    def __init__(self, verseTemplate=BottleVerse):
        self._verseTemplate = verseTemplate

    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(self.verse(i) for i in range(upper, lower - 1, -1))

    def verse(self, number):
        return self._verseTemplate(number).lyrics()


class BottleNumber:
    @staticmethod
    def forVerse(verse):
        candidates = [BottleNumber6, BottleNumber1,
                      BottleNumber0, BottleNumber]
        return next(candidate(verse) for candidate in candidates if candidate.can_handle(verse))

    @staticmethod
    def can_handle(verse):
        return True

    def __init__(self, verse):
        self._verse = verse

    def container(self):
        return 'bottles'

    def pronoun(self):
        return 'one'

    def quantity(self):
        return str(self._verse)

    def action(self):
        return f'Take {self.pronoun()} down and pass it around'

    def successor(self):
        return BottleNumber.forVerse(self._verse - 1)

    def __str__(self):
        return f'{self.quantity()} {self.container()}'


class BottleNumber0(BottleNumber):
    @staticmethod
    def can_handle(verse):
        return verse == 0

    def quantity(self):
        return 'no more'

    def action(self):
        return 'Go to the store and buy some more'

    def successor(self):
        return BottleNumber.forVerse(99)


class BottleNumber1(BottleNumber):
    @staticmethod
    def can_handle(verse):
        return verse == 1

    def container(self):
        return 'bottle'

    def pronoun(self):
        return 'it'


class BottleNumber6(BottleNumber):
    @staticmethod
    def can_handle(verse):
        return verse == 6

    def quantity(self):
        return '1'

    def container(self):
        return 'six-pack'


print(Bottles().song())
