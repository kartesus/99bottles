def no_more(verse):
    return (
        'No more bottles of beer on the wall, '
        'no more bottles of beer.\n'
        'Go to the store and buy some more, '
        '99 bottles of beer on the wall.\n'
    )


def last_one(verse):
    return (
        '1 bottle of beer on the wall, '
        '1 bottle of beer.\n'
        'Take it down and pass it around, '
        'no more bottles of beer on the wall.\n'
    )


def penultimate(verse):
    return (
        '2 bottles of beer on the wall, '
        '2 bottles of beer.\n'
        'Take one down and pass it around, '
        '1 bottle of beer on the wall.\n'
    )


def default(verse):
    return (
        f"{verse.number} bottles of beer on the wall, "
        f"{verse.number} bottles of beer.\n"
        'Take one down and pass it around, '
        f"{verse.number - 1} bottles of beer on the wall.\n"
    )


class Verse:
    def __init__(self, number, lyrics):
        self.number = number
        self.lyrics = lyrics

    def text(self):
        return self.lyrics(self)


class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, finish, start):
        return '\n'.join(self.verse(verse_number) for verse_number in self.down_to(finish, start))

    def verse(self, number):
        return self.verse_for(number).text()

    def verse_for(self, number):
        if number == 0:
            return Verse(number, no_more)
        elif number == 1:
            return Verse(number, last_one)
        elif number == 2:
            return Verse(number, penultimate)
        else:
            return Verse(number, default)

    @staticmethod
    def down_to(max, min):
        return range(max, min - 1, -1)


print(Bottles().song())
